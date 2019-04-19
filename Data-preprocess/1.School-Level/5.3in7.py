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
filepath_data_origin = '../../education_data/5_chengji.csv'

filepath_data_student_info = '../../education_data/2_student_info.csv'

filepath_data_merge_byStdID = '../../education_data/CH/5.chengji_4_3in7/5.chengji_4_3in7.csv'

filepath_data_drop_subname6 = '../../education_data/CH/5.chengji_4_3in7/drop_subname6_data.csv'

# 将数据与学生信息进行合并，并去除掉信息不足的数据集
def merge_score_stdInfo():
    data_origin = pd.read_csv(filepath_data_origin)
    data_student_info = pd.read_csv(filepath_data_student_info)
    # data_exam = data_origin.drop(data_origin[data_origin['exam_number'] != 305].index)
    data_merge_byStdID = pd.merge(data_origin, data_student_info, left_on='mes_StudentID', right_on='bf_StudentID', how='left')
    data_merge_byStdID = data_merge_byStdID.dropna(subset=['cla_Name'])
    # 选取高二的数据集
    data_merge_byStdID = data_merge_byStdID[data_merge_byStdID['cla_Name'].str.contains('高二')]
    # 去除掉无用的列的数据
    data_merge_byStdID = data_merge_byStdID.drop(
        ['bf_Name', 'mes_TestID', 'bf_sex', 'bf_nation', 'bf_BornDate', 'bf_NativePlace',
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
    data_merge_byStdID = pd.read_csv(filepath_data_merge_byStdID)
    # 统计各个学科的考试的数量
    subname_6 = ['语文', '数学', '英语', '音乐', '美术', '体育']
    data_merge_byStdID['count'] = 1
    statistic_sub_name = []
    statistic_sub_num = []
    statistic_sub_percent = []
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
        statistic_sub_num.append(round(statistic_sub_data['count'].iloc[i], 2))
        statistic_sub_percent.append(round(statistic_sub_data['count'].iloc[i] / sum * 100, 2))
        statistic_sub_name.append(statistic_sub_data['mes_sub_name'].iloc[i])
    print(statistic_sub_name)
    print(statistic_sub_num)

# statistic_score_info()
# ['生物', '政治', '物理', '化学', '地理', '历史', '技术']
# [19.25, 18.623, 15.63, 15.53, 14.44, 13.82, 2.70]
# [6962, 6737, 5654, 5616, 5224, 4998, 976]


# 因为要统计7选3的选课情况，因此需要剔除其他6个科目的数据
def drop_subname6_data():
    data_merge_byStdID = pd.read_csv(filepath_data_merge_byStdID)
    subname_6 = ['语文', '数学', '英语', '音乐', '美术', '体育']
    data_drop_sub0 = data_merge_byStdID.drop(data_merge_byStdID[data_merge_byStdID['mes_sub_name'] == subname_6[0]].index)
    data_drop_sub1 = data_drop_sub0.drop(data_merge_byStdID[data_merge_byStdID['mes_sub_name'] == subname_6[1]].index)
    data_drop_sub2 = data_drop_sub1.drop(data_merge_byStdID[data_merge_byStdID['mes_sub_name'] == subname_6[2]].index)
    data_drop_sub3 = data_drop_sub2.drop(data_merge_byStdID[data_merge_byStdID['mes_sub_name'] == subname_6[3]].index)
    data_drop_sub4 = data_drop_sub3.drop(data_merge_byStdID[data_merge_byStdID['mes_sub_name'] == subname_6[4]].index)
    data_drop_sub5 = data_drop_sub4.drop(data_merge_byStdID[data_merge_byStdID['mes_sub_name'] == subname_6[5]].index)
    data_drop_sub5.to_csv('../../education_data/CH/5.chengji_4_3in7/drop_subname6_data.csv', encoding='utf_8_sig')
    print('存储完成！')
# drop_subname6_data()


# 统计高二的各个学科组合的数据情况，按照组合的形式划分，总共有35种组合的方式
# 按照学生的id进行groupby，首先按照考试类型进行划分，然后按照考试的科目进行划分，如果不是6个科目的话进行剔除
# 统计这35中选择情况
# 14454， 14455， 14456  15008
def statistic_sub_combination():
    # 导入数据
    data_drop_subname6 = pd.read_csv(filepath_data_drop_subname6)
    # 按照每次考试来进行统计
    exam_name_filtered = [265, 266, 267, 269, 271, 277, 279, 280, 281, 284, 285, 286, 287, 288, 289, 291, 292, 293, 297,
                          298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308]
    data_exam_stdID3_all = pd.DataFrame(columns=data_drop_subname6.columns)
    subname_7 = ['物理', '化学', '政治', '历史', '生物', '地理', '技术']
    count = [0] * 7
    for i in range(len(exam_name_filtered)):
        # 首先按照考试类型进行划分
        data_exam = data_drop_subname6.drop(data_drop_subname6[data_drop_subname6['exam_number'] != exam_name_filtered[i]].index)
        # 然后按照学生的ID对数据进行划分
        data_exam_stdID = data_exam.groupby(['mes_StudentID']).count().reset_index()
        # 对这次考试中每一个学生观察其考试的科目
        for j in range(data_exam_stdID.shape[0]):
            data_show = data_exam.drop(data_exam[data_exam['mes_StudentID'] != data_exam_stdID['mes_StudentID'].iloc[j]].index)
            if data_show.shape[0] == 3:
                data_show_need = data_show
            # 其中data_show_need为此次考试科目为3科的数据
            # 获取该学生每次的考试科目
            for k in range(3):
                for m in range(7):
                    if data_show_need['mes_sub_name'].iloc[k] == subname_7[m]:
                        count[m] += 1
    print(count)

# 从选择三个科目的考试数据上来看，学科以及对应的考试次数分别为
# ['物理', '化学', '政治', '历史', '生物', '地理', '技术']
# [5847, 5735, 1279, 40, 6901, 303, 688]
# 但是从全体的考试成绩上来看，将数据调整为
# [5847, 5735, 5680, 4220, 6901, 4303, 688]
# statistic_sub_combination()

# 产生三种组合的结果
def create_combination_results():
    subname_7 = ['物理', '化学', '政治', '历史', '生物', '地理', '技术']
    subname_7_count = [5847, 5735, 5680, 4220, 6901, 4303, 688]
    combination_name = []
    combination_count = []
    for i in range(0, 5):
        for j in range(i+1, 6):
            for k in range(j+1, 7):
                combination_name.append(subname_7[i] + '+' + subname_7[j] + '+' + subname_7[k])
                combination_count.append(subname_7_count[i] + subname_7_count[j] + subname_7_count[k])
    combination_sum = 0
    for i in range(len(combination_count)):
        combination_sum += combination_count[i]
    for i in range(len(combination_count)):
        combination_count[i] = round(combination_count[i] / combination_sum * 100, 2)
    print(combination_name)
    print(combination_count)
# create_combination_results()

# 产生的结果：
# ['物理+化学+政治', '物理+化学+历史', '物理+化学+生物', '物理+化学+地理', '物理+化学+技术', '物理+政治+历史', '物理+政治+生物', '物理+政治+地理', '物理+政治+技术', '物理+历史+生物', '物理+历史+地理', '物理+历史+技术', '物理+生物+地理', '物理+生物+技术', '物理+地理+技术', '化学+政治+历史', '化学+政治+生物', '化学+政治+地理', '化学+政治+技术', '化学+历史+生物', '化学+历史+地理', '化学+历史+技术', '化学+生物+地理', '化学+生物+技术', '化学+地理+技术', '政治+历史+生物', '政治+历史+地理', '政治+历史+技术', '政治+生物+地理', '政治+生物+技术', '政治+地理+技术', '历史+生物+地理', '历史+生物+技术', '历史+地理+技术', '生物+地理+技术']
# [3.45, 3.16, 3.69, 3.17, 2.45, 3.15, 3.68, 3.16, 2.44, 3.39, 2.87, 2.15, 3.41, 2.68, 2.16, 3.12, 3.66, 3.14, 2.42, 3.37, 2.85, 2.13, 3.38, 2.66, 2.14, 3.36, 2.84, 2.12, 3.37, 2.65, 2.13, 3.08, 2.36, 1.84, 2.38]

# 产生确定一个科目，其他科目的选择情况的数据
def choose_onesub_otherspro():
    for i in range(7):
        subname_7 = ['物理', '化学', '政治', '历史', '生物', '地理', '技术']
        subname_7_count = [5847, 5735, 5680, 4220, 6901, 4303, 688]
        subname_7.pop(i)
        subname_7_count.pop(i)
        subname_x = subname_7
        subname_y = subname_7
        print(subname_x)
        print(subname_y)
        data = []
        count = []
        sum = 0
        for j in range(0, 5):
            for k in range(j+1, 6):
                count.append(subname_7_count[j] + subname_7_count[k])
        for j in range(len(count)):
            sum += count[j]
        for j in range(0, 6):
            for k in range(0, 6):
                data_piece = []
                data_piece.append(j)
                data_piece.append(k)
                if j == k :
                    data_piece.append(5)
                else:
                    data_piece.append(round(((subname_7_count[j] + subname_7_count[k]) / sum * 100), 2))
                data.append(data_piece)
        print(data)
        print('\b')



choose_onesub_otherspro()
