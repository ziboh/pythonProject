# 初始化计数器
i = 1
# 编写循环条件
while i <= 5:
    if i == 3:
        print('苹果坏了，这个吃不了')
        i = i + 1
        continue

    print(f'正在吃第{i}个苹果')
# 更新计数器
    i += 1

print('-' *20,end='\n'*2)
# 初始化计数器0]
i = 1
# 编写循环条件
while i <= 5:
    if i == 4:
        print('吃饱了，实在吃不下了...............')
        break

    print(f'正在吃第{i}个苹果')
# 更新计数器
    i += 1
    print('')
