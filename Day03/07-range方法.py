# for循环求1~100的和
# result = 0
# for i in range(1,101):
#     result = i + result
# print(f'1~100的和为{result}')


# 打印是遇到e终止打印
user_name = 'sharezhou'
for i in user_name:
    if i == "h":
        continue

    print(i,end="")
