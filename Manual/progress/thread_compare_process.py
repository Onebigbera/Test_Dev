# -*- coding:utf-8 -*-
"""
    分别用3个线程或者进程来完成同一个任务，一般来说，哪个效率更高
        进程快：
            任务数量小于CPU总数，能够并行

        线程：
            由于全局解释器锁GIL的存在，并发（事实上并不能同时执三个任务）

        做多任务的时候，进程快，只使用进程，是否合理?
            不合理，进程虽然执行效率高，但是占用的服务器资源过高
        解决方案: 多进程结合多线程，在多进程中开多线程
"""
import queue
import threading
from multiprocessing import Queue, Manager, Process, Pool
import requests
import time


def count_time(func):
    # 统计函数运行时间的装饰器
    def wrapper(*args, **kwargs):
        print(">>>开始执行>>>")
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("<<<执行结束<<<")
        print("总耗时: {}".format(end_time - start_time))

    return wrapper


# 使用线程来处理任务
def work_thread():
    # 线程中的队列（只能在一个进程中使用，进程中的所有线程共享队列中的资源）
    q1 = queue.Queue()
    for i in range(500):
        q1.put("http://127.0.0.1:8888")
    while q1.qsize() > 0:
        url = q1.get()
        requests.get(url=url)


@count_time
def create_thread():
    print("使用三个线程完成500次请求")
    thread_list = []
    for i in range(3):
        thread_slave = threading.Thread(target=work_thread)
        thread_list.append(thread_slave)
    [thread_slave.start() for thread_slave in thread_list]
    [thread_slave.join() for thread_slave in thread_list]
    print("使用三个线程执行任务完成")


# 使用进程来处理任务
def work_process(q):
    """
    多进程不共享资源，将队列作为参数传入
    :param q:
    :return:
    """
    for i in range(3):
        q.put("http://127.0.0.1:8888")
    while q.qsize() > 0:
        url = q.get()
        requests.get(url=url)


@count_time
def create_process(q):
    print("使用三个进程来完成任务处理")
    process_list = []
    for i in range(3):
        process_slave = Process(target=work_process, args=(q,))
        process_list.append(process_slave)
    [process_slave.start() for process_slave in process_list]
    [process_slave.join() for process_slave in process_list]
    print("使用三个进程执行任务完成")


# ------------------------------------------------------------------------------------------------------
# 使用进程池来处理任务
i = 0


def work(q):
    # 为什么不用判断 q.qsize() > 0 todo:必须要使用判断
    while q.qsize() > 0:
        url = q.get()
        requests.get(url=url)
        global i
        i += 1
    print("该进程执行了{}次".format(i))


def work_1(q):
    # 不使用判断
    url = q.get()
    requests.get(url=url)
    global i
    i += 1
    print("该进程执行了{}次".format(i))


@count_time
def create_process_pool(q):
    # q = Manager().Queue()
    for i in range(500):
        q.put('http://127.0.0.1:8888')
    pool = Pool(3)
    for i in range(3):
        # 进程池中开启三个进程跑任务
        pool.apply_async(work_1, args=(q,))
    # 停止往进程池中添加新的任务
    pool.close()

    # 告诉主进程等待进程池中所有任务都执行完毕后再往下执行
    pool.join()


if __name__ == "__main__":
    # create_thread()

    # q = Queue()
    # create_process(q)

    q = Manager().Queue()
    create_process_pool(q)
