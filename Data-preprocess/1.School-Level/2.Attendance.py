#-*- coding:utf-8 -*-

'''
# Author: chenhao
# Date: March. 12
# Description: Data-process for Education visualization competition
'''

##############################################################################
#Part2：统计学校范围内学生的考勤情况
##############################################################################

import pandas as pd
import datetime

data_origin = pd.read_csv("../1.School-Level-data/data_origin.csv")
##############################################################################
# Step1: 实现数据集学期数据的补齐
# 从Excel中观察，不可以直接进行补齐
# 为保证运行效率，该部分需要单独运行
##############################################################################
'''
# 导入数据集
data_origin = pd.read_csv('../../education_data/3_kaoqin.csv')


# 统计学期一栏数据缺失的数量
num_term_null = len(data_origin['qj_term'][pd.isnull(data_origin['qj_term'])])
print("学期栏缺失数量为：", num_term_null)
# 缺失的数量为947

# 首先获得DataDateTime数据，并将其分隔，获取他们的年、月

data_origin['year'] = data_origin['DataDateTime'].str.split('/', expand=True)[0]
data_origin['month'] = data_origin['DataDateTime'].str.split('/', expand=True)[1]
# print(data_origin['year'], data_origin['month'])

# 通过年月对于数据集重新排序，然后缺失值直接引用上一个即可
data_origin = data_origin.sort_values(by=['year', 'month'], ascending=[True, True])
print(data_origin)
for i in range(data_origin.shape[0]):
    if pd.isnull(data_origin['qj_term'].iloc[i]) == True:
        data_origin['qj_term'].iloc[i] = data_origin["qj_term"].iloc[i-1]

print(len(data_origin['qj_term'][pd.isnull(data_origin['qj_term'])]))
# 已经完成学期的缺失数据的补充
# data_origin.to_csv("data_origin.csv")
'''

##############################################################################
# Step2: 以各个学期为单位，对数据进行划分，并进行统计
# 学期跨度为2013-2014-1，到2018-2019-1

term = ["2013-2014-1", "2013-2014-2", "2014-2015-1", "2014-2015-2", "2015-2016-1", "2015-2016-2", "2016-2017-1",
        "2016-2017-2", "2017-2018-1", "2017-2018-2", "2018-2019-1", ]

# 统计各个学期的特殊情况
# 100100-早上迟到，100200-晚到学校，100300-晚自修迟到
# 100

#
# for j in range(len(term)):
#     morning_late = 0
#     for i in range(data_origin.shape[0]):
#         if data_origin['qj_term'].iloc[i] == term[j]:
#             if data_origin['control_task_order_id'].iloc[i] == 100100:
#                 morning_late += 1
#     print("学期", term[j], "早上迟到人数为", morning_late)

for j in range(len(term)):
    morning_late = 0
    for i in range(data_origin.shape[0]):
        if data_origin['qj_term'].iloc[i] == term[j]:
            if data_origin['control_task_order_id'].iloc[i] == 100200:
                morning_late += 1
    print("学期", term[j], "晚自习迟到人数为", morning_late)