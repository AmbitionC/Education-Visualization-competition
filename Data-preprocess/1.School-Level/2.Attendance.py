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

# 首先统计学年内数据的数量
for i in range(len(year)):
    num_students = 0
    for j in range(data_origin.shape[0]):
        if data_origin['year'].iloc[j] == year[i]:
            num_students += 1
    print("学年", year[i], "登记次数为", num_students)

print("\b")

# 学年 2014 登记次数为 10119（实际为1657条，其中8462条数据为体育场登记数据，其他年份没有）
# 学年 2015 登记次数为 1749
# 学年 2016 登记次数为 1364
# 学年 2017 登记次数为 2037
# 学年 2018 登记次数为 7577（实际为2329条，其中5248条为离校进校登记）
# 学年 2019 登记次数为 784
# 登记的次数不一样，所以要考虑是否进行归一化处理或者是计算比例



# 字段解释：
# 100000  正常时间到校，上课时间为7:25
# 100100  早晨上学迟到，在上课时间迟到一点
# 100200  晚到，白天的时间段都有，离上学时间差距很大
#### 100300  晚自习迟到，该类型没有一例登记
#### 200000  该类型没有一例登记
# 200100  校徽校服，预计是没有穿着校服
# 200200  早退，也就是早退数据
# 300000  操场默认登记数据
# 300100  住宿生早上锻炼记录
# 300200  课间操请假
# 9900100  迟到登记数据，用于几年后，可能设备进行更新了
# 9900200  校徽校服数据
# 9900300  早退数据
# 9900400  离校数据，推测属于正常离校数据
# 9900500  进校数据，推测为正常进校数据



# 需要进行统计展示的信息：
# 早上迟到： 100100 + 9900100 + 100200
# 请假离校（早退）： 200200 + 9900300
# 校徽校服问题： 200100 + 9900200
# 课间操请假：  300200

# 早上迟到进行比较的数据： 100100 + 9900100 + 100200 + 100000


# 记录迟到登记次数
for i in range(len(year)):
    num_statistic = 0
    for j in range(data_origin.shape[0]):
        if data_origin['year'].iloc[j] == year[i]:
            # if (data_origin['control_task_order_id'].iloc[j] == 100100) or (data_origin['control_task_order_id'].iloc[j] == 9900100) or (data_origin['control_task_order_id'].iloc[j] == 100200):
            # if (data_origin['control_task_order_id'].iloc[j] == 200200) or (data_origin['control_task_order_id'].iloc[j] == 9900300) :
            # if (data_origin['control_task_order_id'].iloc[j] == 200100) or (data_origin['control_task_order_id'].iloc[j] == 9900200) :
            # if (data_origin['control_task_order_id'].iloc[j] == 300100):
            if (data_origin['control_task_order_id'].iloc[j] == 9900200):
                num_statistic += 1
    print("学年", year[i], "住宿早晨锻炼次数为", num_statistic)
'''
学年 2014 迟到晚到次数为 959
学年 2015 迟到晚到次数为 1023
学年 2016 迟到晚到次数为 765
学年 2017 迟到晚到次数为 665
学年 2018 迟到晚到次数为 888
学年 2019 迟到晚到次数为 111

学年 2014 请假离校次数为 59
学年 2015 请假离校次数为 87
学年 2016 请假离校次数为 224
学年 2017 请假离校次数为 1150
学年 2018 请假离校次数为 477
学年 2019 请假离校次数为 0

学年 2014 校徽校服问题次数为 527
学年 2015 校徽校服问题次数为 568
学年 2016 校徽校服问题次数为 375
学年 2017 校徽校服问题次数为 222
学年 2018 校徽校服问题次数为 964
学年 2019 校徽校服问题次数为 39

学年 2014 课间操请假次数为 2400
学年 2015 课间操请假次数为 0
学年 2016 课间操请假次数为 0
学年 2017 课间操请假次数为 0
学年 2018 课间操请假次数为 0
学年 2019 课间操请假次数为 0

学年 2014 住宿早晨锻炼次数为 6062
学年 2015 住宿早晨锻炼次数为 0
学年 2016 住宿早晨锻炼次数为 0
学年 2017 住宿早晨锻炼次数为 0
学年 2018 住宿早晨锻炼次数为 0
学年 2019 住宿早晨锻炼次数为 0

'''
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

