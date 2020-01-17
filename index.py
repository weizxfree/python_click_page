# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import subprocess
import time

from FindJson import parseJson
from startTest import start

testdir = "/Users/zhangxiangwei/PycharmProjects/HelloWorld/log/"


def clearAdbLog():
    cmd = r"/Users/zhangxiangwei/Library/Android/sdk/platform-tools/adb logcat -c"
    subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)


def generateLogfile():
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    logcatname = testdir + now + ".log"
    cmd = r"/Users/zhangxiangwei/Library/Android/sdk/platform-tools/adb logcat -s SA.AnalyticsMessages:I -v raw >%s" % (
        logcatname)
    subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)


clearAdbLog()
generateLogfile()

start()
parseJson()
