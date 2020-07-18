import json

# 使用json.dump()将person_dict转换为一个JSON字符串
# 该字符串将保存在person.txt文件中
person_dict = {'name': 'Bob', 'languages': ['English', 'French'], 'age': 16, 'married': False}

with open('person.txt', 'w') as json_file:
    json.dump(person_dict, json_file)
