# -*- coding:utf-8 -*-
"""
    三种队列
        1.先进先出
        2.后入先出
        3.优先级

"""
import queue

# FIFI 先进先出队列
from queue import Queue

# LIFO(后进先出队列)
from queue import LifoQueue

# 优先级别队列
from queue import PriorityQueue


def fifo_queue():
    """先进先出队列"""
    q = queue.Queue(3)
    q.put(1)
    q.put(2)
    q.put(3)
    # 推不进来导致阻塞,默认等待队列
    # q.put(4)

    # 不用等待，有错误直接抛出
    # q.put(4, block=False)

    # 和q.put(22, block=False)效果一致，表示向队列中添加数据不等待
    # q.put_nowait(22)

    # 获取队列中的数据
    print(q.get())
    print(q.get())
    print(q.get())

    # 队列中没有数据时，会导致阻塞
    # print(q.get())

    # 获取数据不等到，有问题直接抛出
    # print(q.get(block=False))
    # 和print(q.get(block=False))效果一致
    print(q.get_nowait())


def fifo_queue_1():
    """先进先出队列"""
    q = queue.Queue(8)
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)
    q.put(6)
    # 获取队列中的任务数
    print(q.qsize())

    # 判断队列是否为空
    print(q.empty())

    # 判断队列是否已满
    print(q.full())

    # 又添加一个任务数
    q.put(12)
    print(q.qsize())

    q.put(3)
    print(q.full())
    print(q.empty())

    q.get(1)
    q.get(2)
    q.get(3)
    q.get(4)
    q.get(5)
    q.get(6)
    q.get(12)
    q.get(3)

    # 将队列中的任务都执行完毕
    # 任务完成调用此方法
    q.task_done()
    q.task_done()
    q.task_done()
    q.task_done()
    q.task_done()
    q.task_done()
    q.task_done()
    q.task_done()

    # 队列中的任务是否执行完毕，如果任务执行完毕，则返回None,否则阻塞
    print(q.join())


def lifo_queue():
    q = LifoQueue()
    q.put(1)
    q.put(2)
    q.put(3)

    print(q.get())
    print(q.get())
    print(q.get())


def priority_queue():
    q = PriorityQueue()

    # 以元组形式传入带等级的对象，第一个表示等级  (priority number, data).
    q.put((11, 'Hello11'))
    q.put((12, 'Hello12'))
    q.put((1, 'Hello1'))
    q.put((15, 'Hello15'))
    q.put((17, 'Hello17'))

    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())


if __name__ == "__main__":
    # fifo_queue()
    # fifo_queue_1()
    # lifo_queue()
    priority_queue()
