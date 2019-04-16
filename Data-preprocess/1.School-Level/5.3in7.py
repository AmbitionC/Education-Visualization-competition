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
    # subname_7 = ['物理', '化学', '生物', '政治', '历史', '地理', '技术']
    # sub_students_choose = []
    statistic_sub_data = data_merge_byStdID.groupby(['mes_sub_name']).count().reset_index().sort_values(by='count', axis=0, ascending=False)
    for i in range(len(subname_6)):
        statistic_sub_data = statistic_sub_data.drop(statistic_sub_data[statistic_sub_data['mes_sub_name'] == subname_6[i]].index)
    for i in range(statistic_sub_data.shape[0]):
        


statistic_score_info()