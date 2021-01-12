# -*- coding:utf-8 -*-
"""
    多进程之间的通讯
        因为多进程之间全局变量不共享，如果使用全局变量会导致变量各自创建自己的变量地址，导致其变量具有不唯一性，因此将Queue作为参数出入进去，确保不同进程之间使用的为同一个队列
"""
from multiprocessing import Process, Queue
import requests


def foo(q):
    while True:
        if q.qsize() > 0:
            # 从队列中拿出任务对象
            url = q.get()
            requests.get(url)
            print("Work1正在执行任务---")


def foo2(q):
    while True:
        if q.qsize() > 0:
            url = q.get()
            requests.get(url)
            print("Work2正在执行任务---")


if __name__ == "__main__":
    q = Queue()
    # 创建一个队列，添加十个任务
    for i in range(6):
        q.put('http://127.0.0.1:8888')
    p1 = Process(target=foo, args=(q,))
    p2 = Process(target=foo2, args=(q,))
    p1.start()
    p2.start()
