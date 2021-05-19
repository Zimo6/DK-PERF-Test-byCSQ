# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 10:09
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : BV4900_Main_Test.py


from Phone.BV4900 import BV4900
import unittest

"""
    BV4900-安卓10
"""


class Main(unittest.TestCase):
    # bv4900 = BV4900("11", "com.google.android.dialer", "com.google.android.dialer.extensions.GoogleDialtactsActivity")
    bv4900 = BV4900("10", "com.android.dialer", "com.android.dialer.main.impl.MainActivity")

    @classmethod
    def setUpClass(cls):
        print("【类】开始执行！")

    @classmethod
    def tearDownClass(cls):
        print("【类】结束执行！")
        cls.bv4900.driver_quit()

    def setUp(self):
        print("【方法】开始执行！")
        self.bv4900.clear_app()

    def tearDown(self):
        print("【方法】结束执行！")
        # self.bv4900.driver_quit()

    def test001_startSpeed(self):
        print("启动速度")
        # self.bv4900.one_app_start("热", 10, "微信", "com.tencent.mm", ["微信", "通讯录", "发现", "我"])
        # self.bv4900.one_app_start("热", 10, "京东", "com.jingdong.app.mall", ["首页"])
        # self.bv4900.one_app_start("热", 10, "哔哩哔哩", "tv.danmaku.bili", ["首页", "频道", "动态", "会员购", "我的"])
        # self.bv4900.one_app_start("热", 10, "3DMark", "com.futuremark.dmandroid.application", ["我的测试", "我的结果", "我的设备", "比较"])
        self.bv4900.one_app_start("热", 10, "Chrome", "com.android.chrome", ["搜索或输入网址"])
        # self.bv4900.one_app_start("热", 10, "Facebook", "com.facebook.katana", ["登录", "新建 Facebook 帐户", "密码", "忘记密码？"], locate_type="desc")

    def test002_installSpeed(self):
        print("安装速度")
        # self.bv4900.install_app(6, "一个木函.apk", "一个木函")
        # self.bv4900.install_app(6, "今日头条.apk", "今日头条")
        self.bv4900.install_app(6, "腾讯视频.apk", "腾讯视频")
        self.bv4900.install_app(6, "QQ.apk", "QQ")
        self.bv4900.install_app(6, "三国杀.apk", "三国杀")
        self.bv4900.install_app(5, "和平精英.apk", "和平精英")
        # self.bv4900.install_app(6, "王者荣耀.apk", "王者荣耀")


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
