# 打印一百遍“老婆大人，我错了”

# i = 0
# while i < 100:
#     i += 1
#     print(f'{i}，老婆大人，我错了')
"""
打印九九乘法表
"""

a = 1
b = 1

while a < 10:
    while b <= a:
        if b == a:
            print(f"{b} × {a}= {a * b}", end='')
        else:
            print(f"{b} × {a}= {a * b}", end='\t')
        b += 1
    a = a + 1
    b = 1
    print('')
print('周伯华')
# print('-' * 10)
# print('\n'*2)
# # 一到一百求和
# i = 1
# result = 0
# while i <= 100:
#     result =result + i
#     i += 1
# print(f'一加到一百的和为：{result}')
#
#
# # 求一到一百所有偶数求和
# print('-' * 10)
# print('\n'*2)
#
# i = 1
# result = 0
# while i <= 100:
#     if i % 2 == 0:
#         result =result + i
#         print(i)
#     i += 1
# print(f'一加到一百的和为：{result}')



