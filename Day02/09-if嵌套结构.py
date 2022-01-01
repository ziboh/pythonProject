'''
if嵌套结构案例
'''
money = 1
seat = 0
if money == 1:
    print('有钱，可以上车。')
    if seat == 1:
        print('有座位，可以坐下。')
    else:
        print('没有位置，只能站着回家。')
else:
    print('没钱，不能上车。')