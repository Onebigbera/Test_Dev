# -*- coding:utf-8 -*-
"""
    描述器
        包含以下方法的其中一种的类称之为 描述器类。
        object.__get__(self,instance,owner)
            调用此方法以获取所有者类的属性（类属性访问）或该类的实例的属性（实例属性访问）。
            所有者使之所有者类，而实例使之被用来访问属性的实例，当所有者被用来访问的属性为None,则此方法返回属性值或者引发一个AttributeError异常
        object.__set__(self,instance,owner)
            调用此方法以设置instance所指定的所有者类的实例的属性为新值value
        object.__delete__(self,instance)
            调用此方法以删除instance指定的所有者的实例的属性
        object.__set_name__(self,owner,name)
            在所有者类owner创建时被调用，描述器会被赋值给name.
"""


class Field(object):
    """
    一个类中，只要出现以下三个方法中的任意一个，那么该类就被称为描述器
    """

    def __get__(self, instance, owner):
        print("__get__方法被触发")
        print("instance对象为{}".format(instance))
        print("owner对象为{}".format(owner))
        return self.value

    def __set__(self, instance, value):
        """
        self为Field对象
        :param instance: 传入的对象，此处为m，即为Model对象
        :param value: value 为设置的值 100
        :return:
        """
        print("__set__方法被触发")
        self.value = value
        print(self)
        print(instance)
        print(value)

    def __delete__(self, instance):
        print("删除属性的时候触发__delete__")
        # del self.value
        self.value = None


class Model(object):
    name = "George"
    # 用一个描述器对象来存储一个变量
    """
        描述器对象：会覆盖类属性相关操作
    """
    attr = Field()


if __name__ == "__main__":
    m = Model()
    # m.name = "Jack"
    # print(m.name)
    m.attr = 100
    print(m.attr)
