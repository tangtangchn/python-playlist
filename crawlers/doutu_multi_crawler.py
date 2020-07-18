# encoding: utf-8
# 参考【多线程--生产者/消费者模式】进行改造

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
import threading

# 大写表示全局变量
BASE_PAGE_URL = 'https://www.doutula.com/photo/list/?page='
PAGE_URL_LIST = []  # 页面的url列表
IMG_URL_LIST = []  # 表情图片的url列表

# 全局线程锁
g_lock = threading.Lock()

for x in range(1, 870):
    url = BASE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)
    # print url


# ------------------------多线程改造 BEGIN------------------------
# 生产者--爬取每个页面中图片的url
def producer():
    # 因为是多线程，所以不用for循坏来处理
    while True:
        g_lock.acquire()  # 加锁
        if len(PAGE_URL_LIST) == 0:
            g_lock.release()  # 解锁
            # 跳出循环
            break
        else:
            page_url = PAGE_URL_LIST.pop()  # 取出最后一个数据
        g_lock.release()  # 解锁
        response = requests.get(page_url)
        content = response.content
        # print content
        soup = BeautifulSoup(content, "html.parser")
        # soup = BeautifulSoup(content, 'lxml')  # 使用【lxml引擎】来解析，需安装
        # 查找img标签，标签有多个属性；过滤条件：img标签的class属性
        img_list = soup.find_all('img', attrs={'class': 'img-responsive lazy image_dta'})
        g_lock.acquire()  # 加锁
        for img in img_list:
            # print img
            # print '-' * 30
            img_url = img['data-original']  # 获取标签中的属性：操作字典
            IMG_URL_LIST.append(img_url)
        g_lock.release()  # 解锁


#  消费者--下载图片
def consumer():
    while True:
        g_lock.acquire()  # 加锁
        if len(IMG_URL_LIST) == 0:
            g_lock.release()  # 解锁
            continue
        else:
            img_url = IMG_URL_LIST.pop()
            g_lock.release()  # 解锁
            split_list = img_url.split('/')
            filename = split_list.pop()
            path = os.path.join('images', filename)
            urllib.urlretrieve(img_url, filename=path)
# ------------------------多线程改造 END--------------------------


def main():
    # 创建3个线程来作为生产者，去爬取图片的url
    for x in range(3):
        thread = threading.Thread(target=producer)
        thread.start()

    # 创建5个线程来作为消费者，去下载图片至本地
    for x in range(5):
        thread = threading.Thread(target=consumer)
        thread.start()


if __name__ == "__main__":
    main()
