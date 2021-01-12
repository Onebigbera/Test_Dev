# -*- coding:utf-8 -*-
"""
    利用元类创建类需要传入三个参数
        1.类名称  str
        2.继承的父类  tuple
        3.方法和属性  dict

    通过使用元类和描述器来模拟实现ORM模型
"""


# 使用type类来创建新的类
def func(self):
    print("---这个是self---")


Test = type("Test", (object,), {'attr': 100, "__attr2": 3000, 'function': func})


# 一般方法创建类
class Test1:
    attr = 100
    __attr2 = 3000


if __name__ == "__main__":
    print(Test)
    T = Test()
    # 将其属性和方法封装在字典中，通过此方式进行调用
    print(T.attr)
    T.function()
    print(Test.__dict__)
    print(Test1)
