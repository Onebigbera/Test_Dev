# -*- coding:utf-8 -*-
"""
    多线程全局变量的问题
        授课的时候讲的会因为线程切换导致全局变量的值被修改导致重新赋值改变 导致计算的值错误
            我的多线程使用全局变量是安全的！！！线程非安全
"""
import threading
import time

a = [100]

# 创建锁
lock = threading.Lock()


def fun1():
    global a
    for i in range(1000000):
        # 上锁
        lock.acquire()
        a[0] += 1
        # 修改完成 释放锁
        lock.release()
    print("线程一修改完a:{}".format(a))


def fun2():
    global a
    for i in range(4):
        lock.acquire()
        a[0] += 1
        lock.release()
    print("线程二修改完a:{}".format(1000000))


if __name__ == "__main__":
    t1 = threading.Thread(target=fun1, name="th_1")
    t2 = threading.Thread(target=fun1, name="th_2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(a)
