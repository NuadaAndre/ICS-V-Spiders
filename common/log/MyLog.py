#coding:utf8

#Author: tsuki
#Date: 2017-11-14
#Time: 15:37

#日志相关功能接口
import os
import datetime
import logging
import logging.config

class MyLog():

    def getLogger(self):
        # 获取logger实例，如果参数为空则返回root logger
        logger = logging.getLogger()

        # 文件日志
        logfile = os.path.join(os.path.abspath(os.path.dirname(__file__)), str(datetime.date.today()) + ".log")
        file_handler = logging.FileHandler(logfile, encoding="utf-8")

        # 指定日志输出格式
        formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)-7s: %(message)s")
        file_handler.setFormatter(formatter)

        # 指定日志的最低输出级别，默认为WARN级别
        logger.setLevel(logging.INFO)

        # 为logger添加的日志处理器
        logger.addHandler(file_handler)
        return logger
