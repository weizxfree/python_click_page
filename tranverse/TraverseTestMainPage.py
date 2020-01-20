# coding:utf-8
import sys

from tranverse import TraverseEles

curDir = sys.path[0]
sys.path.append(curDir + '/common')
from file import Common

import unittest
from time import sleep


class TraverseDiscaveryPage(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)
        self.lastEleIndex = 0
        self.currentEleIndex = 0
        self.appPackage = 'com.sensorsdata.analytics.android.demo'
        self.desktopActivity = Common.getDesktopActivity()
        self.appActivity = '.activity.TestMainActivity'  # 设置被测试应用的启动Activity
        self.testActivity = ".activity.TestMainActivity"  # 设置被测试应用的页面的activity
        print('************************** TraverseDiscaveryPage test **************************')
        print(Common.getDesktopActivity())

    # 初始化操作
    def setUp(self):
        Common.setUp(self)

    # 测试用例执行完成后的操作
    def tearDown(self):
        Common.tearDown(self)

    # 初始化进入某个指定的页面进行遍历测试
    def goIntoPage(self):

        # 判断当前Activity是否为被测试Activity，如果不是抛出异常，让用例执行失败
        if (Common.isTestActivity(self)):
            print("被测试的Activity为：" + self.driver.current_activity + ",是被测试的Activity")
        else:
            Common.excuteFailed("不是被测试activity")

    def test_traverse_discavery_page(self):
        TraverseEles.traverse_all_elements(self)
        sleep(10)



def suite(self):
    suite = unittest.TestSuite()
    suite.addTest(TraverseDiscaveryPage('test_traverse_discavery_page'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
