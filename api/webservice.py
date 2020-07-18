# -*- encoding: utf-8 -*-
__author__ = 'tang'


# 导入suds.client模块下的Client类
# 用于调用WebService接口
from suds.client import Client
from flask import jsonify


wsdl_url = 'http://xx.xxx.xxx.xxx/IFWebService/xxxxxx.asmx?wsdl'


def get_xxx_api():
    # 创建一个webservice接口对象
    client = Client(wsdl_url)
    # 调用这个接口下的GetXXX方法
    client.service.GetXXX()
    # 保存请求报文，因为返回的是一个实例，所以要转为字符串
    # req = str(client.last_sent())
    # 保存返回报文，返回的也是一个实例
    response = str(client.last_received())
    res = dict()
    res['response'] = response
    # jsonify的处理对象必须是字典dict
    resp_json = jsonify(res)
    return resp_json
