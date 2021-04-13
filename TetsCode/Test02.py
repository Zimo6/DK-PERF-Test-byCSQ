# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 16:01
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : Test02.py
import os

a = os.path.abspath(os.path.join(os.getcwd(), "../TestResult/"+"aa"))
print(a)

if os.path.isdir(a):
    print(a)
else:
    print("目录不存在，马上创建")
    os.mkdir(a)