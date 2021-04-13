# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 14:10
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : DemoPhone.py
import os
from datetime import datetime
from time import sleep

from Common.BasePhone import BasePhone

"""
    Demo：BL6000Pro(安卓11)
"""


class  DemoPhone(BasePhone):
    # 测试机型号
    phone_model = os.popen("adb shell getprop ro.product.model").read().strip('\n')
    # 桌面元素
    desktop_key = "电话"

    # 创建汇总测试结果的目录
    def write_test_info(self, test_type, test_info, pm=phone_model):
        self.write(test_type, test_info, pm)

    # 清后台
    def clear_app(self):
        self.driver.keyevent(3)
        self.wait_element("text", self.desktop_key)
        self.driver.keyevent(187)
        self.wait_element("id", "android:id/content")
        if self.find_element("text", "全部清除"):
            self.click_element("text", "全部清除")
        elif self.find_element("desc", "近期没有任何内容"):
            self.driver.keyevent(3)
        else:
            print("清后台异常，请调试代码！")
        print(f"{self.phone_model}后台已清空...")

    # 测试单应用启动速度（冷热启动）
    def one_app_start(self, start_way, times, app_name, apk_name, app_key_list, locate_type="text"):
        """
        注：启动速度相被测App须放桌面
        :param start_way:       启动方式
        :param times:           测试次数
        :param app_name:        测试APP
        :param apk_name:        测试包名
        :param app_key_list:    成功打开APP关键字（text元素）
        :param locate_type:     启动成功定位方式（默认为text）
        :return:
        """
        # if app_key_list is None:
        #     app_key_list = []
        # print(f"启动方式：{start_way}\n测试次数：{times}\n测试APP：{app_name}")
        self.write_test_info("启动速度", f"启动方式：{start_way}\n测试次数：{times}\n测试APP：{app_name}")
        self.driver.keyevent(3)
        self.wait_element("text", self.desktop_key)
        # 冷/热 准备工作
        if start_way == "冷":
            self.kill_process_by_packages_name(apk_name)
            sleep(1)
        elif start_way == "热":
            self.wait_and_click_element("text", app_name)
            # 等待所有元素加载完
            for l in app_key_list:
                self.wait_element(locate_type, l)
            self.driver.keyevent(3)
            self.wait_element("text", self.desktop_key)

        total_time = []  # 每次启动的时间,存入数组
        for i in range(times):
            self.wait_and_click_element("text", app_name)
            # 开始计时
            start_time = datetime.now()
            # 忽略安全（竞品手机）
            # self.wait_and_click_element("text", "忽略")
            # 是否找到成功启动标志
            for l in app_key_list:
                self.wait_element(locate_type, l)
            # 结束计时
            last_time = datetime.now()
            # 得到总用时
            time = last_time - start_time
            total_time.append(self.format_time(time))
            # print(f"第{i + 1}次启动时间为：{self.format_time(time)}")
            self.write_test_info("启动速度", f"第{i + 1}次启动时间为：{self.format_time(time)}")
            # 冷启动则清后台
            if start_way == "冷":
                self.kill_process_by_packages_name(apk_name)
                sleep(1)
            elif start_way == "热":
                self.driver.keyevent(3)
                self.wait_element("text", self.desktop_key)
        self.get_list_avg(total_time)

    # 安装/卸载速度
    def install_app(self, times, apk_name, app_name, file_app="文件极客"):
        """
        注：便于测试，文件极客须放桌面
        :param times:    测试次数
        :param apk_name: 安装包名
        :param app_name: APP名
        :param file_app: 文件管理名
        :return:
        """
        self.write_test_info("安装卸载", f"安装/卸载-测试次数：{times}\n测试APP：{app_name}")
        self.driver.keyevent(3)
        self.wait_element("text", self.desktop_key)
        # 每次启动的时间,存入数组
        install_total_time = []
        uninstall_total_time = []
        # 通过文件极客(须放桌面)
        self.wait_and_click_element("text", file_app)
        sleep(1)
        # 先进入文件极客首页
        for i in range(10):
            if "浏览" in self.driver.page_source:
                break
            else:
                self.driver.keyevent(4)
                sleep(1)
        # 找安装包
        for i in range(times):
            for j in range(10):
                sleep(1)
                if "应用" in self.driver.page_source:
                    break
                else:
                    self.swipe_point(350, 1200, 350, 350)
            self.wait_and_click_element("text", "应用")
            self.wait_and_click_element("text", "应用安装文件 (APK)")
            for k in range(10):
                if apk_name in self.driver.page_source:
                    break
                else:
                    # 上滑
                    self.swipe_point(350, 1200, 350, 600)
            self.wait_and_click_element("text", apk_name)
            # 开始安装
            self.wait_and_click_element("text", "安装")
            # 开始计时
            install_start_time = datetime.now()
            while True:
                if "打开" in self.driver.page_source:
                    break
            install_last_time = datetime.now()
            install_time = install_last_time - install_start_time  # 得到总用时
            install_total_time.append(self.format_time(install_time))
            self.write_test_info("安装卸载", f"第{i + 1}次安装时间为：{self.format_time(install_time)}")
            # 【***卸载准备再次安装***】
            sleep(1)
            self.driver.keyevent(4)
            self.wait_and_click_element("text", "应用")
            self.wait_and_click_element("text", "已安装的应用")
            for l in range(10):
                if app_name in self.driver.page_source:
                    break
                # 上滑
                self.swipe_point(350, 1200, 350, 350)
            self.wait_and_click_element("text", app_name)
            self.wait_and_click_element("text", "卸载")
            self.wait_and_click_element("text", "确定")
            uninstall_start_time = datetime.now()
            # 等待卸载完成
            while True:
                if "已安装的应用" in self.driver.page_source:
                    break
            uninstall_last_time = datetime.now()
            uninstall_time = uninstall_last_time - uninstall_start_time  # 得到总用时
            uninstall_total_time.append(self.format_time(uninstall_time))
            self.write_test_info("安装卸载", f"第{i + 1}次卸载时间为：{self.format_time(uninstall_time)}")
            sleep(1)
            self.driver.keyevent(4)
        print(f"安装时间：")
        self.get_list_avg(install_total_time)
        print(f"卸载时间：")
        self.get_list_avg(uninstall_total_time)


# if __name__ == '__main__':
#     demo = DemoPhone("10", "com.android.dialer", "com.android.dialer.main.impl.MainActivity")
#     # demo.clear_app()
#     # demo.install_app(10, "Facebook.APK", "Facebook")
#     demo.mkdir()