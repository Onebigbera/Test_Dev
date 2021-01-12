# -*- coding:utf-8 -*-
"""
    需求:
    10000个请求，开启两个进程，进程中开启4个线程，线程中开启5个协程来处理
    todo:important
"""
# import monkey
# monkey.patch()
import time
from threading import Thread
from multiprocessing import Process, Queue
import gevent
import requests


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


def thread_work(q, tname):
    """
    每个线程执行任务函数，在该线程中开启5个协程
    :param q:
    :param tname:
    :return:
    """
    g_list = []
    for i in range(5):
        gname = "{}-cor-{}".format(tname, i)
        print("创建协程-----{}".format(gname))
        # 创建协程
        g = gevent.spawn(gevent_work, q, gname)
        g_list.append(g)
    # 等待列表中所有的协程结束
    gevent.joinall(g_list)


def gevent_work(q, gname):
    """

    :param q:
    :param gname:
    :return:
    """
    count = 0
    while not q.empty():
        # 使用等待时间，避免资源竞争导致堵塞,但是还是会由于没法取到资源而抛出raise Empty_queue.Empty错误  就是因为没有取到数据
        url = q.get(timeout=0.01)
        requests.get(url)
        # 设置0.001方便多个协程进程切换 协程必须遇到 gevent.sleep()方法才会进行切换
        gevent.sleep(0.001)
        count += 1
    print("--协程{}执行了{}个任务".format(gname, count))


def process_work(q, pname):
    """
        每个进程执行的任务函数，在该进程中开启3个线程
        创建三个线程
        :param q: 进程之间的通讯的任务队列
        :param pname:进程名称
        :return:
        """
    # 猴子补丁建议使用在单进程中,不建议在此处使用
    # monkey.patch_all()

    thread_list = []
    for i in range(5):
        tname = '{}-th-{}'.format(pname, i)
        print("创建线程{}".format(tname))
        t = Thread(target=thread_work, args=(q, tname))
        thread_list.append(t)
        t.start()
    # 让主线程堵塞，等待子线程
    for t in thread_list:
        t.join()


@count_time
def main():
    # 创建1000个请求的队列
    q = Queue()
    for i in range(10000):
        q.put("http://127.0.0.1:8888")
    # 开启两个进程处理
    print("队列创建完成，数量为{}".format(q.qsize()))

    pro_list = []
    for i in range(2):
        pname = 'Pro-{}'.format(i)
        print("创建进程{}".format(pname))
        p = Process(target=process_work, args=(q, pname))
        p.start()
        pro_list.append(p)
    # 让主进程等待子进程执行结束后再往下执行
    for p in pro_list:
        p.join()


if __name__ == "__main__":
    main()
