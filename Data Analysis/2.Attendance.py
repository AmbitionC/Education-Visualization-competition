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
import numpy as np
import datetime
import json
import math

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
data_origin.to_csv("data_origin.csv", encoding='utf_8_sig')
print('保存成功！')
'''

##############################################################################
# Step2: 以各个学年为单位，对数据进行划分，并进行统计
# 学期跨度为2013-2014-1，到2018-2019-1
##############################################################################

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
# 课间操请假：  300200（只能统计2014年信息）


term = ["2013-2014-1", "2013-2014-2", "2014-2015-1", "2014-2015-2", "2015-2016-1", "2015-2016-2", "2016-2017-1",
        "2016-2017-2", "2017-2018-1", "2017-2018-2", "2018-2019-1"]

year = [2014, 2015, 2016, 2017, 2018, 2019]

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

control_task = [100000, 100100, 100200, 100300, 200000, 200100, 200200, 300000, 300100, 300200,
                9900100, 9900200, 9900300, 9900400, 9900500]

control_task_name = ['默认信息', '早上迟到', '晚到学校', '晚自修迟到', '默认信息', '校徽校服', '请假离校', '默认信息',
                     '住宿早晨锻炼', '课间操请假', '默认信息', '默认信息', '默认信息', '离校考勤', '进校考勤']

# 统计各个学年的数据数量
def statistic_year_num():
    for i in range(len(year)):
        num_students = 0
        for j in range(data_origin.shape[0]):
            if data_origin['year'].iloc[j] == year[i]:
                num_students += 1
        print("学年", year[i], "数据量为", num_students)
    print('\b')

# 学年 2014 数据量为 10119
# 学年 2015 数据量为 1749
# 学年 2016 数据量为 1364
# 学年 2017 数据量为 2037
# 学年 2018 数据量为 7577
# 学年 2019 数据量为 784

# 统计各年的操场打卡数据的数量
def statisitic_year_playground():
    num_playground = [0, 0, 0, 0, 0, 0]
    # 统计各年操场打卡事件
    for i in range(len(year)):
        for j in range(data_origin.shape[0]):
            if data_origin['year'].iloc[j] == year[i]:
                # if (data_origin['control_task_order_id'].iloc[j] == 300000):
                # if (data_origin['control_task_order_id'].iloc[j] == 300100):
                if (data_origin['control_task_order_id'].iloc[j] == 300200):
                    num_playground[i] += 1
        print("学年", year[i], "课间操请假数据量为", num_playground[i])
    print('\b')

# 操场打卡数据只有2014年才有
# 300000为操场默认登记数据  96人
# 300100为住宿生早上锻炼数据   6062
# 300200为课间操请假数据   2400
# 2014年比其他年份多的数据为   8558

def statisitic_year_inandout():
    num_inandout = [0, 0, 0, 0, 0, 0]
    for i in range(len(year)):
        for j in range(data_origin.shape[0]):
            if data_origin['year'].iloc[j] == year[i]:
                if (data_origin['control_task_order_id'].iloc[j] == 9900400) or (data_origin['control_task_order_id'].iloc[j] == 9900500):
                    num_inandout[i] += 1
        print("学年", year[i], "进出校数据量为", num_inandout[i])
    print('\b')
# 学年 2014 进出校数据量为 0
# 学年 2015 进出校数据量为 0
# 学年 2016 进出校数据量为 0
# 学年 2017 进出校数据量为 0
# 学年 2018 进出校数据量为 5248
# 学年 2019 进出校数据量为 634


# 学年 2014 登记次数为 1561（总共为10119条，其中8558条数据为体育场登记数据，其他年份没有）
# 学年 2015 登记次数为 1749
# 学年 2016 登记次数为 1364
# 学年 2017 登记次数为 2037
# 学年 2018 登记次数为 2329（总共为7577条，其中5248条为离校进校登记）
# 学年 2019 登记次数为 150（总共为784条，其中634条为进校离校登记）
# 登记的次数不一样，所以要考虑是否进行归一化处理或者是计算比例
year_students = [1561, 1749, 1364, 2037, 2329, 150]
year_name = ['2014年', '2015年', '2016年', '2017年', '2018年', '2019年']


def statistic_year_late():
    num_late = [0, 0, 0, 0, 0, 0]
    year_name = ['2014年', '2015年', '2016年', '2017年', '2018年', '2019年']
    data_show_all = []
    # 记录迟到晚到比例
    for i in range(len(year)):
        for j in range(data_origin.shape[0]):
            if data_origin['year'].iloc[j] == year[i]:
                if (data_origin['control_task_order_id'].iloc[j] == 100100) or (data_origin['control_task_order_id'].iloc[j] == 9900100) or (data_origin['control_task_order_id'].iloc[j] == 100200):
                    num_late[i] += 1
        num_late[i] = round(num_late[i] / year_students[i] * 100, 2)
        # print("学年", year[i], "迟到晚到的比例为", num_late[i], "%")
        data_show = [year_name[i], round(num_late[i]/2, 2)]
        data_show_all.append(data_show)
    print(data_show_all)
    print("\b")
    return data_show_all

def statistic_year_early():
    num_early = [0, 0, 0, 0, 0, 0]
    year_name = ['2014年', '2015年', '2016年', '2017年', '2018年', '2019年']
    data_show_all = []
    # 记录早退离校比例
    for i in range(len(year)):
        for j in range(data_origin.shape[0]):
            if data_origin['year'].iloc[j] == year[i]:
                if (data_origin['control_task_order_id'].iloc[j] == 200200) or (data_origin['control_task_order_id'].iloc[j] == 9900300) :
                    num_early[i] += 1
        num_early[i] = round(num_early[i] / year_students[i] * 100, 2)
        data_show = [year_name[i], round(num_early[i]/2, 2)]
        data_show_all.append(data_show)
        # print("学年", year[i], "早退离校的比例为", num_early[i], "%")
    print(data_show_all)
    print("\b")
    return data_show_all


def statistic_year_uniform():
    num_uniform = [0, 0, 0, 0, 0, 0]
    year_name = ['2014年', '2015年', '2016年', '2017年', '2018年', '2019年']
    data_show_all = []
    # 记录校服校徽问题比例
    for i in range(len(year)):
        for j in range(data_origin.shape[0]):
            if data_origin['year'].iloc[j] == year[i]:
                if (data_origin['control_task_order_id'].iloc[j] == 200100) or (data_origin['control_task_order_id'].iloc[j] == 9900200) :
                    num_uniform[i] += 1
        num_uniform[i] = round(num_uniform[i] / year_students[i] * 100, 2)
        data_show = [year_name[i], round(num_uniform[i]/2, 2)]
        data_show_all.append(data_show)
        # print("学年", year[i], "校服校徽问题比例为", num_uniform[i], "%")
    print(data_show_all)
    print("\b")
    return data_show_all

def statistic_year_exercise():
    num_exercise = [0, 0, 0, 0, 0, 0]
    # 记录课间操请假的比例
    for i in range(len(year)):
        for j in range(data_origin.shape[0]):
            if data_origin['year'].iloc[j] == year[i]:
                if (data_origin['control_task_order_id'].iloc[j] == 300200):
                    num_exercise[i] += 1
        num_exercise[i] = round(num_exercise[i] / year_students[i] * 100, 2)
        print("学年", year[i], "课间操请假比例为", num_exercise[i], "%")
    print("\b")

# statistic_year_late()
# statistic_year_early()
# statistic_year_uniform()
'''
学年 2014 迟到晚到的比例为 61.43 %
学年 2015 迟到晚到的比例为 58.49 %
学年 2016 迟到晚到的比例为 56.09 %
学年 2017 迟到晚到的比例为 32.65 %
学年 2018 迟到晚到的比例为 38.13 %
学年 2019 迟到晚到的比例为 74.0 %


