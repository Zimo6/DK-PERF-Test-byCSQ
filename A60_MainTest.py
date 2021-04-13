# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 17:43
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : A60_MainTest.py
import unittest
from Phone.A60 import A60

"""
    A60-安卓10
"""


class Main(unittest.TestCase):
    demo = A60("8", "com.android.dialer", "com.android.dialer.app.DialtactsActivity")

    @classmethod
    def setUpClass(cls):
        cls.demo.clear_app()

    @classmethod
    def tearDownClass(cls):
        cls.demo.driver_quit()

    # def setUp(self):
    #     print("方法 开始执行一次")
    #     self.demo.clear_app()
    #
    # def tearDown(self):
    #     print("方法 结束执行一次")
    #     self.demo.driver_quit()

    def test001_startSpeed(self):
        # self.demo.one_app_start("热", 10, "酷安", "com.coolapk.market", ["首页", "数码", "发现", "应用游戏", "我"])
        # self.demo.one_app_start("热", 10, "3DMark", "com.futuremark.dmandroid.application", ["我的测试", "我的结果", "我的设备", "比较"])
        # self.demo.one_app_start("热", 10, "Geekbench 4", "com.primatelabs.geekbench", ["处理器", "运算跑分", "电池跑分"])
        # self.demo.one_app_start("冷", 10, "QQ", "com.tencent.mobileqq", ["欧成"])
        self.demo.one_app_start("冷", 10, "QQ", "com.tencent.mobileqq", ["欧成"])

    def test002_installSpeed(self):
        # self.demo.install_app(5, "androbench.apk", "AndroBench")
        # self.demo.install_app(5, "酷安.apk", "酷安")
        # self.demo.install_app(5, "3DMark.apk", "3DMark")
        # self.demo.install_app(5, "夸克.apk", "夸克")
        self.demo.install_app(5, "Antutu3DLite.apk", "安兔兔评测3DLite")
