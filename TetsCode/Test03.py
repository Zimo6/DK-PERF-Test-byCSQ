# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 14:13
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : Test03.py
import time

nowtime1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
nowtime2 = time.strftime('%Y-%m-%d', time.localtime(time.time()))

print(nowtime1)
print(type(nowtime1))