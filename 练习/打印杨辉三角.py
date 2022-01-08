# 将每一行的数字以列表的形式输出
def func(num):
    if num == 1:
        list1 = [1]
        return list1
    elif num == 2:
        list1 = [1,1]
        return list1
    elif num >= 3:
        list2 = func(num - 1)
        list1 = []
        list1.append(1)
        for i in range(1 , num -1):
            a = list2[i] + list2[i-1]
            list1.append(a)
        else:
            list1.append(1)
        return list1


def main(num):
    for i in range(1,num+1):
        a = func(i)
        count = 0
        print(' ' * (num - i)*2,end='')
        for j in a:
            if count + 1 == i:
                print(j,end=' \n')
            elif j < 10:
                print(j,end='   ')
                count += 1
            else:
                print(j,end='  ')
                count += 1

if __name__ == '__main__':
    main(6)