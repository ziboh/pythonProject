# # 打印正方形
i = 0
while i < 5:
    j = 0
    while j < 5:
        if j == 4:
            print('*', end='')
        else:
            print('*', end='  ')
        j = j + 1
    print('')
    i += 1


print('-' * 30)
# 打印直角三角形
i = 0
while i < 5:
    j = 0
    while j <= i:
        if j == i:
            print('*', end='')
        else:
            print('*', end='  ')
        j = j + 1
    j = 0
    i += 1
    print('')
