# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 16:15
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : BL6000Pro10_MainTest.py
import unittest
from Phone.DemoPhone import DemoPhone

"""
    BL6000Pro-安卓10
"""


class Main(unittest.TestCase):
    demo = DemoPhone("10", "com.android.dialer", "com.android.dialer.main.impl.MainActivity")

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
        self.demo.one_app_start("热", 10, "相机", "com.mediatek.camera", ["拍照", "美颜"])

    def test002_installSpeed(self):
        self.demo.install_app(10, "王者荣耀.apk", "王者荣耀")
