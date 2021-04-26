# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 14:22
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : G109_MainTest.py

from Phone.G109 import G109
import unittest

"""
    G109-安卓9
"""


class Main(unittest.TestCase):
    g109 = G109("9", "com.android.dialer", "com.android.dialer.app.DialtactsActivity")

    @classmethod
    def setUpClass(cls):
        # print("【类】开始执行！")
        pass

    @classmethod
    def tearDownClass(cls):
        # print("【类】结束执行！")
        pass

    def setUp(self):
        print("【方法】开始执行！")
        self.g109.clear_app()

    def tearDown(self):
        print("【方法】结束执行！")
        self.g109.driver_quit()

    def test001_startSpeed(self):
        self.g109.one_app_start("热", 30, "微信", "com.tencent.mm", ["微信", "通讯录", "发现", "我"])
        # self.g109.one_app_start("热", 30, "京东", "com.jingdong.app.mall", ["首页"])
        # self.g109.one_app_start("热", 30, "哔哩哔哩", "tv.danmaku.bili", ["首页", "频道", "动态", "会员购", "我的"])
        # self.g109.one_app_start("热", 30, "Facebook", "com.facebook.katana", ["登录", "新建 Facebook 帐户", "密码", "忘记密码？"], locate_type="desc")
        # self.g109.one_app_start("热", 30, "3DMark", "com.futuremark.dmandroid.application", ["我的测试", "我的结果", "我的设备", "比较"])

    def test002_installSpeed(self):
        # self.g109.install_app(10, "一个木函.apk", "一个木函")
        # self.g109.install_app(10, "今日头条.apk", "今日头条")
        # self.g109.install_app(10, "腾讯视频.apk", "腾讯视频")
        # self.g109.install_app(10, "QQ.apk", "QQ")
        # self.g109.install_app(10, "三国杀.apk", "三国杀")
        # self.g109.install_app(7, "和平精英.apk", "和平精英")
        self.g109.install_app(7, "王者荣耀.apk", "王者荣耀")


# 加载测试用例到测试套件(总共有四种方式，参照：https://blog.csdn.net/weixin_44863956/article/details/104699764)
if __name__ == '__main__':
    # 创建一个测试套件
    suite = unittest.TestSuite()
    # 测试用例类添加到测试套件中
    # loader = unittest.TestLoader()
    # suite.addTest(loader.loadTestsFromTestCase(Main))

    # suite.addTest(Main("test001_startSpeed"))
    suite.addTest(Main("test002_installSpeed"))
    # 运行
    unittest.TextTestRunner().run(suite)
