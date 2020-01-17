# -*- coding: UTF-8 -*-
import os
import json

from ExcelOutPut import insert2Excel

text_str = ''
judg_list = []

dir = "/Users/zhangxiangwei/PycharmProjects/HelloWorld/log/"


def findJson(file_path):
    file_path = os.path.dirname(dir) + "/" + file_path
    with open(file_path) as f:
        split_str = f.readlines()
    global text_str
    for i in split_str:
        text_str += i
    text_str = text_str.replace("\n", "")
    text_str = text_str.replace("\r", "")
    f.close()

    json_char = []
    count = 0
    str_list = text_str
    for each_char in str_list:
        count += 1
        if each_char == "{" or each_char == "}":
            json_char.append(count - 1)
    return (json_char)


def getJsonValue(json_char):
    '''
    :param json_char:
    :return: 提取文件中所有的json格式的字符串
    '''
    s = json_char
    left_char = 0
    right_char = 0
    json_end = 0
    json_match = []
    left_count = 0
    json_value = []
    for i in range(len(s)):
        tmp_list = []
        left_count += 1
        if "{" in json_match and "}" in json_match and (left_char == right_char):
            # print(json_match[i],":",s[len(json_match)],json_match[-1])
            # print("yes json match success")
            json_end += len(json_match)
            # print("json_end:",(json_end+1))
            json_match = []
            if i == len(s):
                break
            else:
                if text_str[s[i]] == "{":
                    left_char += 1
                elif text_str[s[i]] == "}":
                    right_char += 1
                # print(s[i], ":", text_str[s[i]])
                json_match.append(text_str[s[i]])
        else:
            if text_str[s[i]] == "{":
                left_char += 1
            elif text_str[s[i]] == "}":
                right_char += 1
            # print(s[i],":",text_str[s[i]])
            json_match.append(text_str[s[i]])
            # print("text_str:",json_match)
            if "{" in json_match and "}" in json_match and (left_char == right_char):
                # print(json_match[0], json_match[-1])
                # print("yes json match success")
                json_start = json_end
                json_end += len(json_match)
                tmp_list.append(json_start)
                tmp_list.append(json_end - 1)
                # print("json_start:",json_start,"json_end:", json_end-1)
                json_match = []
                json_value.append(tmp_list)
            # print("OK")
    # print(json_value)
    finnal_json = []
    for i in json_value:
        # print("str_start:%s-----str_end:%s"%(s[i[0]],s[i[1]]+1))
        str_value = text_str[s[i[0]]:s[i[1]] + 1]
        # print("str_value:",str_value)
        try:

            dict_str = json.loads(str_value)
            # print(dict_str,type(dict_str))
            finnal_json.append(dict_str)

        except:
            print("格式不是未json：%s" % str_value)

    return finnal_json


def judgJsonKey(json_value):
    for json_content in json_value:
        print("josn_content:", json_content)
        for i in json_content:
            if i == "$element_selector" or i == "$element_content" or i == "$element_type" or i == "$screen_name":
                if json_content[i] == None or json_content[i] == '' or json_content[i] == 'None':
                    pass
                else:
                    judg_list.append(json_content)
                    break
            elif isinstance(json_content[i], dict):
                # print("is second json %s"%i)
                for y in json_content[i]:
                    # print(y)
                    if y == "$element_selector" or i == "$element_content" or i == "$element_type" or i == "$screen_name":
                        # print(json_content[i][y])
                        if json_content[i][y] == None or json_content[i][y] == '' or json_content[i][y] == 'None':
                            pass
                        else:
                            # print(" second else json_content[%s]:" % i,json_content[i][y])
                            judg_list.append(json_content)
                            break

    return judg_list


def parseJsonTest(file_path):
    s = findJson(file_path)
    return judgJsonKey(getJsonValue(s))


def parseJson():
    dirs = os.listdir(dir)
    for file in dirs:
        array = parseJsonTest(file)
        print(array)
        insert2Excel(array)


