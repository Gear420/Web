<?php
/**
 * Created by PhpStorm.
 * User: zhangxingyu
 * Date: 2018/5/30
 * Time: 下午1:23
 */




//框架入口文件
define('DS', DIRECTORY_SEPARATOR);    //定义目录分隔符（上面用到过）
define('ROOT_PATH', __DIR__ . DS);    //定义框架根目录
require 'sys/start.php';    //引入框架启动文件
core\App::run();