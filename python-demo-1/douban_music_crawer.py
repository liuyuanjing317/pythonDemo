from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
excel_name = "douban_music.xlsx"
wb = Workbook()
ws1 = wb.active
ws1.title='书籍'

#目前只能爬静态页面，动态加载的数据获取不到
def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    html = requests.get(url, headers=header).content
    return html


def get_con(html):
    soup = BeautifulSoup(html,'html.parser')
    print(soup)
    book_list = soup.find('div', attrs={'class': 'mod'})
    print(book_list)
    book_list = book_list.find('ul', attrs={'class': 'col5'})
    name = []
    for i in book_list.find_all('li'):
        book_name = i.find('div', attrs={'class': 'intro'})
        m = list(book_name.find('a').stripped_strings)
        if len(m)>1:
            x = m[0]+m[1]
        else:
            x = m[0]
        #print(x)
        name.append(x)
    else:
        return name, None


def main():
    url = 'https://music.douban.com/chart'
    name_list=[]
    while url:
        html = get_html(url)
        name, url = get_con(html)
        name_list = name_list + name
    for i in name_list:
        location = 'A%s'%(name_list.index(i)+1)
        print(i)
        print(location)
        ws1[location]=i
    wb.save(filename=excel_name)


if __name__ == '__main__':
    main()

