#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1、导入模块
import xlwt
# 2、创建workbook（其实就是excel，后来保存一下就行）
workbook = xlwt.Workbook(encoding = 'utf-8')
# 3、创建表
worksheet=workbook.add_sheet('my sheet')
# 4、往单元格内写入内容
worksheet.write(1, 0, label = 'Row 0, Column 0 Value')
# 5、保存
workbook.save('work.xls')