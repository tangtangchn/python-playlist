# encoding: utf-8

import os

# 绝对路径
path = '/Users/user/Desktop/xxx'
files = os.listdir(path)

for f in files:
    if 'MIT' in f and f.endswith('.pdf'):
        print('Found it! ' + f)
