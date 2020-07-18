# pip install bs4
# 做网页分析

# pip install requests
# 做网络请求

# pip install lxml
# BeautifulSoup基于lxml这个解析引擎

# pip install pyecharts
# 可视化工具


from bs4 import BeautifulSoup
import requests
import time
from pyecharts import Bar


# 全局字典
temperature_dict = {}


def get_temperature(url):

    ##################################
    # step 1: 获取中国天气网数据
    # requests -> 将网页数据全部抓取下来
    ##################################

    headers = {
        # 伪装User-Agent(浏览器)
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X)\
                       AppleWebKit/601.1.46 (KHTML, like Gecko)\
                       Version/9.0 Mobile/13B143 Safari/601.1',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'http://www.weather.com.cn/textFC/hb.shtml',
        'Host': 'www.weather.com.cn'
    }

    # get/post
    req = requests.get(url, headers=headers)

    # print(req.content)
    content = req.content

    ##################################
    # step 2: 获取页面中的省份
    # bs4 -> 将抓取下来的数据进行过滤
    ##################################

    soup = BeautifulSoup(content, 'lxml')
    # find -> 返回的不是列表
    conMidtab = soup.find('div', class_='conMidtab')
    # print(conMidtab)

    # find_all -> 返回的是列表
    conMidtab2_list = conMidtab.find_all('div', class_='conMidtab2')

    for x in conMidtab2_list:
        # print(x)
        # 省份或直辖市都存放在表格中
        # 过滤掉前两个无用的tr标签
        tr_list = x.find_all('tr')[2:]

        for index, tr in enumerate(tr_list):
            # (过滤掉前两个tr标签后)
            # 在第0个tr标签中，城市名和省份是放在一起的
            if index == 0:
                td_list = tr.find_all('td')
                # 获取省份
                # .text -> 获取文本 e.g. 北京
                # replace -> 去除多余的换行
                province = td_list[0].text.replace('\n', '')

                ##################################
                # step 3: 获取页面中的城市
                ##################################

                city = td_list[1].text.replace('\n', '')

                ##################################
                # step 4: 获取城市的最低气温
                ##################################

                low = td_list[7].text.replace('\n', '')

            # 在非第0个tr标签中，只存放城市名
            else:
                td_list = tr.find_all('td')
                # 获取页面中的城市
                city = td_list[0].text.replace('\n', '')
                # 获取城市的最低气温
                low = td_list[6].text.replace('\n', '')

            # 将数据保存在字典里
            temperature_dict[province + city] = low

            # print(province + ' - ' + city + ' - ' + low)


##################################
# step 5: 获取所有城市的最低气温
##################################

def main():
    # 华北 | 东北 | 华东 | 华中 | 华南 | 西北 | 西南 | 港澳台
    urls = ['http://www.weather.com.cn/textFC/hb.shtml',
            'http://www.weather.com.cn/textFC/db.shtml',
            'http://www.weather.com.cn/textFC/hd.shtml',
            'http://www.weather.com.cn/textFC/hz.shtml',
            'http://www.weather.com.cn/textFC/hn.shtml',
            'http://www.weather.com.cn/textFC/xb.shtml',
            'http://www.weather.com.cn/textFC/xn.shtml']

    for url in urls:
        get_temperature(url)
        # 避免请求频发被禁止
        time.sleep(2)

    ##################################
    # step 6: 最低气温数据可视化
    ##################################

    # 字典排序
    # lambda -> 生成一个临时函数
    # d -> 字典的每一对键值对
    # d[0] -> key
    # d[1] -> value
    sorted_temperature_list = sorted(temperature_dict.items(), key=lambda d: d[1])

    # 获取前二十个气温最低的城市
    top20_temperature_list = sorted_temperature_list[0:20]

    top20_city_list = []
    top20_low_list = []

    for city, low in top20_temperature_list:
        top20_city_list.append(city)
        top20_low_list.append(low)

    # 柱状图的标题 & 副标题
    bar = Bar('全国最低温度排名', '数据来源于中国天气网')

    # 添加图表的数据 & 设置各种配置项
    bar.add('最低温度', top20_city_list, top20_low_list)

    # 打印输出图表的所有配置项
    bar.show_config()

    # 默认在根目录下生成一个render.html文件
    # 支持path参数，设置文件保存位置
    # e.g. render(r'e:\first_chart.html)
    bar.render()


# 运行主函数
if __name__ == '__main__':
    main()
