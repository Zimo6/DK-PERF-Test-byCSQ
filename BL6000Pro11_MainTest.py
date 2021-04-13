# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 14:24
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : BL6000Pro11_MainTest.py

import unittest
from Phone.BL6000Pro11 import BL6000Pro11

"""
    BL6000Pro-安卓11
"""


class Main(unittest.TestCase):
    demo = BL6000Pro11("11", "com.google.android.dialer", "com.google.android.dialer.extensions.GoogleDialtactsActivity")

    @classmethod
    def setUpClass(cls):
        # cls.demo.clear_app()
        # 安装测试相关app
        # cls.demo.install_testApp
        pass

    @classmethod
    def tearDownClass(cls):
        print("【类】结束执行！")
        cls.demo.driver_quit()

    def setUp(self):
        print("【方法】开始执行！")
        self.demo.clear_app()

    # def tearDown(self):
    #     print("【方法】结束执行！")
    #     self.demo.driver_quit()

    def test001_startSpeed(self):
        # self.demo.one_app_start("冷", 5, "相机", "com.mediatek.camera", ["照片", "视频"])
        self.demo.one_app_start("热", 5, "相机", "com.mediatek.camera", ["照片", "视频"])

    def test002_installSpeed(self):
        self.demo.install_app(3, "知乎.apk", "知乎")

