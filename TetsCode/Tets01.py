# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 14:58
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : Tets01.py
from datetime import datetime
from time import sleep

now_time = datetime.now()
print(now_time)
for i in range(3):
    print("==========")
    sleep(1)
last_time = datetime.now()
print(last_time)
# print(last_time-now_time)

rt = str(last_time-now_time).split(":")
print(rt)
print(rt[0])
print(rt[1])
print(rt[2])
run_time = (int(rt[1]) * 60) + float(rt[2])