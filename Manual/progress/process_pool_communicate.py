# -*- coding:utf-8 -*-
"""
    使用进程池时进程之间如何通信
        线程池中的进程是当前程序进程的子进程
"""
from multiprocessing import Manager, Pool
import os, time, random


def reader(q):
    print("Reader启动{},父进程为{}".format(os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("Reader从Queue中读取到的消息:{}".format(q.get()))


def writer(q):
    print("Reader启动{},父进程为{}".format(os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        q.put(i)


if __name__ == "__main__":
    print("{} starts".format(os.getpid()))
    q = Manager().Queue()
    po = Pool()
    po.apply_async(writer, (q,))
    time.sleep(1)
    po.apply_async(reader, (q,))
    po.close()
    po.join()
