# coding: utf-8
import subprocess

from appium import webdriver

def setUp(params):
    desired_caps = {}
    desired_caps['device'] = 'Android'
    desired_caps['browserName'] = ''
    desired_caps["platformName"] = "Android"
    desired_caps["deviceName"] = "5d6a5e8d"
    desired_caps["appActivity"] = "com.sensorsdata.analytics.android.demo.activity.TestMainActivity"
    desired_caps[
        "app"] = "/Users/zhangxiangwei/AndroidStudioProjects/android/demoAndroidX/build/outputs/apk/debug/demoAndroidX-debug.apk"

    params.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# 测试用例执行完成后的操作
def tearDown(params):
    params.driver.quit()
    print('end ... ')


# 获取桌面的Activity
def getDesktopActivity():
    output = subprocess.getstatusoutput('adb shell dumpsys activity | grep "mFocusedActivity"')
    aaa = output[1]
    bbb = aaa.split("/")
    ccc = bbb[1].split(" ")
    result = ccc[0]
    return result


# 获取被测试应用的进程号
def getPorcessId(packageName):
    command = "adb shell ps | grep " + "'" + packageName + "'"
    output = subprocess.getstatusoutput(command)
    result = ""
    if (output[1] == ""):
        pass
    else:
        aaa = output[1]
        bbb = aaa.split("\r\n")
        for i in bbb:
            ccc = i.split(" ")
            li = []
            for j in ccc:
                if (j != ""):
                    li.append(j)
            li[8] = li[8].replace("\r", "")  # 去掉字符串末尾的换行符号
            li[8] = li[8].replace("\n", "")  # 去掉字符串末尾的换行符号
            if (li[8] == packageName):
                result = li[1]
    return result


# 判断当前activity是否为被测试Activity
def isTestActivity(params):
    activity = params.testActivity
    curActivity = params.driver.current_activity
    if (activity == curActivity):
        return True
    else:
        return False


# 让用例执行失败
def excuteFailed(info):
    print("do excuteFailed ...")
    raise Exception(info)


