# -*- coding:utf-8 -*-
"""
    greenlet模块对Python协程进行了封装，更方便使用
"""
from greenlet import greenlet
import time


def test1():
    for i in range(10):
        print(i)
        print("切换到g2")
        g2.switch()
        time.sleep(0.1)


def test2():
    for i in range(10, 20):
        print(i)
        print("切换到g1")
        g1.switch()
        time.sleep(0.1)


g1 = greenlet(test1)
g2 = greenlet(test2)

g1.switch()


# 理解对比以下
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