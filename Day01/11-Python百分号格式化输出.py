name = '周伯华'
school = '湖南工业大学'
age = 21
# print('我的名字叫%s，毕业于%s，今年%5d岁。'%(name,school,age))

# print('我的名字叫{}，毕业于{},今年{}岁。'.format(name,school,age))
# print(f'我的名字叫{name}，毕业于{school},今年{age}岁。')
jianjie = f'我的名字叫{name}\n毕业于{school}\n今年{age}岁'
print(type(jianjie))
print(jianjie)
title = "大白菜"
price = 3.999999999
# 格式化输出”大白菜只要3.5元一斤“
print('%s只要%d一斤。' % (title,price))

num=1
# 格式化输出”姓名：周伯华，学号：000001“

print('姓名：%s，学号：%06d'%(name,num))

print('*\t*\t*')

print('*',end=' ')
print('*',end=' ')
print('*',end=' ')


password = input('请输入密码：')    # <class 'str'>
print(f'你输入的银行卡密码为：{password}')
print(type(password))