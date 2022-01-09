import threading
import time
# 定义全局变量
g_num = 0

lock = threading.Lock()
# 循环一次给全局变量加1
def sum_num1():
    print('1111')
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1

    print("sum1:", g_num)
    lock.release()

# 循环一次给全局变量加1
def sum_num2():
    print('1111')
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    print("sum2:", g_num)
    lock.release()

if __name__ == '__main__':
    # 创建两个线程
    first_thread = threading.Thread(target=sum_num1)
    second_thread = threading.Thread(target=sum_num2)

    # 启动线程
    first_thread.start()
    # 启动线程
    # first_thread.join()
    second_thread.start()