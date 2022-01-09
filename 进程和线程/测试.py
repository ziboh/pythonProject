import multiprocessing
import time


def task():
    time.sleep(1)
    print("当前进程:", multiprocessing.current_process())


if __name__ == '__main__':

       sub_process = multiprocessing.Process(target=task)
       sub_process.start()
       sub_process = multiprocessing.Process(target=task)
       sub_process.start()
       sub_process = multiprocessing.Process(target=task)
       sub_process.start()
       sub_process.terminate()
       sub_process = multiprocessing.Process(target=task)
       sub_process.start()
       exit()