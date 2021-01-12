# -*- coding:utf-8 -*-
"""
    多进程
        Python中的多线程本质上是单线程，不能最大化利用CPU核数，而使用多进程可以做到最大化利用CPU核数
        多进程并不会共享全局变量
"""

from multiprocessing import Process

a = 100


def func1():
    global a
    a += 1
    print("进程一中的a为{}".format(a))


def func2():
    global a
    a += 2
    print("进程一中的a为{}".format(a))


def func3():
    global a
    a += 3
    print("进程一中的a为{}".format(a))


def func4():
    global a
    a += 4
    print("进程一中的a为{}".format(a))


if __name__ == "__main__":
    p1 = Process(target=func1)
    p2 = Process(target=func2)
    p3 = Process(target=func3)
    p4 = Process(target=func4)
    [p.start() for p in [p1, p2, p3, p4]]
