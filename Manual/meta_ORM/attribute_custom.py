# -*- coding:utf-8 -*-
"""
    自定义属性访问
"""


class Test:
    """
    使用__getattribute__和__getattr__可以自定义属性查找之前和查找的属性不存在的时候自定义的操作
    """

    def __init__(self):
        self.age = 18

    # def __getattr__(self, item):
    #     # 当我们访问的属性不存在时，如果属性不存在 （出现AttributeError时）该方法会被触发
    #     print("由于属性不存在，触发了__getattr__方法")
    #     # 继承父类的此方法
    #     # object.__getattribute__(self,item)
    #     super().__getattribute__(item)
    #     return 100
    #
    # def __getattribute__(self, item):
    #     # 查找属性时，第一时间触发该方法查找属性
    #     print("__触发__getattribute__方法")
    #     # return 100
    #     return super().__getattribute__(item)

    def __setattr__(self, key, value):
        # 此方法为给对象设置属性时触发,重写此方法
        if key == "age":
            # 扩展父类的__setattr__,此处方法属主为当前类
            super().__setattr__(key, 18)
        else:
            print("设置属性的时候触发")
            super().__setattr__(key, value)

        print("设置属性时触发__setattr__方法")
        # print(key)
        # print(value)
        super().__setattr__(key, value)

    def __delattr__(self, item):
        # 此方法在删除属性的时候触发
        print("调用删除属性的方法:__delattr__")
        # 限制不让删除name属性
        if item == "name":
            pass
        else:
            print("调用删除属性的方法:__delattr__")
            # 扩展父类的删除属性方法 删除属性
            super().__delattr__(item)


if __name__ == "__main__":
    t = Test()

    t.name = 10
    print(t.name)
    print(t.age)
    # 删除对象属性
    del t.name
    print(t.name)
    # print(t.name1)
    # print(t.name2)
