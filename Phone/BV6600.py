# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 14:05
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : BV6600.py



import os
from datetime import datetime
from time import sleep
from Common.BasePhone import BasePhone

"""
    BV6600(安卓10)
"""


class BV6600(BasePhone):
    # 测试机型号
    phone_model = os.popen("adb shell getprop ro.product.model").read().strip('\n')
    # 桌面元素
    desktop_key = "电话"

    # 创建汇总测试结果的目录
    def write_test_info(self, test_type, test_info, pm=phone_model):
        self.write(test_type, test_info, pm)

    # 删除测试结果

    # 清后台
    def clear_app(self):
        self.driver.keyevent(3)
        self.wait_element("text", self.desktop_key)
        self.driver.keyevent(187)
        sleep(1)

        # for i in range(30):
        #     if self.desktop_key in self.driver.page_source:
        #         break
        #     else:
        #         self.swipe_point(300, 1200, 300, 300)
        #         sleep(1)
        # self.wait_element("text", "全部清除")
        self.click_point(438, 1100)
        self.wait_element("text", self.desktop_key)
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
        self.write_test_info("启动速度", f"=================分割线=================\n测试开始时间：{datetime.now()}")
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
        self.write_test_info("启动速度",
                             f"最大值:{self.get_list_avg(total_time)[0]}\n"
                             f"最小值:{self.get_list_avg(total_time)[1]}\n"
                             f"平均值:{self.get_list_avg(total_time)[2]}\n")

