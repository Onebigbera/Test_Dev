# -*- coding:utf-8 -*-
"""
    生产者-消费者模式
        思路:
            1.用一个队列来存储商品
            2.创建一个专门负责生产商品的线程，当商品数量小于50时，开始生产商品，每次生产200个商品，每生产完一轮，暂停1秒
            3.创建一个专门消费商品的线程，当商品数量大于10时就开始消费，循环消费，每次消费3个，当商品实例小于10个的时候，暂停2秒
            4.使用一个线程生产商品
            5.使用5个线程生产商品

"""
import time
import queue
from threading import Thread

# 队列本身就实现了锁机制，所以不需要再额外加锁
q = queue.Queue()


class Producer(Thread):
    """生产者"""

    def run(self):
        # 判断队列中的商品数量是否少于50个，少于50就生产500个
        count = 0
        while True:
            if q.qsize() < 50:
                for i in range(500):
                    count += 1
                    goods = "---第{}个商品---".format(count)
                    # 向队列中推入商品
                    q.put(goods)
                    print("生产:", goods)
                    time.sleep(1)


class Customer(Thread):
    """消费者"""

    def run(self):
        while True:
            if q.qsize() > 10:
                for i in range(3):
                    # 调用q.get()方法，从队列中取出对象
                    print("消费:{}".format(q.get()))
                time.sleep(1)


def factory():
    # 创建一个生产者
    p = Producer()
    p.start()

    # 创建5个消费者
    for i in range(5):
        c = Customer()
        c.start()


if __name__ == "__main__":
    factory()
