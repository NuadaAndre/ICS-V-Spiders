#coding:utf8

#Author: tsuki
#Date: 2017-12-09
#Time: 13:48
import os
import platform
import time
from selenium import webdriver
from common.log.MyLog import MyLog

class Webdriver():

    # 初始化并加载浏览器
    def __init__(self):

        __driver = "geckodriver"
        self.logger = MyLog().getLogger()

        # 获取驱动目录
        driverpath = ""
        if platform.system() == "Windows":
            driverpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), __driver + ".exe")

        elif platform.system() == "Linux":
            driverpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), __driver)

        else:
            self.logger.error("浏览器驱动文件出错：未在以下文件夹下"
                              "查找到驱动文件{}：{}".format(__driver, os.path.dirname(driverpath)))

        #print(driverpath)

        # 设置Firefox的启动选项
        options = webdriver.FirefoxOptions()
        #options.add_argument('-headless')

        self.browser = webdriver.Firefox(firefox_options=options, executable_path=driverpath)

        # 隐式等待10秒，待页面元素全部加载完毕
        self.browser.implicitly_wait(10)


    # 获取页面源代码
    def getPage_source(self, url):
        self.browser.get(url)
        # 刷新页面获取完整的页面
        self.browser.refresh()
        time.sleep(0.3)
        return self.browser.page_source

    # 获取cookie
    def getCookies(self, url):
        self.browser.get(url)
        # 刷新页面  重新加载页面
        self.browser.refresh()
        time.sleep(0.3)
        res = self.browser.get_cookies()
        # (list)res = [{'domain': 'www.cnvd.org.cn', 'httpOnly': True, 'expiry': 1527519798.543155, 'secure': False, 'value': '1c652993f3cfb95e68057050a70b69ef', 'name': '__jsluid', 'path': '/'}, {'domain': 'www.cnvd.org.cn', 'httpOnly': False, 'expiry': 1495987361, 'secure': False, 'value': '1495983761.518|0|lKyWZPLs%2FizLz8vTlbysQtasKFw%3D', 'name': '__jsl_clearance', 'path': '/'}]
        cookie = ""
        for r in res:
            cookie += (r['name'] + "=" + r["value"] + ";")
        return cookie

    # 关闭浏览器
    def close(self):
        self.browser.close()
