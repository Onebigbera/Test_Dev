# -*- coding:utf-8 -*-
"""
    使用描述器模拟实现ORM模型
"""


class BaseField(object):
    """所有字段的父类"""
    pass


class CharField(BaseField):
    """
        定义一个描述器，接收字符串类型
    """

    def __init__(self, max_length=20):
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        # 在赋值前进行类型限制
        if isinstance(value, str):
            # 限制其长度
            if len(value) <= self.max_length:
                self.value = value
            else:
                raise ValueError("字符串超过限定长度{}".format(self.max_length))
        else:
            raise TypeError("Need a str type")

    def __delete__(self, instance):
        self.value = None


class IntField(BaseField):
    """
        定义一个描述器，接收整数型
    """

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        # 在赋值前进行类型限制
        if isinstance(value, int):
            self.value = value
        else:
            raise TypeError("Need a Int type")

    def __delete__(self, instance):
        self.value = None


class BoolField(BaseField):
    """
        定义一个描述器，接收布尔类型
    """

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        # 在赋值前进行类型限制
        if isinstance(value, bool):
            self.value = value
        else:
            raise TypeError("Need a Int type")

    def __delete__(self, instance):
        self.value = None


class UserModel(object):
    """
    User 模型类
    """
    name = CharField(max_length=20)
    pwd = CharField()
    age = IntField()
    is_delete = BoolField()


if __name__ == "__main__":
    m = UserModel()

    m.name = "George"
    print(m.name)

    m.age = 18
    print(m.age)

    m.is_delete = False
    print(m.is_delete)
