# -*- coding:utf-8 -*-
import gc

res = gc.get_threshold()
print(res)


a = 100
b = 100

print(id(a))
print(id(b))
print(a is b)
