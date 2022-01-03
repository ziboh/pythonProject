# 字典的增操作
dict1 = {}
dict1['name'] = '周伯华'
dict1['age'] = 21
dict1['address'] = '湖南'
print(dict1)

# 字典的删操作
# del dict1['address']
# dict1.clear()
print(dict1)

# 字典的查询操作
print(dict1['name'])
dict1.get('name')
print(dict1['name'])
# print(type(dict1.keys()))
# print(type(dict1))
print(dict1.values())
print(dict1.keys())

print(dict1.items())
for i,j in dict1.items():
    print(f'{i}:{j}')
for i in dict1.items():
    print(type(i))