# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 11:51
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : Test05.py

"""
    python 执行adb命令
"""
import os

result = os.system("adb devices")

print(result)