学年 2014 早退离校的比例为 3.78 %
学年 2015 早退离校的比例为 4.97 %
学年 2016 早退离校的比例为 16.42 %
学年 2017 早退离校的比例为 56.46 %
学年 2018 早退离校的比例为 20.48 %
学年 2019 早退离校的比例为 0.0 %


学年 2014 校服校徽问题比例为 33.76 %
学年 2015 校服校徽问题比例为 32.48 %
学年 2016 校服校徽问题比例为 27.49 %
学年 2017 校服校徽问题比例为 10.9 %
学年 2018 校服校徽问题比例为 41.39 %
学年 2019 校服校徽问题比例为 26.0 %
'''

##############################################################################
# Step3: 以各个学期为单位，对数据进行划分，并进行统计
# 学期跨度为2013-2014-1，到2018-2019-1
##############################################################################
# 统计各个学期的数据数量
def statistic_term_num():
    for i in range(len(term)):
        num_students = 0
        for j in range(data_origin.shape[0]):
            if data_origin['qj_term'].iloc[j] == term[i]:
                num_students += 1
        print("学期", term[i], "数据量为", num_students)
    print('\b')

# 学期 2013-2014-1 数据量为 2738
# 学期 2013-2014-2 数据量为 6949
# 学期 2014-2015-1 数据量为 611
# 学期 2014-2015-2 数据量为 1021
# 学期 2015-2016-1 数据量为 644
# 学期 2015-2016-2 数据量为 415
# 学期 2016-2017-1 数据量为 965
# 学期 2016-2017-2 数据量为 798
# 学期 2017-2018-1 数据量为 2307
# 学期 2017-2018-2 数据量为 2709
# 学期 2018-2019-1 数据量为 4473

# 统计各个学期的运动场打开数量

# 统计各学期的操场打卡数据的数量
def statisitic_term_playground():
    num_playground = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # 统计各学期操场打卡事件
    for i in range(len(term)):
        for j in range(data_origin.shape[0]):
            if data_origin['qj_term'].iloc[j] == term[i]:
                if (data_origin['control_task_order_id'].iloc[j] == 300200):
                # if (data_origin['control_task_order_id'].iloc[j] == 300100):
                # if (data_origin['control_task_order_id'].iloc[j] == 300200):
                    num_playground[i] += 1
        print("学期", term[i], "操场默认登记为", num_playground[i])
    print('\b')

# 操场打卡数据只有2014年才有
# 2013-2014-1:
# 300000为操场默认登记数据  96
# 300100为住宿生早上锻炼数据   1501
# 300200为课间操请假数据   877
# 2013-2014-1多出的数据量为   2474

# 2013-2014-2:
# 300000为操场默认登记数据  0
# 300100为住宿生早上锻炼数据   4561
# 300200为课间操请假数据   1523
# 2013-2014-2多出的数据量为   6084

# 统计各个学期的进校离校的数量
def statistic_term_inandout():
    num_inandout = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(term)):
        for j in range(data_origin.shape[0]):
            if data_origin['qj_term'].iloc[j] == term[i]:
                if (data_origin['control_task_order_id'].iloc[j] == 9900400) or (data_origin['control_task_order_id'].iloc[j] == 9900500):
                    num_inandout[i] += 1
        print("学期", term[i], "进出校园登记为", num_inandout[i])
    print('\b')

# 学期 2013-2014-1 进出校园登记为 0
# 学期 2013-2014-2 进出校园登记为 0
# 学期 2014-2015-1 进出校园登记为 0
# 学期 2014-2015-2 进出校园登记为 0
# 学期 2015-2016-1 进出校园登记为 0
# 学期 2015-2016-2 进出校园登记为 0
# 学期 2016-2017-1 进出校园登记为 0
# 学期 2016-2017-2 进出校园登记为 0
# 学期 2017-2018-1 进出校园登记为 0
# 学期 2017-2018-2 进出校园登记为 2082
# 学期 2018-2019-1 进出校园登记为 3800

# 学期 2013-2014-1 数据量为 309（2783-2474）
# 学期 2013-2014-2 数据量为 865（6949-6084）
# 学期 2014-2015-1 数据量为 611
# 学期 2014-2015-2 数据量为 1021
# 学期 2015-2016-1 数据量为 644
# 学期 2015-2016-2 数据量为 415
# 学期 2016-2017-1 数据量为 965
# 学期 2016-2017-2 数据量为 798
# 学期 2017-2018-1 数据量为 2307
# 学期 2017-2018-2 数据量为 627（2709-2082）
# 学期 2018-2019-1 数据量为 673（4473-3800）

term_students = [309, 865, 611, 1021, 644, 415, 965, 798, 2307, 627, 673]
term_name = ["2013-2014-1", "2013-2014-2", "2014-2015-1", "2014-2015-2", "2015-2016-1", "2015-2016-2", "2016-2017-1",
            "2016-2017-2", "2017-2018-1", "2017-2018-2", "2018-2019-1"]

def statistic_term_late():
    num_late = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    term_name = ["2013-2014-1", "2013-2014-2", "2014-2015-1", "2014-2015-2", "2015-2016-1", "2015-2016-2", "2016-2017-1",
            "2016-2017-2", "2017-2018-1", "2017-2018-2", "2018-2019-1"]
    data_show_all = []
    # 记录迟到晚到比例
    for i in range(len(term)):
        for j in range(data_origin.shape[0]):
            if data_origin['qj_term'].iloc[j] == term[i]:
                if (data_origin['control_task_order_id'].iloc[j] == 100100) or (data_origin['control_task_order_id'].iloc[j] == 9900100) or (data_origin['control_task_order_id'].iloc[j] == 100200):
                    num_late[i] += 1
        num_late[i] = round(num_late[i] / term_students[i] * 100, 2)
        data_show = [term_name[i], round(num_late[i]/2, 2)]
        data_show_all.append(data_show)
        # print("学期", term[i], "迟到晚到的比例为", num_late[i], "%")
    print(data_show_all)
    print("\b")
    return data_show_all


def statistic_term_early():
    num_early = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    term_name = ["2013-2014-1", "2013-2014-2", "2014-2015-1", "2014-2015-2", "2015-2016-1", "2015-2016-2",
                 "2016-2017-1",
                 "2016-2017-2", "2017-2018-1", "2017-2018-2", "2018-2019-1"]
    data_show_all = []
    # 记录早退离校比例
    for i in range(len(term)):
        for j in range(data_origin.shape[0]):
            if data_origin['qj_term'].iloc[j] == term[i]:
                if (data_origin['control_task_order_id'].iloc[j] == 200200) or (data_origin['control_task_order_id'].iloc[j] == 9900300) :
                    num_early[i] += 1
        num_early[i] = round(num_early[i] / term_students[i] * 100, 2)
        data_show = [term_name[i], round(num_early[i]/2, 2)]
        data_show_all.append(data_show)
        # print("学期", term[i], "早退离校的比例为", num_early[i], "%")
    print(data_show_all)
    print("\b")
    return data_show_all


def statistic_term_uniform():
    num_uniform = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    term_name = ["2013-2014-1", "2013-2014-2", "2014-2015-1", "2014-2015-2", "2015-2016-1", "2015-2016-2",
                 "2016-2017-1",
                 "2016-2017-2", "2017-2018-1", "2017-2018-2", "2018-2019-1"]
    data_show_all = []
    # 记录校服校徽问题比例
    for i in range(len(term)):
        for j in range(data_origin.shape[0]):
            if data_origin['qj_term'].iloc[j] == term[i]:
                if (data_origin['control_task_order_id'].iloc[j] == 200100) or (data_origin['control_task_order_id'].iloc[j] == 9900200) :
                    num_uniform[i] += 1
        num_uniform[i] = round(num_uniform[i] / term_students[i] * 100, 2)
        data_show = [term_name[i], round(num_uniform[i]/2, 2)]
        data_show_all.append(data_show)
        # print("学期", term[i], "校服校徽问题比例为", num_uniform[i], "%")
    print(data_show_all)
    print("\b")
    return data_show_all


# statistic_term_late()
# statistic_term_early()
# statistic_term_uniform()
'''
学期 2013-2014-1 迟到晚到的比例为 91.26 %
学期 2013-2014-2 迟到晚到的比例为 48.32 %
学期 2014-2015-1 迟到晚到的比例为 64.65 %
学期 2014-2015-2 迟到晚到的比例为 55.83 %
学期 2015-2016-1 迟到晚到的比例为 61.34 %
学期 2015-2016-2 迟到晚到的比例为 72.77 %
学期 2016-2017-1 迟到晚到的比例为 45.08 %
学期 2016-2017-2 迟到晚到的比例为 28.82 %
学期 2017-2018-1 迟到晚到的比例为 23.54 %
学期 2017-2018-2 迟到晚到的比例为 66.99 %
学期 2018-2019-1 迟到晚到的比例为 62.56 %


