# -*- coding: utf-8 -*-
# @Time    : 2021/5/10 16:09
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : Tab8E_MainTest.py


from Phone.Tab8E import Tab8E
import unittest

"""
    Tab8E-安卓10
"""


class Main(unittest.TestCase):
    tab8e = Tab8E("10", "com.android.settings", "com.android.settings.Settings")

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
        self.tab8e.clear_app()

    def tearDown(self):
        print("【方法】结束执行！")
        self.tab8e.driver_quit()

    def test001_startSpeed(self):
        print("启动速度")
        # self.tab8e.one_app_start("热", 6, "京东", "com.jingdong.app.mall", ["首页"])
        # self.tab8e.clear_app()
        # self.tab8e.one_app_start("热", 6, "今日头条", "com.ss.android.article.news", ["首页"])
        # self.tab8e.clear_app()
        # self.tab8e.one_app_start("热", 6, "微信", "com.tencent.mm", ["微信", "通讯录", "发现", "我"])
        # self.tab8e.clear_app()
        self.tab8e.one_app_start("热", 6, "哔哩哔哩", "tv.danmaku.bili", ["首页", "频道", "动态", "会员购", "我的"])
        # self.tab8e.clear_app()
        # self.tab8e.one_app_start("热", 6, "Facebook", "com.facebook.katana", ["登录", "新建 Facebook 帐户", "密码", "忘记密码？"], locate_type="desc")
        # self.tab8e.clear_app()
        # self.tab8e.one_app_start("热", 6, "3DMark", "com.futuremark.dmandroid.application", ["我的测试", "我的结果", "我的设备", "比较"])

    def test002_installSpeed(self):
        print("安装速度")
        # self.tab8e.install_app(6, "爱奇艺.apk", "爱奇艺")
        # self.tab8e.install_app(6, "支付宝.apk", "支付宝")
        # self.tab8e.install_app(6, "美团.apk", "美团")
        # self.tab8e.install_app(6, "QQ.apk", "QQ")
        # self.tab8e.install_app(6, "原神.apk", "原神")
        self.tab8e.install_app(3, "和平精英.apk", "和平精英")


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
