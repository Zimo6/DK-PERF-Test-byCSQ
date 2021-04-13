# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 11:51
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : Multilaser_F_Pro_2_MainTest.py

import unittest
from Phone.Multilaser_F_Pro_2 import Multilaser_F_Pro_2


class Main(unittest.TestCase):
    demo = Multilaser_F_Pro_2("11", "com.google.android.dialer", "com.google.android.dialer.extensions.GoogleDialtactsActivity")

    @classmethod
    def setUpClass(cls):
        print("【类】开始执行！")
        cls.demo.clear_app()
        # 安装测试相关app
        # cls.demo.install_testApp

    @classmethod
    def tearDownClass(cls):
        print("【类】结束执行！")
        cls.demo.driver_quit()

    # def setUp(self):
    #     print("【方法】开始执行！")
    #
    # def tearDown(self):
    #     print("【方法】结束执行！")

    def test001_startSpeed(self):
        # self.demo.one_app_start("热", 10, "酷安", "com.coolapk.market", ["首页", "数码", "发现", "应用游戏", "我"])
        # self.demo.one_app_start("热", 10, "3DMark", "com.futuremark.dmandroid.application", ["我的测试", "我的结果", "我的设备", "比较"])
        self.demo.one_app_start("热", 10, "Geekbench 4", "com.primatelabs.geekbench", ["处理器", "运算跑分", "电池跑分"])

    def test002_installSpeed(self):
        self.demo.install_app(5, "androbench.apk", "AndroBench")
        self.demo.install_app(5, "酷安.apk", "酷安")
        self.demo.install_app(5, "3DMark.apk", "3DMark")
        self.demo.install_app(5, "夸克.apk", "夸克")
        self.demo.install_app(5, "Antutu3DLite.apk", "安兔兔评测3DLite")

