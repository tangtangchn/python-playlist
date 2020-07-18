# -*- coding: utf-8 -*-


import pandas as pd
from datetime import datetime


# 计时开始
start = datetime.now()

# 把excel内容读取为DataFrame对象
# sheetname=0表示第一个sheet
df = pd.read_excel('明细.xlsx', sheet_name=0)

# 行数
# 列名这一行不计数
# print('行数为：', len(df.index))
# 列名
# print('列名为：', df.columns)
# 保留50000行数据
df.drop(df.index[50000:], inplace=True)

# 根据列名遍历行
for i in range(len(df.index)):
    if df.loc[df.index[i], '费用发生地公司'] == 66 or df.loc[df.index[i], '费用发生地公司'] == 88:
        df.loc[df.index[i], '总部或分公司'] = '总部'
    else:
        df.loc[df.index[i], '总部或分公司'] = '分公司'
    # print(df.loc[df.index[i], ['费用发生地公司', '总部或分公司']])
    i += 1

# 导出数据
writer = pd.ExcelWriter('明细_Output.xlsx')
df.to_excel(writer)
writer.save()

# 计时结束
end = datetime.now()

# 耗时
processtime = (end - start) / 60
print('耗时：', processtime, 'minutes')
