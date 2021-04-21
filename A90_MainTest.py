# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 11:30
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : A90_MainTest.py

from Phone.A90 import A90
import unittest

"""
    A90-安卓11
"""


class Main(unittest.TestCase):
    a90 = A90("11", "com.google.android.dialer",
              "com.google.android.dialer.extensions.GoogleDialtactsActivity")

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
        self.a90.clear_app()

    def tearDown(self):
        print("【方法】结束执行！")
        self.a90.driver_quit()

    def test001_startSpeed(self):
        # 先测热启
        start_flag = "热"
        for i in range(1):
            # 微信
            # self.a90.one_app_start(start_flag, 10, "微信", "com.tencent.mm", ["微信", "通讯录", "发现", "我"])
            # 哔哩哔哩
            self.a90.one_app_start(start_flag, 10, "哔哩哔哩", "tv.danmaku.bili", ["首页", "频道", "动态", "会员购", "我的"])
            # 京东
            # self.a90.one_app_start(start_flag, 10, "京东", "com.jingdong.app.mall", ["首页"])
            # 3D Mark
            # self.a90.one_app_start(start_flag, 10, "3DMark", "com.futuremark.dmandroid.application", ["我的测试", "我的结果", "我的设备", "比较"])
            # Facebook
            # self.a90.one_app_start(start_flag, 10, "Facebook", "com.facebook.katana", ["登录", "新建 Facebook 帐户", "密码", "忘记密码？"], locate_type="desc")
            start_flag = "冷"

    def test002_installSpeed(self):
        self.a90.install_app(5, "QQ.apk", "QQ")
        self.a90.install_app(5, "一个木函.apk", "一个木函")
        self.a90.install_app(5, "今日头条.apk", "今日头条")
        self.a90.install_app(5, "腾讯视频.apk", "腾讯视频")
        self.a90.install_app(5, "三国杀.apk", "三国杀")
        # A90 不能装王者荣耀
        # self.a90.install_app(5, "王者荣耀.apk", "王者荣耀")
        self.a90.install_app(5, "和平精英.apk", "和平精英")


# 加载测试用例到测试套件(总共有四种方式，参照：https://blog.csdn.net/weixin_44863956/article/details/104699764)
if __name__ == '__main__':
    # 创建一个测试套件
    suite = unittest.TestSuite()
    # 测试用例类添加到测试套件中
    # loader = unittest.TestLoader()
    # suite.addTest(loader.loadTestsFromTestCase(Main))

    suite.addTest(Main("test001_startSpeed"))
    # suite.addTest(Main("test002_installSpeed"))
    # 运行
    unittest.TextTestRunner().run(suite)
