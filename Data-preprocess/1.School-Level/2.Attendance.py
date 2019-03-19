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
data_origin['date-time'] = data_origin['DataDateTime'].str.split('/', expand=True)[2]
data_origin['date'] = data_origin['date-time'].str.split(' ', expand=True)[0]
# print(data_origin['year'], data_origin['month'])

# 通过年月对于数据集重新排序，然后缺失值直接引用上一个即可
data_origin = data_origin.sort_values(by=['year', 'month'], ascending=[True, True])
print(data_origin)
for i in range(data_origin.shape[0]):
    if pd.isnull(data_origin['qj_term'].iloc[i]) == True:
        data_origin['qj_term'].iloc[i] = data_origin["qj_term"].iloc[i-1]

print(len(data_origin['qj_term'][pd.isnull(data_origin['qj_term'])]))
# 已经完成学期的缺失数据的补充
data_origin.to_csv("data_origin.csv")
'''

##############################################################################
# Step2: 以各个学年为单位，对数据进行划分，并进行统计
# 学期跨度为2013-2014-1，到2018-2019-1
##############################################################################

term = ["2013-2014-1", "2013-2014-2", "2014-2015-1", "2014-2015-2", "2015-2016-1", "2015-2016-2", "2016-2017-1",
        "2016-2017-2", "2017-2018-1", "2017-2018-2", "2018-2019-1"]

year = [2014, 2015, 2016, 2017, 2018, 2019]

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

control_task = [100000, 100100, 100200, 100300, 200000, 200100, 200200, 300000, 300100, 300200,
                9900100, 9900200, 9900300, 9900400, 9900500]

control_task_name = ['默认信息', '早上迟到', '晚到学校', '晚自修迟到', '默认信息', '校徽校服', '请假离校', '默认信息',
                     '住宿早晨锻炼', '课间操请假', '默认信息', '默认信息', '默认信息', '离校考勤', '进校考勤']
# 统计各个学期的特殊情况

# for i in range(len(term)):
#     for j in range(len(control_task)):
#         num_attendance = 0
#         for k in range(data_origin.shape[0]):
#             if data_origin['qj_term'].iloc[k] == term[i]:
#                 if data_origin['control_task_order_id'].iloc[k] == control_task[j]:
#                     num_attendance += 1
#         print("学期", term[i], control_task_name[j], "人数为", num_attendance)

##############################################################################
# Step3: 以各个学期为单位，对数据进行划分，并进行统计
# 学期跨度为2013-2014-1，到2018-2019-1

print(data_origin['year'])

for i in range(len(year)):
    num_statistic = 0
    for j in range(data_origin.shape[0]):
        if data_origin['year'].iloc[j] == year[i]:
            if data_origin['control_task_order_id'].iloc[j] == 200100:
                num_statistic += 1
    print("学年", year[i], "校服校徽人数为", num_statistic)
