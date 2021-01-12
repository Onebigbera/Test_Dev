# -*- coding:utf-8 -*-
"""
coroutines:协程 协程，又称微线程，纤程。英文名Coroutine。一句话说明什么是线程：协程是一种用户态的轻量级线程。
协程存在的意义：对于多线程应用，CPU通过切片的方式来切换线程间的执行，线程切换时需要耗时（保存状态，下次继续）。协程，则只使用一个线程，在一个线程中规定某个代码块执行顺序。

适用场景：其实在其他语言中，协程的其实是意义不大的多线程即可已解决I/O的问题，但是在python因为他有GIL（Global Interpreter Lock 全局解释器锁 ）在同一时间只有一个线程在工作，所以：如果一个线程里面I/O操作特别多，协程就比较适用;
协程是一把双刃剑；用好了就像线程一样提高运行效率；没运用好也会降低程序运行效率

"""
import time
import asyncio


# 手撸一个计时的装饰器函数 内部函数调用外部函数参数func(func(*args, **kwargs)) 将*args 和 **kwargs 应用进来 很重要
def time_it(func):
    # 存在内部函数
    def __wrapper(*args, **kwargs):
        begin_time = time.time()
        # 内部函数调用外部函数参数func(函数对象)
        res = func(*args, **kwargs)
        end_time = time.time()
        use_time = end_time - begin_time
        print(f'{func.__name__} use time :{use_time}')
        return res

    # 外部函数返回内部函数对象
    return __wrapper


# 用@asyncio.coroutine装饰器来开启协程
@asyncio.coroutine
def task1():
    # 让程序睡眠两秒 是和task2串联执行
    # yield time.sleep(2)
    # 让程序睡眠两秒 异步执行 即为和task2同步执行 并行执行
    yield from asyncio.sleep(2)
    print(f'hello, this is task1')


@asyncio.coroutine
def task2():
    # 同步串联执行
    # yield time.sleep(2)
    # 异步并行执行
    yield from asyncio.sleep(3)
    print(f'hello, this is task2')


tasks = [task1(), task2()]


@time_it
def test_task_asyncio():
    # 构建异步事件
    loop = asyncio.get_event_loop()
    # 运行异步事件循环直至结束
    loop.run_until_complete(asyncio.wait(tasks))
    # 循环结束(关闭)
    loop.close()


if __name__ == '__main__':
    test_task_asyncio()
