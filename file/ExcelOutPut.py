# -*- coding: UTF-8 -*-
import time

import xlsxwriter


def insert2Excel(jsonArray):
    workbook = xlsxwriter.Workbook('/Test.xlsx')  # 创建一个Excel文件
    worksheet = workbook.add_worksheet()  # 创建一个sheet
    title = [U'$screen_name', U'$element_selector', U'$element_type', U'$element_content']  # 表格title
    worksheet.write_row('A1', title)  # title 写入Excel
    length = len(jsonArray)
    if length == 0:
        return

    for i in range(0, len(jsonArray)):
        map = jsonArray[i]
        num0 = i + 2
        screen_name = str(map['properties']['$screen_name'])
        element_selector = str(map['properties']['$element_selector'])
        element_type = str(map['properties']['$element_type'])
        element_content = str(map['properties']['$element_content'])
        row = 'A' + str(num0)
        data = [screen_name, element_selector, element_type, element_content]
        print("write_row")
        worksheet.write_row(row, data)

    workbook.close()
