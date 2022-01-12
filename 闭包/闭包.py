# 在函数嵌套(函数里面再定义函数)的前提下
# 内部函数使用了外部函数的变量(还包括外部函数的参数)
# 外部函数返回了内部函数

def func_out():
    num1 = 10
    def func_inner(b):
        result = num1 + b
        print(f"结果：{result}")


    return func_inner


if __name__ == '__main__':
    new_func = func_out()
    new_func(210)