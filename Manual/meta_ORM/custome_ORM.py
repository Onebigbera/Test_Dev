# -*- coding:utf-8 -*-
"""
    自定义实现模型类
"""
from discriber_model import BaseField, CharField, IntField, BoolField


class FieldMetaClass(type):
    """模型类的元类"""

    def __new__(cls, name, bases, dict_attr, *args, **kwargs):
        table_name = name.lower()  # 将类名转换为小写，对应数据库表的名称
        fields_1 = {}  # 定义一个空字典，用来存放模型类字段和数据库表中字段对应的关系
        for key, value in dict_attr.items():  # 遍历所有的属性
            if isinstance(key, BaseField):  # 判断属性值是否为字段类型
                fields_1[key] = value
        dict_attr['t_name'] = table_name
        dict_attr['fields'] = fields_1
        print(fields_1)
        return super().__new__(cls, name, bases, dict_attr)


class BaseModel(metaclass=FieldMetaClass):
    """在此类中实现由对象到数据库的映射关系"""

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)  # 遍历得到所有的关键字参数，并给其赋对应值
            print(k, v)

    def save(self):
        """保存一条数据，对应生成一条sql语句
            获取表名、获取字段名称和值、生成对应的SQL
        """
        # 获取表名称
        t_name = self.t_name
        # 获取对应字段的值
        fields = self.fields
        field_dict = {}  # 创建一个空字典 用来存储键值对
        for field in fields.keys():
            field_dict[field] = getattr(self, field)

            # 生成对应的SQL
            sql = "INSERT INTO {} VALUES {}".format(t_name, tuple(field_dict.values()))
            print(sql)


class User(BaseModel):
    """用例模型类"""

    username = CharField()
    pwd = CharField()
    age = IntField()
    is_delete = BoolField()


class Oder(BaseModel):
    """订单模型类"""
    id = IntField()
    money = IntField()


if __name__ == "__main__":
    print(User.fields)
    print(User.t_name)

    xiaoming = User(name='xiaoming', age=18, pwd='123', is_delete=False)
