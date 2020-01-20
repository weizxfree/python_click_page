# coding:utf-8
import sys

curDir = sys.path[0]
from time import sleep


# 遍历点击页面所有元素
def traverse_all_elements(params):
    print('开始测试...........')
    params.goIntoPage()
    sleep(5)
    e1 = params.driver.find_elements_by_xpath('//*')
    print("当前页面共有：" + str(len(e1)) + " 元素")
    print(params.driver.current_activity)
    traverseEles(params, e1)


# 执行元素的遍历点击测试，针对可点击元素
def traverseEles(params, e1):
    # 进入要测试的页面
    for i in range(params.currentEleIndex, len(e1)):
        try:
            e1[i].get_attribute("clickable")  # 如果元素不存在，则进入except代码块
            if (e1[i].get_attribute("clickable") == "true"):
                print("这是第：" + str(i) + " 个元素 ; 元素文本为：" + str(e1[i].text))
                print("元素的resource-id为:" + str(e1[i].get_attribute("resourceId")))
                reLanchAppRule(params)
                params.lastEleIndex = i
                params.currentEleIndex = i
                e1[i].click()
                sleep(1)
                backToLastPage(params)
                sleep(1)
            else:
                params.lastEleIndex = i
                params.currentEleIndex = i
                print("跳过第：" + str(i) + " 个元素")
        except:
            print("跳过第：" + str(i) + " 个元素" + "----获取该元素失败...")
            params.lastEleIndex = i
            params.currentEleIndex = i
            params.currentEleIndex = params.currentEleIndex + 1
            params.driver.launch_app()
            print("lanch app")
            traverseEles(params, e1)
            break


# 重启被测试应用
def reLanchAppRule(params):
    curActivity = params.driver.current_activity
    activity = params.testActivity
    if (curActivity != activity):
        print(curActivity)
        print("不是被测试 activity")
        print("lanch app")
        params.driver.launch_app()
        params.goIntoPage()


# 如果不是被测试activity，则点击返回键
def backToLastPage(params):
    activity = params.driver.current_activity  # 获取当前Activity
    theActivity = params.testActivity
    if (activity != theActivity):  # 设置页面
        params.driver.keyevent('4')
        if (activity == params.driver.current_activity):
            sleep(0.5)
            params.driver.keyevent('4')






