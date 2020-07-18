# JSON
# Javascript对象表示法
# 在Python中，JSON以字符串形式存在
# p = '{"name": "Alice", "languages": ["Python", "Java"]}'


import json

# 使用json.loads()方法解析JSON字符串
# 该方法返回一个字典
person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)

print(person_dict)
print(person_dict['languages'])
