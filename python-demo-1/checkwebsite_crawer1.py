from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
import time
from selenium import webdriver

excel_name = "checkweb.xlsx"
wb = Workbook()
ws1 = wb.active
ws1.title='权力清单'


def get_data(url,post):
    """
    根据请求地址获取数据
    :param url:
    :return:
    """
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    resp = requests.post(url, post, [],
                     verify=False, timeout=10).content
    return resp



import json
def main():
    name_list=[]
    pageIndex=1
    uri='http://zwfw.guizhou.gov.cn/ytbase/system/default.aspx?yt_out_lay=1&YtAction=BaseIEx&ClassName=ZnzwSvr.page.QltAction&YtOpt=GetQltItemAndFolderInfoList&DB_Conn=ZWBSDB'
    import json
    params = {
    'areacode':'520115',
    'type':"",
    'ispage':1,
    'pagesize': 10,
    'page':1,
    'isxz':0
    }
    resp = get_data(uri,params)
    dataList=json.loads(resp)
    link=[]
    for i in dataList["data"]:
        print(i)
        id="http://zwfw.guizhou.gov.cn/bsznindex.do?otheritemcode="+i['Id']+'&orgcode='+i['Org_code']
        link.append(id)
        name_list.append(i['NAME'])
    for i in name_list:
        location = 'A%s'%(name_list.index(i)+1)
        ws1[location]=i
    wb.save(filename=excel_name)
    getDetail(link)

#抓取详情页
def getDetail(link):
    chrome_options = webdriver.ChromeOptions()
    # 使用headless无界面浏览器模式
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # 启动浏览器，获取网页源代码
    browser = webdriver.Chrome(chrome_options=chrome_options)
    for i in link:
        print(i)

        browser.get(i)
        time.sleep(1)
        #bxzn-action1-right-top
        td=browser.find_element_by_class_name('bxzn-action1-right-top')
        print(td.text)
        picname=str(link.index(i))+'.png'
        try:
            br=webdriver.PhantomJS(executable_path=r'E:\server_environment\phantomjs-2.1.1-windows\bin\phantomjs.exe')
            br.maximize_window()
            br.get(i)
            picture_url=br.get_screenshot_as_file('G:\\workspace\\personal_project\\python\\pythonDemo\\python-demo-1\\pic\\'+picname)
            print("%s：截图成功！！！" % picture_url)
            br.close()
        except BaseException as msg:
            print(msg)
        #browser.quit()
    else:
        browser.quit()



if __name__ == '__main__':
    main()

