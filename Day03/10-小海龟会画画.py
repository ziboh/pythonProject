# import turtle
# import time
#
# for i in range(5):
#     turtle.pencolor('red')
#     turtle.forward(100)
# #    turtle.right(144)
#     turtle.left(144)
# time.sleep(10)
n = int(input("请输入同学数量："))
count = 0
for i in range(1,n+1):
    if not (i % 10 == 7 or i % 7 == 0):
        count += 1
else:
    print(f'{n}个同学，报数同学数量为{count}')



