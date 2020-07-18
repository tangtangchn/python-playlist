import json

# 使用json.load()方法取读一个包含JSON对象的文件
# 该方法返回一个字典
with open('./person.json') as f:
    data = json.load(f)

print(data)
