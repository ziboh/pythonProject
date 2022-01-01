# 输入三角形三遍长度
a = float(input('请输入三角形第一条边的长度a:'))
b = float(input('请输入三角形第二条边的长度b:'))
c = float(input('请输入三角形第三条边的长度c:'))
# 根据三角形任意两边之和大于第三边判断
if a + b > c or a + c >b or b + c > a :
    print("该三角形为合法三角形")
else:
    print("这三条边不能组成合法三角形")

# import random
#
#
# a = random.randint(1,99)
# print(a)