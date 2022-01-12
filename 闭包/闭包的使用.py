def func_name(name):
    def inner(msg):
        print(name +"在" + msg)
    print(id(inner))
    return inner

if __name__ == '__main__':
    print(id(func_name))
    tom = func_name("tom")
    jerry = func_name("jerry")
    tom("北京")
    jerry("纽约")


