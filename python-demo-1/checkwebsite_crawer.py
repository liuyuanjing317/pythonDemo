import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
根据table的id属性和table中的某一个元素定位其在table中的位置
table包括表头，位置坐标都是从1开始算
tableId：table的id属性
queryContent：需要确定位置的内容
"""
def get_table_content(tableId,queryContent):
    arr = []
    arr1 = []
    table_loc = webdriver.find_element_by_id(tableId)
    # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
    table_tr_list = webdriver.find_element(*table_loc).find_elements(By.TAG_NAME, "tr")
    for tr in table_tr_list:
        arr1 = (tr.text).split(" ") #以空格拆分成若干个(个数与列的个数相同)一维列表
        print(tr.text)
        # print(arr1)
        arr.append(arr1)    #将表格数据组成二维的列表

    #循环遍历table数据，确定查询数据的位置
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if queryContent== arr[i][j]:
                print("%r坐标为(%r,%r)" %(queryContent,i+1,j+1))





chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 启动浏览器，获取网页源代码
browser = webdriver.Chrome(chrome_options=chrome_options)
mainUrl = "http://zwfw.guizhou.gov.cn/qlqdlist.do?areacode=520115"
browser.get(mainUrl)
source=browser.page_source
table_loc = browser.find_element_by_id("ggfwshow")
# 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
table_tr_list = table_loc.find_elements_by_tag_name("tr")
for tr in table_tr_list:
    #print(tr.text)
    #print()
    tds=tr.find_elements_by_tag_name('td')

    print(tds[0].text)
    lens=len(tds)
    print(tds[lens-1].text)
    path="//div[text()='"+tds[0].text+"']/span"
    #browser.findElement(tds[lens-1]).click()
    #time.sleep(5)
    #t=browser.page_source()
    #print(t)
    for td in tds:
        pass
        #print(td.text)
    #tr.find_element_by_class_name('bsqd_btn').click()
    #print(browser.page_source)
#table=browser.find_element_by_id("ggfwshow")
#trList=table.find_element_by_tag_name("tr")
#for i in table:
#    print(i)
#print(f"browser text = {browser.page_source}")



time.sleep(3)               #留出加载时间

links=browser.find_elements_by_xpath("/html/body/div[6]/div/div[1]/table/tbody/span")  #获取到所有a标签，组成一个列表
length=len(links)           #列表的长度，一共有多少个a标签

for i in range(0,length):   #遍历列表的循环，使程序可以逐一点击
    links=browser.find_elements_by_xpath("/html/body/div[6]/div/div[1]/table/tbody/span")    #在每次循环内都重新获取a标签，组成列表
    link=links[i]           #逐一将列表里的a标签赋给link
    #url=link.get_attribute('href')  #提取a标签内的链接，注意这里提取出来的链接是字符串
    #browser.fin(url)         #不能用click，因为click点击字符串没用，直接用浏览器打开网址即可
    time.sleep(1)           #留出加载时间
    title=browser.find_element_by_xpath("//div[@class='articleTitle']").text   #.text的意思是指输出这里的纯文本内容
    print(title)
    content=browser.find_element_by_xpath("//div[@class='TRS_Editor']").text
    print(content)
    print("\n")
    browser.back()           #后退，返回原始页面目录页
    time.sleep(1)           #留出加载时间

print(length)

browser.quit()
