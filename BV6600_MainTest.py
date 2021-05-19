# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 14:15
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : BV6600_MainTest.py


from Phone.BV6600 import BV6600
import unittest

"""
    BV6600-安卓10
"""


class Main(unittest.TestCase):
    bv6600 = BV6600("10", "com.android.dialer", "com.android.dialer.main.impl.MainActivity")

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
        self.bv6600.clear_app()

    def tearDown(self):
        print("【方法】结束执行！")
        self.bv6600.driver_quit()

    def test001_startSpeed(self):
        print("启动速度")
        # self.bv6600.one_app_start("热", 20, "微信", "com.tencent.mm", ["微信", "通讯录", "发现", "我"])
        # self.bv6600.one_app_start("热", 20, "京东", "com.jingdong.app.mall", ["首页"])
        # self.bv6600.one_app_start("热", 20, "哔哩哔哩", "tv.danmaku.bili", ["首页", "频道", "动态", "会员购", "我的"])
        self.bv6600.one_app_start("热", 20, "Facebook", "com.facebook.katana", ["登录", "新建 Facebook 帐户", "密码", "忘记密码？"], locate_type="desc")
        # self.bv6600.one_app_start("热", 20, "3DMark", "com.futuremark.dmandroid.application", ["我的测试", "我的结果", "我的设备", "比较"])


    def test002_installSpeed(self):
        pass
        # self.bv6600.install_app(5, "QQ.apk", "QQ")
        # self.bv6600.install_app(5, "一个木函.apk", "一个木函")
        # self.bv6600.install_app(5, "今日头条.apk", "今日头条")
        # self.bv6600.install_app(5, "腾讯视频.apk", "腾讯视频")
        # self.bv6600.install_app(5, "三国杀.apk", "三国杀")
        # # bv6600 不能装王者荣耀
        # # self.bv6600.install_app(5, "王者荣耀.apk", "王者荣耀")
        # self.bv6600.install_app(5, "和平精英.apk", "和平精英")


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