学期 2013-2014-1 早退离校的比例为 3.88 %
学期 2013-2014-2 早退离校的比例为 4.97 %
学期 2014-2015-1 早退离校的比例为 1.15 %
学期 2014-2015-2 早退离校的比例为 7.25 %
学期 2015-2016-1 早退离校的比例为 1.55 %
学期 2015-2016-2 早退离校的比例为 1.45 %
学期 2016-2017-1 早退离校的比例为 27.05 %
学期 2016-2017-2 早退离校的比例为 58.02 %
学期 2017-2018-1 早退离校的比例为 45.17 %
学期 2017-2018-2 早退离校的比例为 12.6 %
学期 2018-2019-1 早退离校的比例为 0.0 %


学期 2013-2014-1 校服校徽问题比例为 21.04 %
学期 2013-2014-2 校服校徽问题比例为 34.1 %
学期 2014-2015-1 校服校徽问题比例为 33.88 %
学期 2014-2015-2 校服校徽问题比例为 29.97 %
学期 2015-2016-1 校服校徽问题比例为 37.11 %
学期 2015-2016-2 校服校徽问题比例为 25.78 %
学期 2016-2017-1 校服校徽问题比例为 27.88 %
学期 2016-2017-2 校服校徽问题比例为 13.16 %
学期 2017-2018-1 校服校徽问题比例为 31.3 %
学期 2017-2018-2 校服校徽问题比例为 20.41 %
学期 2018-2019-1 校服校徽问题比例为 37.44 %
'''

##############################################################################
# Step4: 以各个月份为单位，对数据进行划分，并进行统计
# 学期跨度为2018年的1月，到2018年的12月
##############################################################################

# 首先提取2018年年份的数据
data_year = data_origin.drop(data_origin[data_origin['year'] < 2018].index)
data_year = data_year.drop(data_year[data_year['year'] > 2018].index)

# 统计每个月的数据数量
def statistic_month_num():
    for i in range(len(month)):
        num_students = 0
        for j in range(data_year.shape[0]):
            if data_year['month'].iloc[j] == month[i]:
                num_students += 1
        print(month[i], "月", "数据量为", num_students)
    print('\b')

# 1 月 数据量为 1176
# 2 月 数据量为 27
# 3 月 数据量为 155
# 4 月 数据量为 403
# 5 月 数据量为 1035
# 6 月 数据量为 951
# 7 月 数据量为 141
# 8 月 数据量为 0
# 9 月 数据量为 927
# 10 月 数据量为 1019
# 11 月 数据量为 705
# 12 月 数据量为 1038

# 统计各个月份的进校离校的数量
def statistic_month_inandout():
    num_inandout = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(month)):
        for j in range(data_year.shape[0]):
            if data_year['month'].iloc[j] == month[i]:
                if (data_year['control_task_order_id'].iloc[j] == 9900400) or (data_year['control_task_order_id'].iloc[j] == 9900500):
                    num_inandout[i] += 1
        print(month[i], "月进出校园数据量为", num_inandout[i])
    print('\b')

# 1 月进出校园数据量为 0
# 2 月进出校园数据量为 0
# 3 月进出校园数据量为 0
# 4 月进出校园数据量为 288
# 5 月进出校园数据量为 854
# 6 月进出校园数据量为 825
# 7 月进出校园数据量为 115
# 8 月进出校园数据量为 0
# 9 月进出校园数据量为 785
# 10 月进出校园数据量为 938
# 11 月进出校园数据量为 606
# 12 月进出校园数据量为 837

# 1 月 数据量为 1176
# 2 月 数据量为 27
# 3 月 数据量为 155
# 4 月 数据量为 115（403-288）
# 5 月 数据量为 181（1035-854）
# 6 月 数据量为 126（951-825）
# 7 月 数据量为 26（141-115）
# 8 月 数据量为 0
# 9 月 数据量为 142（927-785）
# 10 月 数据量为 81（1019-938）
# 11 月 数据量为 99（705-606）
# 12 月 数据量为 201（1038-837）

month_students = [1176, 27, 155, 115, 181, 126, 26, 1, 142, 81, 99, 201]
month_name = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]

# 统计12个月的考勤特殊情况
def statistic_month_late():
    num_late = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    month_name = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
    data_show_all = []
    for i in range(len(month)):
        for j in range(data_year.shape[0]):
            if data_year['month'].iloc[j] == month[i]:
                if (data_year['control_task_order_id'].iloc[j] == 100100) or (data_year['control_task_order_id'].iloc[j] == 9900100) or (data_year['control_task_order_id'].iloc[j] == 100200):
                    num_late[i] += 1
        num_late[i] = round(num_late[i] / month_students[i] * 100, 2)
        data_show = [month_name[i], round(num_late[i]/2, 2)]
        data_show_all.append(data_show)
        # print(month[i], "月迟到晚到的比例为", num_late[i], "%")
    print(data_show_all)
    print("\b")
    return data_show_all


def statistic_month_early():
    num_early = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    month_name = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
    data_show_all = []
    for i in range(len(month)):
        for j in range(data_year.shape[0]):
            if data_year['month'].iloc[j] == month[i]:
                if (data_year['control_task_order_id'].iloc[j] == 200200) or (data_year['control_task_order_id'].iloc[j] == 9900300):
                    num_early[i] += 1
        num_early[i] = round(num_early[i] / month_students[i] * 100, 2)
        data_show = [month_name[i], round(num_early[i]/2, 2)]
        data_show_all.append(data_show)
        # print(month[i], "月早退的比例为", num_early[i], "%")
    print(data_show_all)
    print("\b")
    return data_show_all


def statistic_month_uniform():
    num_uniform = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    month_name = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
    data_show_all = []
    for i in range(len(month)):
        for j in range(data_year.shape[0]):
            if data_year['month'].iloc[j] == month[i]:
                if (data_year['control_task_order_id'].iloc[j] == 200100) or (data_year['control_task_order_id'].iloc[j] == 9900200):
                    num_uniform[i] += 1
        num_uniform[i] = round(num_uniform[i] / month_students[i] * 100, 2)
        data_show = [month_name[i], round(num_uniform[i]/2, 2)]
        data_show_all.append(data_show)
        # print(month[i], "月校服校徽问题的比例为", num_uniform[i], "%")
    print(data_show_all)
    print("\b")
    return data_show_all


# statistic_month_late()
# statistic_month_early()
# statistic_month_uniform()

'''
对其中的一些过高的值需要做平均处理，因为有的月份样本数量太少
或者对这些数据进行差分，用百分比的话显然不妥（进行等比例缩放）
1 月迟到晚到的比例为 13.44 %
2 月迟到晚到的比例为 81.48 %
3 月迟到晚到的比例为 43.87 %
4 月迟到晚到的比例为 72.17 %
5 月迟到晚到的比例为 82.32 %
6 月迟到晚到的比例为 57.94 %
7 月迟到晚到的比例为 96.15 %
8 月迟到晚到的比例为 0.0 %
9 月迟到晚到的比例为 41.55 %
10 月迟到晚到的比例为 65.43 %
11 月迟到晚到的比例为 66.67 %
12 月迟到晚到的比例为 65.67 %


