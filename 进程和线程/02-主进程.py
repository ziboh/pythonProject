import multiprocessing
import time

def task():
    for i in range(10):
        print('任务进行中.....')
        time.sleep(0.2)

if __name__ == '__main__':

    task_process = multiprocessing.Process(target=task)
    # task_process.daemon = True
    task_process.start()

    time.sleep(0.5)
    task_process.terminate()
    print('over')
    exit()
