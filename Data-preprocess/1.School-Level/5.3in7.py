#-*- coding:utf-8 -*-

'''
# Author: chenhao
# Date: April. 15
# Description: Data-process for Education visualization competition
'''

##############################################################################
#Part5：直观展示学生7选3的课程分布情况
##############################################################################

import pandas as pd
import numpy as np
import json

# 读取原始的数据集
data_origin = pd.read_csv('../../education_data/5_chengji.csv')

data_student_info = pd.read_csv('../../education_data/2_student_info.csv')

data_merge_byStdID = pd.read_csv('../../education_data/CH/5.chengji_4_3in7/5.chengji_4_3in7.csv')

# 将数据与学生信息进行合并，并去除掉信息不足的数据集
def merge_score_stdInfo():
    # data_exam = data_origin.drop(data_origin[data_origin['exam_number'] != 305].index)
    data_merge_byStdID = pd.merge(data_origin, data_student_info, left_on='mes_StudentID', right_on='bf_StudentID', how='left')
    data_merge_byStdID = data_merge_byStdID.dropna(subset=['cla_Name'])
    # 选取高二的数据集
    data_merge_byStdID = data_merge_byStdID[data_merge_byStdID['cla_Name'].str.contains('高二')]
    # 去除掉无用的列的数据
    data_merge_byStdID = data_merge_byStdID.drop(
        ['bf_Name', 'mes_TestID', 'exam_number', 'bf_sex', 'bf_nation', 'bf_BornDate', 'bf_NativePlace',
         'Bf_ResidenceType', 'bf_policy', 'cla_term', 'bf_zhusu', 'bf_leaveSchool', 'bf_qinshihao'], axis=1)
    # 删除掉数据量异常的数据，比如ID为14037的考试数据量为251，考试数据量过少的学生ID
    data_groupby_stdID = data_merge_byStdID.groupby(['bf_StudentID']).count().reset_index().sort_values(by='exam_numname', axis=0, ascending=False)
    data_groupby_stdID = data_groupby_stdID.drop(data_groupby_stdID[data_groupby_stdID['exam_numname'] > 100].index)
    data_merge_byStdID = data_merge_byStdID.drop(data_merge_byStdID[data_merge_byStdID['bf_StudentID'] == 14037].index)
    for i in range(data_groupby_stdID.shape[0]):
        data_merge_byStdID = data_merge_byStdID.drop(data_merge_byStdID[data_merge_byStdID['bf_StudentID'] == data_groupby_stdID['bf_StudentID'].iloc[i]].index)
    # 将数据进行存储
    data_merge_byStdID.to_csv('../../education_data/CH/5.chengji_4_3in7/5.chengji_4_3in7.csv', encoding='utf_8_sig')
    print('完成文件加载！')

# merge_score_stdInfo()

# 统计高二的数据，观察其考试的数据
def statistic_score_info():
    # 统计各个学科的考试的数量
    subname_6 = ['语文', '数学', '英语', '音乐', '美术', '体育']
    data_merge_byStdID['count'] = 1
    statistic_sub_name = []
    statistic_sub_num = []
    sum = 0
    statistic_sub_data = data_merge_byStdID.groupby(['mes_sub_name']).count().reset_index().sort_values(by='count', axis=0, ascending=False)
    # 去除掉非7选3的学科
    for i in range(len(subname_6)):
        statistic_sub_data = statistic_sub_data.drop(statistic_sub_data[statistic_sub_data['mes_sub_name'] == subname_6[i]].index)
    # 计算课程的总量
    for i in range(statistic_sub_data.shape[0]):
        sum += statistic_sub_data['count'].iloc[i]
    # 提取数据
    for i in range(statistic_sub_data.shape[0]):
        print(statistic_sub_data['mes_sub_name'].iloc[i], '的数据量为', statistic_sub_data['count'].iloc[i])
        statistic_sub_num.append(round(statistic_sub_data['count'].iloc[i] / sum * 100, 2))
        statistic_sub_name.append(statistic_sub_data['mes_sub_name'].iloc[i])
    print(statistic_sub_name)
    print(statistic_sub_num)

statistic_score_info()
# ['生物', '政治', '物理', '化学', '地理', '历史', '技术']
# [19.25, 18.623, 15.63, 15.53, 14.44, 13.82, 2.70]

# 统计高二的各个学科组合的数据情况，按照组合的形式划分，总共有35种组合的方式
# 按照学生的id进行groupby，首先按照考试类型进行划分，然后按照考试的科目进行划分，如果不是6个科目的话进行剔除
# 统计这35种情况
# def statistic_sub_combination():
