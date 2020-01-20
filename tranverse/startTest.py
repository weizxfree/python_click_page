# coding:utf-8
# Edit by liyuanhong 2016/10/17#
import sys

# 执行完所有用例所消耗的时间
from tranverse import TraverseTestMainPage

totalTime = 0
# 执行完单条用例所消耗的时间
singleTime = 0


def start():
    TraverseTestMainPage.suite("0")
