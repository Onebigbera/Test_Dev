# -*- coding:utf-8 -*-
"""
    使用gevent模块创建协程
        协程存在于线程之中，线程默认不会等待协程
    spawn: 开启协程，第一个参数为协程要执行的任务
    join: 让线程等待协程执行
    协程之间切换的条件:
        方法一:gevent.sleep()
        方法二:使用gevent模块中的monkey功能打补丁

    并发情况下:
        先考虑协程，再考虑线程


"""

import gevent
import queue

import requests
from gevent import monkey
import time

monkey.patch_all()

q = queue.Queue()
for i in range(100):
    q.put("http://127.0.0.1:8888")


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


def work():
    while q.qsize() > 0:
        url = q.get()
        requests.get(url)


@count_time
def work_slave():
    w1 = gevent.spawn(work)
    w1.join()


def work1():
    for i in range(10):
        print("Work1---{}".format(i))
        # 只有使用了gevent.sleep()方法，协程之间才会切换上下文；或者打完补丁后也不需要使用gevent.sleep()方法也可以切换
        # gevent.sleep(0.1)
        time.sleep(0.1)


def work2():
    for i in range(10):
        print("Work2---{}".format(i))
        # gevent.sleep(0.1)
        time.sleep(0.1)


def main():
    # 创建两个协程
    g1 = gevent.spawn(work1)
    g2 = gevent.spawn(work2)

    # 让线程等待协程执行,默认不会切换,在work中使用了gevent.sleep()方法协程之间才会切换
    g1.join()
    g2.join()


if __name__ == "__main__":
    # main()

    work_slave()
