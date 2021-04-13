# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 14:03
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : BasePhone.py
"""
    公共类：所有Phone类继承该类，此类包含性能测试所有方法
"""
import os
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class BasePhone(object):

    def __init__(self, android_version, package_name, activity_name):
        """
        :param android_version: 安卓版本
        :param package_name:    启动包名
        :param activity_name:   启动Activity
        """
        desired_caps = {
            'platformName': 'Android',  # 平台名称
            'deviceName': 'test',  # 设备名称(任写)
            'platformVersion': android_version,  # 安卓版本
            'appPackage': package_name,  # 启动包名
            'appActivity': activity_name,  # 启动 Acclivity
            'noReset': True,  # 重置(不会保留之前的启动数据)
        }
        if android_version == "11":
            # Android 11 添加此参数
            desired_caps["automationName"] = "uiautomator2"
        # 开始初始化
        print("Appium 正在初始化...")

        # 启动服务/通过4723端口来建立一个会话
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # 隐式等待10s
        self.driver.implicitly_wait(10)
        print("Appium 初始化完成...")
        self.driver.keyevent(3)

    # 退出
    def driver_quit(self):
        self.driver.quit()
        print("Appium 成功退出！...")

    # 查找元素
    def find_element(self, way, value):
        if way == "text":
            return self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % value)
        elif way == "id":
            return self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")' % value)
        elif way == "desc":
            return self.driver.find_element_by_android_uiautomator('new UiSelector().description("%s")' % value)
        else:
            print("定位方式待更新")

    # 等待元素(默认等待180秒)
    def wait_element(self, way, value, time=180):
        if way == "text":
            WebDriverWait(self.driver, time).until(
                lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("%s")' % value))
        elif way == "id":
            WebDriverWait(self.driver, time).until(
                lambda x: x.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")' % value))
        elif way == "desc":
            WebDriverWait(self.driver, time).until(
                lambda x: x.find_element_by_android_uiautomator('new UiSelector().description("%s")' % value))
        else:
            print("等待方式方式待更新！")

    # 点击元素
    def click_element(self, way, value):
        self.find_element(way, value).click()

    # 长按某个元素（默认长按2秒且释放）
    def long_press_element(self, way, value, duration=2000, release="yes"):
        if release == "yes":
            # 长按某个元素2秒然后释放
            TouchAction(self.driver).long_press(self.find_element(way, value), duration=duration).release().perform()
        else:
            # 长按某个元素2秒钟（不释放）
            TouchAction(self.driver).long_press(self.find_element(way, value), duration=duration).perform()

    # 等待元素出现并点击
    def wait_and_click_element(self, way, value):
        self.wait_element(way, value)
        self.click_element(way, value)

    # 点击某个点 (可以点击多个点，参数加入多个列表,keep_time为点击保持的时间)
    def click_point(self, x, y, keep_time=100):
        self.driver.tap([(x, y)], keep_time)

    # 长按某个点（默认长按2秒且释放）
    def long_press_point(self, x, y, duration=2000, release="yes"):
        if release == "yes":
            # 长按某个点2秒然后释放
            TouchAction(self.driver).long_press(x=x, y=y, duration=duration).release().perform()
        else:
            # 长按某个点2秒钟（不释放）
            TouchAction(self.driver).long_press(x=x, y=y, duration=duration).perform()

    # 滑动
    def swipe_point(self, x1, y1, x2, y2):
        """
        :param x1:  起始点x轴
        :param y1:  起始点y轴
        :param x2:  结束点x轴
        :param y2:  结束点y轴
        :param duration: 滑动速度(默认20ms)
        :return:
        """
        self.driver.swipe(start_x=x1, start_y=y1, end_x=x2, end_y=y2)

    # 取列表最大值、最小值、平均值（去掉一个最大值，去掉一个最小值）
    def get_list_avg(self, num_list):
        # print(f"最大值：{max(num_list)}")
        # print(f"最小值：{min(num_list)}")
        # print(f"平均值：{(sum(num_list) - (max(num_list) + min(num_list))) / (len(num_list) - 2)}")
        # 返回list参数的最大值、最小值、平均值
        return max(num_list), min(num_list), (sum(num_list) - (max(num_list) + min(num_list))) / (len(num_list) - 2)

    # 格式化时间戳
    def format_time(self, time):
        # 通过split函数对总用时进行切割，用来提取秒和毫秒，产生一个列表rt
        rt = str(time).split(":")
        return (int(rt[1]) * 60) + float(rt[2])

    # 根据包名清掉进程
    def kill_process_by_packages_name(self, packages_name):
        os.system(f"adb shell am force-stop {packages_name}")
        print(f"包名：{packages_name}, 已清除。")

    # 判断目录是否存在，不存在则创建
    def write(self, test_type, test_info, dir_path_name):
        # TestResult 目录下是否存在目录
        phone_dir = os.path.abspath(os.path.join(os.getcwd(), "./TestResult/" + dir_path_name))
        now_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        file_path = os.path.join(phone_dir, f"{dir_path_name}"+"-"+test_type+"-"+now_time+"-TestResult.txt")
        # print(os.path.abspath(os.path.join(os.getcwd())))
        # print(d)
        if not os.path.isdir(phone_dir):
            os.mkdir(phone_dir)
        else:
            pass

        with open(file_path, "a+", encoding="utf-8") as f:
            # f.write(now_time + ":" + text_info + "\n")
            f.write(test_info+ "\n")