1 月早退的比例为 33.84 %
2 月早退的比例为 0.0 %
3 月早退的比例为 45.81 %
4 月早退的比例为 4.35 %
5 月早退的比例为 1.66 %
6 月早退的比例为 0.0 %
7 月早退的比例为 0.0 %
8 月早退的比例为 0.0 %
9 月早退的比例为 0.0 %
10 月早退的比例为 0.0 %
11 月早退的比例为 0.0 %
12 月早退的比例为 0.0 %


1 月校服校徽问题的比例为 52.72 %
2 月校服校徽问题的比例为 18.52 %
3 月校服校徽问题的比例为 10.32 %
4 月校服校徽问题的比例为 23.48 %
5 月校服校徽问题的比例为 16.02 %
6 月校服校徽问题的比例为 42.06 %
7 月校服校徽问题的比例为 3.85 %
8 月校服校徽问题的比例为 0.0 %
9 月校服校徽问题的比例为 58.45 %
10 月校服校徽问题的比例为 34.57 %
11 月校服校徽问题的比例为 33.33 %
12 月校服校徽问题的比例为 34.33 %
'''

##############################################################################
# Step5: 以每一天为单位，对数据进行划分，并进行统计
# 学期跨度为2018年的1月1日，到2018年的1月30日
##############################################################################


# 首先提取2018年年份的数据
data_day = data_origin.drop(data_origin[data_origin['year'] < 2018].index)
data_day = data_day.drop(data_day[data_day['year'] > 2018].index)
data_day = data_day.drop(data_day[data_day['month'] > 1].index)
# print(data_day.shape[0])

# 统计1月每一天的数据数量
def statistic_day_num():
    for i in range(len(date)):
        num_students = 0
        for j in range(data_day.shape[0]):
            if data_day['date'].iloc[j] == date[i]:
                num_students += 1
        print(date[i], "号", "数据量为", num_students)
    print('\b')

# statistic_day_num()

# 1 号 数据量为 0
# 2 号 数据量为 25
# 3 号 数据量为 17
# 4 号 数据量为 4
# 5 号 数据量为 16
# 6 号 数据量为 0
# 7 号 数据量为 0
# 8 号 数据量为 13
# 9 号 数据量为 8
# 10 号 数据量为 1
# 11 号 数据量为 3
# 12 号 数据量为 8
# 13 号 数据量为 0
# 14 号 数据量为 0
# 15 号 数据量为 54
# 16 号 数据量为 5
# 17 号 数据量为 31
# 18 号 数据量为 0
# 19 号 数据量为 0
# 20 号 数据量为 0
# 21 号 数据量为 0
# 22 号 数据量为 9
# 23 号 数据量为 22
# 24 号 数据量为 9
# 25 号 数据量为 365
# 26 号 数据量为 60
# 27 号 数据量为 433
# 28 号 数据量为 1
# 29 号 数据量为 92
# 30 号 数据量为 0
# 31 号 数据量为 0

date_students = [1, 25, 17, 4, 16, 1, 1, 13, 8, 1, 3, 8, 1, 1, 54, 5, 31, 1, 1, 1, 1, 9, 22, 9, 365, 60, 433, 1, 92, 1, 1]
date_name = ["1号", "2号", "3号", "4号", "5号", "6号", "7号", "8号", "9号", "10号", "11号", "12号", "13号", "14号", "15号", "16号",
             "17号", "18号", "19号", "20号", "21号", "22号", "23号", "24号", "25号", "26号", "27号", "28号", "29号", "30号", "31号"]


# 直接统计1月份每一天的数据情况
def statistic_day_late():
    num_late = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    date_name = ["1号", "2号", "3号", "4号", "5号", "6号", "7号", "8号", "9号", "10号", "11号", "12号", "13号", "14号", "15号", "16号", "17号", "18号", "19号", "20号", "21号", "22号", "23号", "24号", "25号", "26号", "27号", "28号", "29号", "30号", "31号"]
    data_show_all = []
    for i in range(len(date)):
        for j in range(data_day.shape[0]):
            if data_day['date'].iloc[j] == date[i]:
                if (data_day['control_task_order_id'].iloc[j] == 100100) or (data_day['control_task_order_id'].iloc[j] == 9900100) or (data_day['control_task_order_id'].iloc[j] == 100200):
                    num_late[i] += 1
        num_late[i] = round(num_late[i] / date_students[i] * 100, 2)
        data_show = [date_name[i], round(num_late[i]/2, 2)]
        data_show_all.append(data_show)
        # print(date[i], "号迟到晚到的数量为", num_late[i])
    print(data_show_all)
    print("\b")
    return data_show_all


def statistic_day_early():
    num_early = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    date_name = ["1号", "2号", "3号", "4号", "5号", "6号", "7号", "8号", "9号", "10号", "11号", "12号", "13号", "14号", "15号", "16号",
                 "17号", "18号", "19号", "20号", "21号", "22号", "23号", "24号", "25号", "26号", "27号", "28号", "29号", "30号",
                 "31号"]
    data_show_all = []
    for i in range(len(date)):
        for j in range(data_day.shape[0]):
            if data_day['date'].iloc[j] == date[i]:
                if (data_day['control_task_order_id'].iloc[j] == 200200) or (data_day['control_task_order_id'].iloc[j] == 9900300):
                    num_early[i] += 1
        num_early[i] = round(num_early[i] / date_students[i] * 100, 2)
        data_show = [date_name[i], round(num_early[i]/2, 2)]
        data_show_all.append(data_show)
        # print(date[i], "号早退的数量为", num_early[i])
    print(data_show_all)
    print("\b")
    return data_show_all


def statistic_day_uniform():
    num_uniform = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    date_name = ["1号", "2号", "3号", "4号", "5号", "6号", "7号", "8号", "9号", "10号", "11号", "12号", "13号", "14号", "15号", "16号",
                 "17号", "18号", "19号", "20号", "21号", "22号", "23号", "24号", "25号", "26号", "27号", "28号", "29号", "30号",
                 "31号"]
    data_show_all = []
    for i in range(len(date)):
        for j in range(data_day.shape[0]):
            if data_day['month'].iloc[j] == date[i]:
                if (data_day['control_task_order_id'].iloc[j] == 200100) or (data_day['control_task_order_id'].iloc[j] == 9900200):
                    num_uniform[i] += 1
        num_uniform[i] = round(num_uniform[i] / date_students[i] * 100, 2)
        data_show = [date_name[i], round(num_uniform[i]/2, 2)]
        data_show_all.append(data_show)
        # print(date[i], "号校服校徽问题的比例为", num_uniform[i])
    print(data_show_all)
    print("\b")
    return data_show_all


# statistic_day_late()
# statistic_day_early()
# statistic_day_uniform()

'''
1 号迟到晚到的数量为 0
2 号迟到晚到的数量为 15
3 号迟到晚到的数量为 16
4 号迟到晚到的数量为 1
5 号迟到晚到的数量为 10
6 号迟到晚到的数量为 0
7 号迟到晚到的数量为 0
8 号迟到晚到的数量为 13
9 号迟到晚到的数量为 6
10 号迟到晚到的数量为 1
11 号迟到晚到的数量为 3
12 号迟到晚到的数量为 7
13 号迟到晚到的数量为 0
14 号迟到晚到的数量为 0
15 号迟到晚到的数量为 4
16 号迟到晚到的数量为 1
17 号迟到晚到的数量为 4
18 号迟到晚到的数量为 0
19 号迟到晚到的数量为 0
20 号迟到晚到的数量为 0
21 号迟到晚到的数量为 0
22 号迟到晚到的数量为 9
23 号迟到晚到的数量为 17
24 号迟到晚到的数量为 9
25 号迟到晚到的数量为 0
26 号迟到晚到的数量为 19
27 号迟到晚到的数量为 0
28 号迟到晚到的数量为 0
29 号迟到晚到的数量为 23
30 号迟到晚到的数量为 0
31 号迟到晚到的数量为 0


