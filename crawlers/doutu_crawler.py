# encoding: utf-8

# 请求网络数据
# requests
# pip install requests

# 解析html文档，过滤数据
# beautifulsoup4
# pip install bs4

# 下载url对应的资源
# urllib - Python自带库，无需安装

import requests
from bs4 import BeautifulSoup
import urllib
import os

# 大写表示全局变量
BASE_PAGE_URL = 'https://www.doutula.com/photo/list/?page='
PAGE_URL_LIST = []
for x in range(1, 870):
    url = BASE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)
    # print url


def download_img(img_url):
    split_list = img_url.split('/')
    filename = split_list.pop()
    path = os.path.join('images', filename)
    urllib.urlretrieve(url, filename=path)


def get_page(page_url):
    response = requests.get(page_url)
    content = response.content
    # print content
    soup = BeautifulSoup(content, "html.parser")
    # soup = BeautifulSoup(content, 'lxml')  # 使用【lxml引擎】来解析，需安装
    # 查找img标签，标签有多个属性；过滤条件：img标签的class属性
    img_list = soup.find_all('img', attrs={'class': 'img-responsive lazy image_dta'})
    for img in img_list:
        # print img
        # print '-' * 30
        img_url = img['data-original']  # 获取标签中的属性：操作字典
        download_img(img_url)


def main():
    for page_url in PAGE_URL_LIST:
        get_page(page_url)


if __name__ == "__main__":
    main()
