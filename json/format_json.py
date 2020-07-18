import json

# 使用Python完美输出JSON
person_string = '{"name": "Bob", "languages": ["English", "French"], "numbers": [8, 1.6, null]}'

# get dictionary
person_dict = json.loads(person_string)

# pretty print json string back
# indent的默认值是None，sort_keys的默认值是False
print(json.dumps(person_dict, indent=4, sort_keys=True))  # 4个空格缩进，键值按升序排序
