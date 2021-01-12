# -*- coding:utf-8 -*-
"""
    创建生成器的两种方式:
        1.通过生成器表达式
        2.通过关键字yield
"""
import time


def work1():
    for i in range(10):
        print("Work1---{}".format(i))
        time.sleep(0.1)
        yield


def work2():
    for i in range(10):
        print("Work2---{}".format(i))
        time.sleep(0.1)
        yield


def generate_work():
    g1 = work1()
    g2 = work2()
    while True:
        try:
            next(g1)
            next(g2)
        except StopIteration:
            break


if __name__ == "__main__":
    # work1()
    # work2()

    generate_work()
"""
    协程:微线程
    协程的本质是单任务，协程依赖于线程
    协程相对于线程来讲，其占用的资源更少（几乎不占用什么资源）
"""