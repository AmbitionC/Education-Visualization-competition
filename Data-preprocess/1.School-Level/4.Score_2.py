#-*- coding:utf-8 -*-

'''
# Author: chenhao
# Date: April. 11
# Description: Data-process for Education visualization competition
'''

##############################################################################
#Part4：统计学校的学生成绩
##############################################################################

import pandas as pd
import numpy as np
import json

# 读取原始数据集合
data_origin = pd.read_csv('../../education_data/5_chengji.csv')

data_student_info = pd.read_csv('../../education_data/2_student_info.csv')

data_merge_byStdId = pd.read_csv('../../education_data/CH/5.chengji_3_claID/5.chengji_3_claID.csv')


##############################################################################
#Step1: 观察各次考试的数据情况

def statistic_exam():
    data_origin['sum'] = 1
    data_statistic =data_origin.groupby(['exam_numname']).count().reset_index().sort_values(by='sum', axis=0, ascending=False)
    print(data_statistic)

# print(statistic_exam())

def extract_exam_data(exam_id):
    data_exam = data_origin.drop(data_origin[data_origin['exam_number'] != exam_id].index)
    # print(data_exam)
    return data_exam

def statistic_exam_data():
    data_exam = extract_exam_data(304)
    data_statis = data_exam.groupby(['mes_sub_name']).count().reset_index()
    for i in range(data_statis.shape[0]):
        print('学科', data_statis['mes_sub_name'].iloc[i], '的数据量为', data_statis['mes_TestID'].iloc[i])
    students_groupby = data_exam.groupby(['mes_StudentID']).count().reset_index().sort_values(by='mes_TestID', axis=0, ascending=False)
    print(students_groupby.shape)

# statistic_exam_data()
# 学科 化学 的数据量为 954
# 学科 历史 的数据量为 730
# 学科 地理 的数据量为 843
# 学科 政治 的数据量为 1110
# 学科 数学 的数据量为 1516
# 学科 物理 的数据量为 973
# 学科 生物 的数据量为 1111
# 学科 英语 的数据量为 1112
# 学科 语文 的数据量为 1517
# (1518, 13)

def merge_data_byStdId():
    data_exam = extract_exam_data(304)
    data_merge_byStdId = pd.merge(data_exam, data_student_info, left_on='mes_StudentID', right_on='bf_StudentID', how='left')
    print(data_merge_byStdId)
    data = data_merge_byStdId.drop(['bf_Name', 'mes_TestID', 'exam_number', 'bf_sex', 'bf_nation', 'bf_BornDate', 'bf_NativePlace', 'Bf_ResidenceType', 'bf_policy', 'cla_term', 'bf_zhusu', 'bf_leaveSchool', 'bf_qinshihao'], axis=1)
    data.to_csv('../../education_data/CH/5.chengji_3_claID/5.chengji_3_claID.csv', encoding='utf_8_sig')
    print('存储完成！')

# merge_data_byStdId()

def split_data_byGrade():
    grade = ['高一', '高二', '高三']
    for i in range(3):
        data_split_byGrade = data_merge_byStdId[data_merge_byStdId['cla_Name'].str.contains(grade[i])]
        # 使用上一组数据对缺失值进行填充
        data_split_byGrade['mes_T_Score'] = data_split_byGrade['mes_T_Score'].fillna(method='pad')
        filename = '../../education_data/CH/5.chengji_3_claID/' + grade[i] + '.csv'
        data_split_byGrade.to_csv(filename, encoding='utf_8_sig')
        print('存储完成！')

# split_data_byGrade()

def get_claName_byGrade():
    filepath = ['../../education_data/CH/5.chengji_3_claID/高一.csv',
                '../../education_data/CH/5.chengji_3_claID/高二.csv',
                '../../education_data/CH/5.chengji_3_claID/高三.csv']
    cla_Name = []
    for i in range(3):
        data_split_byGrade = pd.read_csv(filepath[i])
        data_claName_byGrade = data_split_byGrade.groupby('cla_Name').count().reset_index()
        cla_Name_piece = []
        for j in range(data_claName_byGrade.shape[0]):
            cla_Name_piece.append(data_claName_byGrade['cla_Name'].iloc[j])
        print(cla_Name_piece)
        cla_Name.append(cla_Name_piece)
    print(cla_Name)
get_claName_byGrade()

def group_data_byStdId(grade):
    filepath = ['../../education_data/CH/5.chengji_3_claID/高一.csv',
                '../../education_data/CH/5.chengji_3_claID/高二.csv',
                '../../education_data/CH/5.chengji_3_claID/高三.csv']
    sub_name = ['语文', '数学', '英语', '物理', '化学', '政治', '历史', '生物', '地理', '技术']
    data_split_byGrade = pd.read_csv(filepath[grade])
    data_group_byStuId = data_split_byGrade.groupby('mes_StudentID').count().reset_index()
    print(data_group_byStuId)

# group_data_byStdId(0)