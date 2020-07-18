import json
import time
import requests
from bs4 import BeautifulSoup

# 获取所有标签
url = 'https://movie.douban.com/j/search_tags?type=movie'
req = requests.get(url)
result = json.loads(req.content.decode('utf-8'))
tags = result['tags']

'''
print(len(tags))

for tag in tags:
    print(tag)
'''

# 列表存储电影的基本信息
movies = []

# 处理每个tag
for tag in tags:
    limit = 0
    # 不断请求，直到返回结果为空
    while 1:
        # 拼接需要请求的链接，包括标签和开始编号
        url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' + tag +\
              '&sort=recommend&page_limit=20&page_start=' + str(limit)
        print(url)

        req = requests.get(url)
        result = json.loads(req.content.decode('utf-8'))

        result = result['subjects']

        # 返回结果为空 -> 说明已经没有数据
        # 完成一个标签的处理，退出循环
        if len(result) == 0:
            break

        limit += 20

        for item in result:
            movies.append(item)

        # for testing
        break

    # for testing
    break

# 请求每部电影的详情页面
for m in range(len(movies)):
    movie = movies[m]
    url = movie['url']
    req = requests.get(url)
    result = req.content

    # 使用BeautifulSoup解析html
    html = BeautifulSoup(result, 'html5lib')

    # for testing
    '''
    title = html.select('h1')[0]
    title = title.select('span')[0]
    title = title.get_text()
    print(title)
    '''

    # 提取电影简介
    # 捕捉异常，有的电影详情页中没有简介
    try:
        # 尝试提取电影简介
        description = html.find_all("span", attrs={"property": "v:summary"})[0].get_text()
    except:
        # 没有提取到简介，则简介为空
        movies[m]['description'] = ''
    else:
        # 将新获取的字段填入movies
        movies[m]['description'] = description
    finally:
        pass

    # 适当休息，避免请求频发被禁止
    # 报403 Forbidden错误
    time.sleep(0.5)

fw = open('douban_movies.txt', 'w')

# 写入一行表头，用于说明每个字段的意义
fw.write('title^rate^url^cover^id^description\n')

for item in movies:
    # 用^作为分隔符
    # 为了避免中文里可能包含逗号发生冲突
    fw.write(item['title'] + '^' + item['rate'] + '^' + item['url'] + '^' + item['cover']
             + '^' + item['id'] + '^' + item['description'] + '\n')
fw.close()
