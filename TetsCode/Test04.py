# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 15:10
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : Test04.py
from datetime import datetime, time


def fun1():
    return 1, 2


x, y = fun1()

print(fun1()[0])
print(x)
print(datetime.today())