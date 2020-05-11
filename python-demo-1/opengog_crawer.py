from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
excel_name = "opengog.xlsx"
wb = Workbook()
ws1 = wb.active
ws1.title='数据目录'


def get_data(url):
    """
    根据请求地址获取数据
    :param url:
    :return:
    """
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    html = requests.get(url, headers=header).content
    return html


def get_name(data):
    """
    遍历列表获取名称
    :param data:
    :return:
    """
    name = []
    for i in data:
        name.append(i['appName'])
    else:
        return name

import json
def main():
    name_list=[]
    pageIndex=1
    uri='https://open.gog.cn/appz/apps/selPageList?limit=5&'
    url = uri+'page='+str(pageIndex)+'&userId='
    data = get_data(url)
    dataList=json.loads(data)
    pageNum=dataList['data']['total']//5
    rest=dataList['data']['total']%5
    #取余下数据
    if rest>0:
        pageNum=pageNum+1
    #获取名称
    name=get_name(dataList['data']['data'])
    name_list = name_list + name
    pageIndex=pageIndex+1
    #分页查询
    while pageIndex<pageNum:
        pageIndex=pageIndex+1
        url = uri+'page='+str(pageIndex)+'&userId='
        data = get_data(url)
        dataList=json.loads(data)
        name=get_name(dataList['data']['data'])
        name_list = name_list + name

    for i in name_list:
        location = 'A%s'%(name_list.index(i)+1)
        print(i)
        print(location)
        ws1[location]=i
    wb.save(filename=excel_name)


if __name__ == '__main__':
    main()

