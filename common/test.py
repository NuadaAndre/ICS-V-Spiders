import os
import platform
import time

"""
from selenium import webdriver

if platform.system() == "Windows":
    driverfile = os.path.join(os.path.abspath(os.path.dirname(__file__)), "geckodriver.exe")
elif platform.system() == "Linux":
    driverfile = os.path.join(os.path.abspath(os.path.dirname(__file__)), "geckodriver")
else:
    pass

# 设置Firefox的启动选项
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('-headless')

browser = webdriver.Firefox(firefox_options=firefox_options,executable_path=driverfile)

# 隐式等待10秒，待页面元素全部加载完毕
browser.implicitly_wait(10)
try:
    browser.get('http://www.cnvd.org.cn/flaw/list.htm?flag=true')
    #title = browser.find_element_by_xpath("//address").text.strip()
    browser.refresh()
    time.sleep(0.3)
    print(browser.page_source)
    #print(title)
except Exception as e:
    print(e)

browser.close()
"""

from selenium import webdriver




from selenium import webdriver

if platform.system() == "Windows":
    driverfile = os.path.join(os.path.abspath(os.path.dirname(__file__)), "geckodriver.exe")
elif platform.system() == "Linux":
    driverfile = os.path.join(os.path.abspath(os.path.dirname(__file__)), "geckodriver")
else:
    pass

# 设置Firefox的启动选项
#firefox_options = webdriver.FirefoxOptions()
#firefox_options.add_argument('-headless')

browser = webdriver.Firefox(executable_path=driverfile)
