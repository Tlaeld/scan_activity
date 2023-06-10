# 一个简单的扫描程序

## 使用步骤

1、安装依赖
    `pip install -r requirements.txt`

2、将config内的`bot_def.json`文件修改并复制为`bot.json`

3、在根目录里新建一个`JD_COOKIE.txt`文件将COOKIE放在里面，一个cookie一行

4、运行程序`python bot.py`

## 进阶
自己摸索放在🐉里运行

    `task scan_activity/bot.py`
    

推荐半小时运行一次

## 特性
1、cookie一般情况下只使用一次，后续用缓存数据即可，🤫-可能在cookie失效情况下也能用-

2、带有活动缓存，只发送新活动

