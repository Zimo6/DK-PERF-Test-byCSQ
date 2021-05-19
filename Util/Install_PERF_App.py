# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 11:19
# @Author  : CuiShuangqi
# @Email   : 2807481686@qq.com
# @File    : Install_PERF_App.py
import os

"""
    安装性能测试相关的apk

    adb install -r -g 安装包
    -r: 强制安装，替换已存在的应用程序
    -g：为应用程序授予所有运行时的权限

"""


#   安装性能测试工具App
def install_perf_app():
    perf_dir = os.path.abspath(os.path.join(os.getcwd(), "../Apks/PERF_App"))
    print(f"性能测工具App目录：{perf_dir}")
    for root, dirs, files in os.walk(perf_dir):
        for apk in files:
            if apk.endswith("3DMark.apk") or apk.endswith(".APK"):
                if os.system(f"adb install -r -g {perf_dir}/{apk}") != 0:
                    print(f"{apk} 安装失败！\n")
                    break
                else:
                    print(f"{apk} 安装成功！\n")


#   安装测试启动速度的App
def install_Startup_app():
    perf_dir = os.path.abspath(os.path.join(os.getcwd(), "../Apks/Startup_App"))
    print(f"启动速度App目录：{perf_dir}")
    for root, dirs, files in os.walk(perf_dir):
        for apk in files:
            if apk.endswith(".apk") or apk.endswith(".APK"):

                if os.system(f"adb install -r -g {perf_dir}/{apk}") != 0:
                    print(f"{apk} 安装失败！\n")
                    break
                else:
                    print(f"{apk} 安装成功！\n")


#   将测试安装/卸载的Apk push到手机内
def push_Install_app():
    perf_dir = os.path.abspath(os.path.join(os.getcwd(), "../Apks/Install_App"))
    print(f"安装速度App目录：{perf_dir}")
    for root, dirs, files in os.walk(perf_dir):
        for apk in files:
            if apk.endswith(".apk") or apk.endswith(".APK"):
                if os.system(f"adb push {perf_dir}\\{apk} /sdcard/{apk}") != 0:
                    print(f"{apk} push失败！")
                    break
                else:
                    print(f"{apk} push成功！")


#   等待手机连接
def wait_for_phone():
    print("等待手机连接...")
    os.system("adb wait-for-device")
    device_name = os.popen("adb devices").read().strip("List of devices attached\n").strip(" ")
    # print(device_name)
    print(f"手机连接成功！\n设备名：{device_name}")


def main(appType):
    if appType == "perf":
        install_perf_app()
    elif appType == "start":
        install_Startup_app()
    elif appType == "install":
        push_Install_app()
    else:
        print("你是煞笔吗？")


if __name__ == '__main__':
    wait_for_phone()
    appType = input("1.perf:   安装性能相关App\n"
                    "2.start:  安装启动速度App\n"
                    "3.install:安装安装速度App\n"
                    "请输入指令:")
    main(appType)
