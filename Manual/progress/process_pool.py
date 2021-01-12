# -*- coding:utf-8 -*-
"""
    进程池
        当我们需要创建额子进程数量不多时，我们可以直接利用multiprocessing动态生成多个进程，但如果是成百甚至上千个目标，手动去创建进程的工作量巨大，此时我们可以利用multiprocessing模块中提供的Pool方法来创建进程池

- 初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool时，如果池还没有满，那么就会创建一个新的进程来执行该请求；但是当池子中的进程数量已经达到了指定的最大值，那么该请求就会等待，直到池子中进程结束，才会用之前的进程来执行新的任务，具体参考示例

Pool 常用方法:

- apply_async(func[,args[,kwds]]): 使用非阻塞方式调用fun（并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程），args为传递給func函数的参数列表，kwds为传递給func的关键字参数列表；
- close(): 关闭Pool,使其不再接收新的任务；
- terminate()：不管任务是否完成，立即终止
- join(): 主进程阻塞，等待子进程的退出，必须在close()或者terminate()之后使用

"""
import random
from multiprocessing import Pool
import os, time


def work(msg):
    start_t = time.time()
    print("{} 开始执行，进程号为{}".format(msg, os.getpid()))
    time.sleep(random.random() * 2)
    stop_t = time.time()
    print(msg, "执行完毕，耗时{}".format(stop_t - start_t))


if __name__ == "__main__":
    # 创建包含3个进程的进程池
    pool = Pool(3)

    # 执行任务10
    for i in range(10):
        pool.apply_async(work, (i,))
    pool.close()
    pool.join()
