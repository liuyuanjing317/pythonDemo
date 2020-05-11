import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 启动浏览器，获取网页源代码
browser = webdriver.Chrome(chrome_options=chrome_options)
mainUrl = "http://zwfw.guizhou.gov.cn/qlqdlist.do?areacode=520115"
browser.get(mainUrl)

elements = browser.find_elements_by_class_name("bsqd_btn");

actions = ActionChains(browser)
for i in elements:
    actions.click(i)
    time.sleep(5)
    t=browser.page_source()
    print(t)



browser.quit()
