# -*- coding:utf-8 -*-
"""
    自定义元类
        自定义元类必须继承type
"""


class MyMetaClass(type):
    """自定义元类"""

    def __new__(cls, name, bases, attr_dict, *args, **kwargs):
        print("最基础的自定义元类")

        # 遍历属性名称  attr_dict.items() 返回生成器对象
        print(111, list(attr_dict.items()), "这是一个列表")
        print(222, attr_dict.items(), "这是一个生成器，迭代的时候是动态的") # 遍历字典的时候，不允许添加元素或者修改元素
        for k, v in list(attr_dict.items()):
            attr_dict.pop(k)
            print(k)
            attr_dict[k.upper()] = v
        print(333, list(attr_dict.items()))
        attr_dict["__slots__"] = ["name", "gender"]

        return super().__new__(cls, name, bases, attr_dict)
        # 在 父类的基础上扩展自身的参数,直接使用type时不需要cls参数
        # type.__new__(name, bases, attr_dict)


# 通过自定义元类来创建
class Test(metaclass=MyMetaClass):
    """
    如果metaclass不赋值，默认使用type类，也可以使用自定义的元类
    """
    name = "George"
    gender = "男"
    # 最后一个没有被遍历到 todo
    age = 99


class MyClass(Test):
    """
    父类指定元类，子类继承父类所指定的元类
    """
    pass


if __name__ == "__main__":
    print(type(Test))
    print(type(MyClass))
    print(Test.__dict__)
