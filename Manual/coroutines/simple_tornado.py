"""
    tornado  用Python写的web框架，处理并发问题效率较高 采用协程处理并发 非阻塞式异步服务器  支持并发量很高；但是一旦程序阻塞，将会导致整个程序崩溃
    简单模拟tornado模块 基本运行原理
"""
import tornado
import tornado.ioloop
import tornado.web
import json


class MainHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        """
        GET 方法
        :param args: 接受多个参数
        :param kwargs: 接受多个关键字参数
        """
        self.write('hello, this is main handler!')


# 继承tornado.web.RequestHandler类
class AddHandler(tornado.web.RequestHandler):

    def get(self, x, y):
        sum = int(x) + int(y)
        # dict(**kwargs) 构建字典的方法
        data = dict(
            code=200,  # 业务状态吗
            msg='ok',  # 业务描述信息
            data=sum,  # 业务返回数据
        )
        self.write(json.dumps(data))


def main():
    PORT = 8888
    url_router = [
        (r'/', MainHandler),

        (r'/add/(\d+)/(\d+)/', AddHandler),
    ]
    application = tornado.web.Application(url_router)
    application.listen(PORT)
    print(f'the server with port:{PORT} is running')
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()

"""
  构建字典的方法之一:
  eg:
b = dict(a=3, b=4)
print(type(b))
print(b)
"""

""" 
    返回json数据
    浏览器上输入URL:http://127.0.0.1:8888
    浏览器上输入URL:http://127.0.0.1:8888/add/2/3/
"""
