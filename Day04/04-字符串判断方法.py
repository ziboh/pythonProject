# str1 = 'Python Program'
# print(str1.startswith('p'))
# str2 = 'shia.jpg'
# if str2.endswith('.jpg' or '.png' or 'tif'):
#     print('这是张图片。')
# else:
#     print('图片格式错误！')
#
# print(str1.replace(' ','').isalpha())
# print(len(str1))

# for i in range(1,101):
#     password = input('请输入6位数密码：')
#     if len(password) == 6 and password.isdigit():
#         print('密码输入成功，正在验证.......')
#         break
#     else:
#         print('密码格式错误，请输入6位纯数字密码！')
str1 = '   d'
print(str1.isalpha())
print(str1.isalnum())
print(str1.isspace())
