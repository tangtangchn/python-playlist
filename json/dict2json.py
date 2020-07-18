import json

# 使用json.dumps()方法将字典转换成JSON字符串
person_dict = {'name': 'Bob', 'languages': ['English', 'French'], 'age': 16, 'children': None}
person_json = json.dumps(person_dict)

print(person_json)

# ---------------------------------------
#
#      Python        JSON Equivalent
#
#       dict            object
#    list, tuple        array
#       str             string
#     int, float        number
#       True            true
#       False           false
#       None            null
#
# ---------------------------------------
