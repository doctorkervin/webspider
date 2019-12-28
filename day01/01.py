# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests

'''
first time use requests api
'''


def firstgrep():
    target = 'http://gitbook.cn/'
    req = requests.get(url=target)
    print(req.text)


'''
use requests api to get html div
'''


def grep_div():
    target = 'http://www.biqukan.com/1_1094/'
    req = requests.get(url=target)
    # 设定编码不然乱码
    req.encoding = 'gbk'

    html = req.text
    # print(html)
    div_br = BeautifulSoup(html)
    div = div_br.find_all('div', class_='listmain')
    print(div[0])


'''
抓取笔趣网中可用的a标签的href属性
'''


def grep_a():
    server = 'http://www.biqukan.com/'
    target = 'http://www.biqukan.com/1_1094/'
    req = requests.get(url=target)
    # 设定编码不然乱码
    req.encoding = 'gbk'

    html = req.text
    div_bf = BeautifulSoup(html)
    div = div_bf.find_all('div', class_='listmain')
    a_bf = BeautifulSoup(str(div[0]))
    a = a_bf.find_all('a')
    for each in a:
        print(each.string, server + each.get('href'))


# 网络爬虫的第一步就是根据URL，获取网页的HTML信息。在Python3中，可以使用urllib.request和requests进行网页爬取。
if __name__ == '__main__':
    # firstgrep()
    # grep_div()
    grep_a()