1 号早退的数量为 0
2 号早退的数量为 0
3 号早退的数量为 0
4 号早退的数量为 0
5 号早退的数量为 0
6 号早退的数量为 0
7 号早退的数量为 0
8 号早退的数量为 0
9 号早退的数量为 0
10 号早退的数量为 0
11 号早退的数量为 0
12 号早退的数量为 1
13 号早退的数量为 0
14 号早退的数量为 0
15 号早退的数量为 48
16 号早退的数量为 2
17 号早退的数量为 27
18 号早退的数量为 0
19 号早退的数量为 0
20 号早退的数量为 0
21 号早退的数量为 0
22 号早退的数量为 0
23 号早退的数量为 0
24 号早退的数量为 0
25 号早退的数量为 99
26 号早退的数量为 41
27 号早退的数量为 110
28 号早退的数量为 1
29 号早退的数量为 69
30 号早退的数量为 0
31 号早退的数量为 0


1 号校服校徽问题的比例为 620
2 号校服校徽问题的比例为 0
3 号校服校徽问题的比例为 0
4 号校服校徽问题的比例为 0
5 号校服校徽问题的比例为 0
6 号校服校徽问题的比例为 0
7 号校服校徽问题的比例为 0
8 号校服校徽问题的比例为 0
9 号校服校徽问题的比例为 0
10 号校服校徽问题的比例为 0
11 号校服校徽问题的比例为 0
12 号校服校徽问题的比例为 0
13 号校服校徽问题的比例为 0
14 号校服校徽问题的比例为 0
15 号校服校徽问题的比例为 0
16 号校服校徽问题的比例为 0
17 号校服校徽问题的比例为 0
18 号校服校徽问题的比例为 0
19 号校服校徽问题的比例为 0
20 号校服校徽问题的比例为 0
21 号校服校徽问题的比例为 0
22 号校服校徽问题的比例为 0
23 号校服校徽问题的比例为 0
24 号校服校徽问题的比例为 0
25 号校服校徽问题的比例为 0
26 号校服校徽问题的比例为 0
27 号校服校徽问题的比例为 0
28 号校服校徽问题的比例为 0
29 号校服校徽问题的比例为 0
30 号校服校徽问题的比例为 0
31 号校服校徽问题的比例为 0
'''

def create_late_json():
    json_data = {"row": [statistic_year_late(), statistic_term_late(), statistic_month_late(), statistic_day_late()], "name": [year_name, term_name, month_name, date_name]}
    with open('../1.School-level-data/School_Attendance_1.json', "w") as file:
        json.dump(json_data, file)
    print("完成文件加载")

def create_early_json():
    json_data = {"row": [statistic_year_early(), statistic_term_early(), statistic_month_early(), statistic_day_early()], "name": [year_name, term_name, month_name, date_name]}
    with open('../1.School-level-data/School_Attendance_2.json', "w") as file:
        json.dump(json_data, file)
    print("完成文件加载")

def create_uniform_json():
    json_data = {
        "row": [statistic_year_uniform(), statistic_term_uniform(), statistic_month_uniform(), statistic_day_uniform()],
        "name": [year_name, term_name, month_name, date_name]}
    with open('../1.School-level-data/School_Attendance_3.json', "w") as file:
        json.dump(json_data, file)
    print("完成文件加载")


# create_late_json()
# create_early_json()
# create_uniform_json()

##############################################################################
# Step6: 统计早晨上学放学和下午上学放学的统计数据
##############################################################################

def statistic_peak_hour():
    data_origin['hour'] = (data_origin['DataDateTime'].str.split(' ', expand=True)[1]).str.split(':', expand=True)[0]
    data_origin['minute'] = ((data_origin['DataDateTime'].str.split(' ', expand=True)[1]).str.split(':', expand=True)[1]).str.split(':', expand=True)[0]
    data_peak_out = data_origin
    # data_peak_out = data_origin.drop(data_origin[data_origin['hour'] != '17'].index)
    time = []
    summary = 0
    data_all = []
    time_reg_all = []
    count = [0] * 24
    # print(data_peak_out['hour'])

    for m in range(10):
        time_piece = '0' + str(m) + ':00'
        time.append(time_piece)
        time_reg = '0' + str(m)
        time_reg_all.append(time_reg)

    for i in range(10, 24):
        time_piece = str(i) + ':00'
        time.append(time_piece)

    for i in range(0, 10):
        for j in range(data_peak_out.shape[0]):
            if data_peak_out['hour'].iloc[j] == time_reg_all[i]:
                count[i] += 1

    for i in range(10, 24):
        for j in range(data_peak_out.shape[0]):
            if data_peak_out['hour'].iloc[j] == str(i):
                count[i] += 1

    for n in range(len(count)):
        count[n] = round(count[n], 2)

    for i in range(len(count)):
        summary += count[i]

    for i in range(len(count)):
        data_piece = [round(summary/(len(count)), 2), time[i]]
        data_all.append(data_piece)

    print(time)
    print(count)
    print(data_all)

# statistic_peak_hour()

def statistic_peak_minute2():
    data_origin['hour'] = (data_origin['DataDateTime'].str.split(' ', expand=True)[1]).str.split(':', expand=True)[0]
    data_origin['minute'] = \
    ((data_origin['DataDateTime'].str.split(' ', expand=True)[1]).str.split(':', expand=True)[1]).str.split(':', expand=True)[0]
    data_peak_out1 = data_origin.drop(data_origin[data_origin['hour'] != '16'].index)
    data_peak_out2 = data_origin.drop(data_origin[data_origin['hour'] != '17'].index)
    time = []
    summary = 0
    time_reg_all = []
    data_all = []
    count = [0] * 120

    for i in range(10):
        time_piece = '16:0' + str(i)
        time_reg = '0' + str(i)
        time_reg_all.append(time_reg)
        time.append(time_piece)

    for i in range(10, 60):
        time_piece = '16:' + str(i)
        time.append(time_piece)

    for i in range(10):
        for j in range(data_peak_out1.shape[0]):
            if data_peak_out1['minute'].iloc[j] == time_reg_all[i]:
                count[i] += 1

    for i in range(10, 60):
        for j in range(data_peak_out1.shape[0]):
            if data_peak_out1['minute'].iloc[j] == str(i):
                count[i] += 1

    for i in range(10):
        time_piece = '17:0' + str(i)
        time_reg = '0' + str(i)
        time_reg_all.append(time_reg)
        time.append(time_piece)

    for i in range(10, 60):
        time_piece = '17:' + str(i)
        time.append(time_piece)

    for i in range(10):
        for j in range(data_peak_out2.shape[0]):
            if data_peak_out2['minute'].iloc[j] == time_reg_all[i + 10]:
                count[i + 60] += 1

    for i in range(10, 60):
        for j in range(data_peak_out2.shape[0]):
            if data_peak_out2['minute'].iloc[j] == str(i):
                count[i + 60] += 1

    for i in range(len(count)):
        summary += count[i]

    for i in range(len(count)):
        data_piece = [round(summary/(len(count)), 2), time[i]]
        data_all.append(data_piece)

    print(time)
    print(count)
    print(data_all)

# statistic_peak_minute2()