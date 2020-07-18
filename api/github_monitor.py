# encoding: utf-8

# RESTFUL api
# https://api.github.com/repos/vinta/awesome-python

# web page
# https://github.com/vinta/awesome-python

# 监测Github项目更新并自动打开网页

import requests
import webbrowser
import time

api = 'https://api.github.com/repos/channelcat/sanic'
web_page = 'https://github.com/vinta/awesome-python'

last_update = None
all_info = requests.get(api).json()  # 字典
cur_update = all_info['updated_at']  # 数据更新时间
print cur_update

while True:
    if not last_update:
        last_update = cur_update

    if last_update < cur_update:
        webbrowser.open(web_page)
    time.sleep(600)
