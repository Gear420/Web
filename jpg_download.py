'''
Created on 2017-3-17

@author: Gear
'''

# -*- coding: utf-8 -*-
#!/usr/bin/python
#论面向过程编程！！！！（mdzz）
import re
import bs4
import sys
import os
from bs4 import BeautifulSoup
import requests


def choiceType(choice):#选择你的喜好（口胡）
    if(choice == 1):
        url = "http://www.apic.in/hentai/zukongfuli"
    if(choice == 2):
        url = "http://www.apic.in/hentai/jueduilingyu"
    if(choice == 3):
        url = "http://www.apic.in/hentai/pangci"
    if(choice == 4):
        url = "http://www.apic.in/zhifu/lolikong"  
    if(choice == 5):
        url = "http://www.apic.in/zhifu/baihe"  
    if(choice == 6):
        url = "http://www.apic.in/hentai/juru"
    if(choice>6):
        return "error"
    return url#返回一个url链接
def sum_imgpackge(firsturl,imgpck,imginfo):#显示此界面的图包数量以及你选择的图包
    try:
        r = requests.get(firsturl,timeout=100)
        r.raise_for_status()
        r.encoding = 'utf-8'
        demo = r.text
        soup = BeautifulSoup(demo,"html.parser")
        soup2 = soup.find_all('h2')
        for i in range(len(soup2)):
            imginfo.append(soup2[i].a.attrs['title'])
            imgpck.append(soup2[i].a.attrs['href'])
    except:
        return "error" #返回一个含有全部图包地址的列表
def imgpackge(url):#用来返回一个有该链接全部图片链接的列表
    try:
        r = requests.get(url,timeout=100)
        r.raise_for_status()
        r.encoding = 'utf-8'
        demo = r.text
        s = re.findall(r'http://img.gov.com.de/201\d/0\d/[ashiura-]*\w*-apic-in-\d*.jpg',demo)
        return s
    except:
        return "error"
def main():#把图片保存到路径里；
    url = "http://www.apic.in/hentai"
    path = "f:/test/"
    if os.path.exists(path):#判断目录是否存在,不存在则创建
        pass
    else:
        os.makedirs(path)
    choice = input("做出你的选择(不可描述的事物):")
    choice = (int)(choice)
    firsturl = choiceType(choice)
    imgpck = []
    imginfo = []
    print("当前的图包数量为9\n")
    sum_imgpackge(firsturl,imgpck,imginfo)
    print(imgpck)
    for i in range(9):
        s=[]
        path = "f:/test/" + imginfo[i] + '/'
        if os.path.exists(path):#判断目录是否存在,不存在则创建
            pass
        else:
            os.makedirs(path)
        #sum2 = input("输入你要抓取的图片页数（你输了也没用）:")
        s=imgpackge(imgpck[i])
        print(s)
        count = '1'
        for j in range(len(s)):
            path = "f:/test/" + imginfo[i] + '/' + count + '.jpg'
            r = requests.get(s[j])
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
            print("一个保存完成")
            count = count + '1'
main()       