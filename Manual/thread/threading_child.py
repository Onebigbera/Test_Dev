# -*- coding:utf-8 -*-
"""
    通过继承Thread类来创建线程
"""
import threading
import requests
import time


class RequestThread(threading.Thread):
    """发送requests请求"""

    def __init__(self, url):
        self.url = url
        # 传入自定义参数时，必须要继承父类的__init__方法,因为父类在__init__时会执行很多内部方法
        super().__init__()

    def run(self):
        """通过run方法来创建线程"""
        res = requests.get(self.url)
        print("线程：{}---返回的状态码为--{}--".format(threading.currentThread(), res.status_code))


if __name__ == "__main__":
    ulr = 'https://www.baidu.com'
    start_time = time.time()
    for i in range(3):
        t = RequestThread(ulr)
        t.start()
    t.join()
    end_time = time.time()
    print("耗时为{}".format(end_time - start_time))
