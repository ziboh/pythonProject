# import  random
# c_num = random.randint(1,10)
# i = 1
# while i < 4:
#     p_num = int(input("请输入1~10间的数字："))
#     if p_num == c_num:
#         print('恭喜你，猜对了。')
#
#         break
#     elif p_num > c_num:
#         print('猜大了')
#     else:
#         print('猜小了')
#     i += 1
# print(f'随机数为{c_num}')


# 外层循环计数器
j = 1
# 外层循环条件
while j <= 3:
    i = 1
    # 编写循环条件
    while i <= 5:
        if i == 4:
            print('吃饱了，实在吃不下了...............')
            break

        print(f'正在吃第{i}个苹果')
        # 更新计数器
        i += 1
    j += 1      # 更改外层计数器
    print('-'*30)
