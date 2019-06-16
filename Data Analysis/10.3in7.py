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

# 对组合选择情况进行排序
def sort_combination_results():
    combination_name = ['物理+化学+政治', '物理+化学+历史', '物理+化学+生物', '物理+化学+地理', '物理+化学+技术', '物理+政治+历史', '物理+政治+生物', '物理+政治+地理', '物理+政治+技术', '物理+历史+生物', '物理+历史+地理', '物理+历史+技术', '物理+生物+地理', '物理+生物+技术', '物理+地理+技术', '化学+政治+历史', '化学+政治+生物', '化学+政治+地理', '化学+政治+技术', '化学+历史+生物', '化学+历史+地理', '化学+历史+技术', '化学+生物+地理', '化学+生物+技术', '化学+地理+技术', '政治+历史+生物', '政治+历史+地理', '政治+历史+技术', '政治+生物+地理', '政治+生物+技术', '政治+地理+技术', '历史+生物+地理', '历史+生物+技术', '历史+地理+技术', '生物+地理+技术']
    combination_count = [3.45, 3.16, 3.69, 3.17, 2.45, 3.15, 3.68, 3.16, 2.44, 3.39, 2.87, 2.15, 3.41, 2.68, 2.16, 3.12, 3.66, 3.14, 2.42, 3.37, 2.85, 2.13, 3.38, 2.66, 2.14, 3.36, 2.84, 2.12, 3.37, 2.65, 2.13, 3.08, 2.36, 1.84, 2.38]
    combination_count = np.array(combination_count)
    sorted_index = combination_count.argsort()
    print(sorted_index)
    sorted_count = []
    sorted_name = []
    for i in range(len(sorted_index)):
        sorted_count.append(combination_count[sorted_index[34-i]])
        sorted_name.append(combination_name[sorted_index[34-i]])
    print(sorted_name)
    print(sorted_count)

# sort_combination_results()
# ['物理+化学+生物', '物理+政治+生物', '化学+政治+生物', '物理+化学+政治', '物理+生物+地理', '物理+历史+生物', '化学+生物+地理', '化学+历史+生物', '政治+生物+地理', '政治+历史+生物', '物理+化学+地理', '物理+化学+历史', '物理+政治+地理', '物理+政治+历史', '化学+政治+地理', '化学+政治+历史', '历史+生物+地理', '物理+历史+地理', '化学+历史+地理', '政治+历史+地理', '物理+生物+技术', '化学+生物+技术', '政治+生物+技术', '物理+化学+技术', '物理+政治+技术', '化学+政治+技术', '生物+地理+技术', '历史+生物+技术', '物理+地理+技术', '物理+历史+技术', '化学+地理+技术', '化学+历史+技术', '政治+地理+技术', '政治+历史+技术', '历史+地理+技术']
# [3.69, 3.68, 3.66, 3.45, 3.41, 3.39, 3.38, 3.37, 3.37, 3.36, 3.17, 3.16, 3.16, 3.15, 3.14, 3.12, 3.08, 2.87, 2.85, 2.84, 2.68, 2.66, 2.65, 2.45, 2.44, 2.42, 2.38, 2.36, 2.16, 2.15, 2.14, 2.13, 2.13, 2.12, 1.84]


# 产生确定一个科目，其他科目的选择情况的数据
def choose_onesub_otherspro():
    data_total = []
    subname_xy_total = []
    for i in range(7):
        subname_7 = ['物理', '化学', '政治', '历史', '生物', '地理', '技术']
        subname_7_count = [5847, 5735, 5680, 4220, 6901, 4303, 688]
        subname_7.pop(i)
        subname_7_count.pop(i)
        subname_x = subname_7
        subname_y = subname_7
        # print(subname_x)
        # print(subname_y)
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
                if j != k:
                    data_piece.append(round(((subname_7_count[j] + subname_7_count[k]) / sum * 100), 2))
                    data.append(data_piece)
        subname_xy_total.append(subname_x)
        data_total.append(data)
    print(subname_xy_total)
    print(data_total)

# choose_onesub_otherspro()
# ['化学', '政治', '历史', '生物', '地理', '技术']
# ['化学', '政治', '历史', '生物', '地理', '技术']
# [[0, 0, 5], [0, 1, 8.29], [0, 2, 7.23], [0, 3, 9.18], [0, 4, 7.29], [0, 5, 4.67], [1, 0, 8.29], [1, 1, 5], [1, 2, 7.19], [1, 3, 9.14], [1, 4, 7.25], [1, 5, 4.63], [2, 0, 7.23], [2, 1, 7.19], [2, 2, 5], [2, 3, 8.08], [2, 4, 6.19], [2, 5, 3.57], [3, 0, 9.18], [3, 1, 9.14], [3, 2, 8.08], [3, 3, 5], [3, 4, 8.14], [3, 5, 5.51], [4, 0, 7.29], [4, 1, 7.25], [4, 2, 6.19], [4, 3, 8.14], [4, 4, 5], [4, 5, 3.63], [5, 0, 4.67], [5, 1, 4.63], [5, 2, 3.57], [5, 3, 5.51], [5, 4, 3.63], [5, 5, 5]]
#
#
# ['物理', '政治', '历史', '生物', '地理', '技术']
# ['物理', '政治', '历史', '生物', '地理', '技术']
# [[0, 0, 5], [0, 1, 8.34], [0, 2, 7.28], [0, 3, 9.22], [0, 4, 7.34], [0, 5, 4.73], [1, 0, 8.34], [1, 1, 5], [1, 2, 7.16], [1, 3, 9.1], [1, 4, 7.22], [1, 5, 4.61], [2, 0, 7.28], [2, 1, 7.16], [2, 2, 5], [2, 3, 8.05], [2, 4, 6.17], [2, 5, 3.55], [3, 0, 9.22], [3, 1, 9.1], [3, 2, 8.05], [3, 3, 5], [3, 4, 8.11], [3, 5, 5.49], [4, 0, 7.34], [4, 1, 7.22], [4, 2, 6.17], [4, 3, 8.11], [4, 4, 5], [4, 5, 3.61], [5, 0, 4.73], [5, 1, 4.61], [5, 2, 3.55], [5, 3, 5.49], [5, 4, 3.61], [5, 5, 5]]
#
#
# ['物理', '化学', '历史', '生物', '地理', '技术']
# ['物理', '化学', '历史', '生物', '地理', '技术']
# [[0, 0, 5], [0, 1, 8.36], [0, 2, 7.27], [0, 3, 9.21], [0, 4, 7.33], [0, 5, 4.72], [1, 0, 8.36], [1, 1, 5], [1, 2, 7.19], [1, 3, 9.13], [1, 4, 7.25], [1, 5, 4.64], [2, 0, 7.27], [2, 1, 7.19], [2, 2, 5], [2, 3, 8.03], [2, 4, 6.16], [2, 5, 3.54], [3, 0, 9.21], [3, 1, 9.13], [3, 2, 8.03], [3, 3, 5], [3, 4, 8.09], [3, 5, 5.48], [4, 0, 7.33], [4, 1, 7.25], [4, 2, 6.16], [4, 3, 8.09], [4, 4, 5], [4, 5, 3.6], [5, 0, 4.72], [5, 1, 4.64], [5, 2, 3.54], [5, 3, 5.48], [5, 4, 3.6], [5, 5, 5]]
#
#
# ['物理', '化学', '政治', '生物', '地理', '技术']
# ['物理', '化学', '政治', '生物', '地理', '技术']
# [[0, 0, 5], [0, 1, 7.95], [0, 2, 7.91], [0, 3, 8.75], [0, 4, 6.96], [0, 5, 4.48], [1, 0, 7.95], [1, 1, 5], [1, 2, 7.83], [1, 3, 8.67], [1, 4, 6.89], [1, 5, 4.41], [2, 0, 7.91], [2, 1, 7.83], [2, 2, 5], [2, 3, 8.63], [2, 4, 6.85], [2, 5, 4.37], [3, 0, 8.75], [3, 1, 8.67], [3, 2, 8.63], [3, 3, 5], [3, 4, 7.69], [3, 5, 5.21], [4, 0, 6.96], [4, 1, 6.89], [4, 2, 6.85], [4, 3, 7.69], [4, 4, 5], [4, 5, 3.42], [5, 0, 4.48], [5, 1, 4.41], [5, 2, 4.37], [5, 3, 5.21], [5, 4, 3.42], [5, 5, 5]]
#
#
# ['物理', '化学', '政治', '历史', '地理', '技术']
# ['物理', '化学', '政治', '历史', '地理', '技术']
# [[0, 0, 5], [0, 1, 8.75], [0, 2, 8.71], [0, 3, 7.61], [0, 4, 7.67], [0, 5, 4.94], [1, 0, 8.75], [1, 1, 5], [1, 2, 8.62], [1, 3, 7.52], [1, 4, 7.58], [1, 5, 4.85], [2, 0, 8.71], [2, 1, 8.62], [2, 2, 5], [2, 3, 7.48], [2, 4, 7.54], [2, 5, 4.81], [3, 0, 7.61], [3, 1, 7.52], [3, 2, 7.48], [3, 3, 5], [3, 4, 6.44], [3, 5, 3.71], [4, 0, 7.67], [4, 1, 7.58], [4, 2, 7.54], [4, 3, 6.44], [4, 4, 5], [4, 5, 3.77], [5, 0, 4.94], [5, 1, 4.85], [5, 2, 4.81], [5, 3, 3.71], [5, 4, 3.77], [5, 5, 5]]
#
#
# ['物理', '化学', '政治', '历史', '生物', '技术']
# ['物理', '化学', '政治', '历史', '生物', '技术']
# [[0, 0, 5], [0, 1, 7.97], [0, 2, 7.93], [0, 3, 6.93], [0, 4, 8.77], [0, 5, 4.5], [1, 0, 7.97], [1, 1, 5], [1, 2, 7.85], [1, 3, 6.85], [1, 4, 8.69], [1, 5, 4.42], [2, 0, 7.93], [2, 1, 7.85], [2, 2, 5], [2, 3, 6.81], [2, 4, 8.66], [2, 5, 4.38], [3, 0, 6.93], [3, 1, 6.85], [3, 2, 6.81], [3, 3, 5], [3, 4, 7.65], [3, 5, 3.38], [4, 0, 8.77], [4, 1, 8.69], [4, 2, 8.66], [4, 3, 7.65], [4, 4, 5], [4, 5, 5.22], [5, 0, 4.5], [5, 1, 4.42], [5, 2, 4.38], [5, 3, 3.38], [5, 4, 5.22], [5, 5, 5]]
#
#
# ['物理', '化学', '政治', '历史', '生物', '地理']
# ['物理', '化学', '政治', '历史', '生物', '地理']
# [[0, 0, 5], [0, 1, 7.09], [0, 2, 7.05], [0, 3, 6.16], [0, 4, 7.8], [0, 5, 6.21], [1, 0, 7.09], [1, 1, 5], [1, 2, 6.98], [1, 3, 6.09], [1, 4, 7.73], [1, 5, 6.14], [2, 0, 7.05], [2, 1, 6.98], [2, 2, 5], [2, 3, 6.06], [2, 4, 7.7], [2, 5, 6.11], [3, 0, 6.16], [3, 1, 6.09], [3, 2, 6.06], [3, 3, 5], [3, 4, 6.8], [3, 5, 5.22], [4, 0, 7.8], [4, 1, 7.73], [4, 2, 7.7], [4, 3, 6.8], [4, 4, 5], [4, 5, 6.86], [5, 0, 6.21], [5, 1, 6.14], [5, 2, 6.11], [5, 3, 5.22], [5, 4, 6.86], [5, 5, 5]]

# [['化学', '政治', '历史', '生物', '地理', '技术'], ['物理', '政治', '历史', '生物', '地理', '技术'], ['物理', '化学', '历史', '生物', '地理', '技术'], ['物理', '化学', '政治', '生物', '地理', '技术'], ['物理', '化学', '政治', '历史', '地理', '技术'], ['物理', '化学', '政治', '历史', '生物', '技术'], ['物理', '化学', '政治', '历史', '生物', '地理']]
# [[[0, 1, 8.29], [0, 2, 7.23], [0, 3, 9.18], [0, 4, 7.29], [0, 5, 4.67], [1, 0, 8.29], [1, 2, 7.19], [1, 3, 9.14], [1, 4, 7.25], [1, 5, 4.63], [2, 0, 7.23], [2, 1, 7.19], [2, 3, 8.08], [2, 4, 6.19], [2, 5, 3.57], [3, 0, 9.18], [3, 1, 9.14], [3, 2, 8.08], [3, 4, 8.14], [3, 5, 5.51], [4, 0, 7.29], [4, 1, 7.25], [4, 2, 6.19], [4, 3, 8.14], [4, 5, 3.63], [5, 0, 4.67], [5, 1, 4.63], [5, 2, 3.57], [5, 3, 5.51], [5, 4, 3.63]], [[0, 1, 8.34], [0, 2, 7.28], [0, 3, 9.22], [0, 4, 7.34], [0, 5, 4.73], [1, 0, 8.34], [1, 2, 7.16], [1, 3, 9.1], [1, 4, 7.22], [1, 5, 4.61], [2, 0, 7.28], [2, 1, 7.16], [2, 3, 8.05], [2, 4, 6.17], [2, 5, 3.55], [3, 0, 9.22], [3, 1, 9.1], [3, 2, 8.05], [3, 4, 8.11], [3, 5, 5.49], [4, 0, 7.34], [4, 1, 7.22], [4, 2, 6.17], [4, 3, 8.11], [4, 5, 3.61], [5, 0, 4.73], [5, 1, 4.61], [5, 2, 3.55], [5, 3, 5.49], [5, 4, 3.61]], [[0, 1, 8.36], [0, 2, 7.27], [0, 3, 9.21], [0, 4, 7.33], [0, 5, 4.72], [1, 0, 8.36], [1, 2, 7.19], [1, 3, 9.13], [1, 4, 7.25], [1, 5, 4.64], [2, 0, 7.27], [2, 1, 7.19], [2, 3, 8.03], [2, 4, 6.16], [2, 5, 3.54], [3, 0, 9.21], [3, 1, 9.13], [3, 2, 8.03], [3, 4, 8.09], [3, 5, 5.48], [4, 0, 7.33], [4, 1, 7.25], [4, 2, 6.16], [4, 3, 8.09], [4, 5, 3.6], [5, 0, 4.72], [5, 1, 4.64], [5, 2, 3.54], [5, 3, 5.48], [5, 4, 3.6]], [[0, 1, 7.95], [0, 2, 7.91], [0, 3, 8.75], [0, 4, 6.96], [0, 5, 4.48], [1, 0, 7.95], [1, 2, 7.83], [1, 3, 8.67], [1, 4, 6.89], [1, 5, 4.41], [2, 0, 7.91], [2, 1, 7.83], [2, 3, 8.63], [2, 4, 6.85], [2, 5, 4.37], [3, 0, 8.75], [3, 1, 8.67], [3, 2, 8.63], [3, 4, 7.69], [3, 5, 5.21], [4, 0, 6.96], [4, 1, 6.89], [4, 2, 6.85], [4, 3, 7.69], [4, 5, 3.42], [5, 0, 4.48], [5, 1, 4.41], [5, 2, 4.37], [5, 3, 5.21], [5, 4, 3.42]], [[0, 1, 8.75], [0, 2, 8.71], [0, 3, 7.61], [0, 4, 7.67], [0, 5, 4.94], [1, 0, 8.75], [1, 2, 8.62], [1, 3, 7.52], [1, 4, 7.58], [1, 5, 4.85], [2, 0, 8.71], [2, 1, 8.62], [2, 3, 7.48], [2, 4, 7.54], [2, 5, 4.81], [3, 0, 7.61], [3, 1, 7.52], [3, 2, 7.48], [3, 4, 6.44], [3, 5, 3.71], [4, 0, 7.67], [4, 1, 7.58], [4, 2, 7.54], [4, 3, 6.44], [4, 5, 3.77], [5, 0, 4.94], [5, 1, 4.85], [5, 2, 4.81], [5, 3, 3.71], [5, 4, 3.77]], [[0, 1, 7.97], [0, 2, 7.93], [0, 3, 6.93], [0, 4, 8.77], [0, 5, 4.5], [1, 0, 7.97], [1, 2, 7.85], [1, 3, 6.85], [1, 4, 8.69], [1, 5, 4.42], [2, 0, 7.93], [2, 1, 7.85], [2, 3, 6.81], [2, 4, 8.66], [2, 5, 4.38], [3, 0, 6.93], [3, 1, 6.85], [3, 2, 6.81], [3, 4, 7.65], [3, 5, 3.38], [4, 0, 8.77], [4, 1, 8.69], [4, 2, 8.66], [4, 3, 7.65], [4, 5, 5.22], [5, 0, 4.5], [5, 1, 4.42], [5, 2, 4.38], [5, 3, 3.38], [5, 4, 5.22]], [[0, 1, 7.09], [0, 2, 7.05], [0, 3, 6.16], [0, 4, 7.8], [0, 5, 6.21], [1, 0, 7.09], [1, 2, 6.98], [1, 3, 6.09], [1, 4, 7.73], [1, 5, 6.14], [2, 0, 7.05], [2, 1, 6.98], [2, 3, 6.06], [2, 4, 7.7], [2, 5, 6.11], [3, 0, 6.16], [3, 1, 6.09], [3, 2, 6.06], [3, 4, 6.8], [3, 5, 5.22], [4, 0, 7.8], [4, 1, 7.73], [4, 2, 7.7], [4, 3, 6.8], [4, 5, 6.86], [5, 0, 6.21], [5, 1, 6.14], [5, 2, 6.11], [5, 3, 5.22], [5, 4, 6.86]]]

# 产生单科组合排名
def create_combination_data():
    subname_7 = ['物理', '化学', '政治', '历史', '生物', '地理', '技术']
    subname_7_percent = [15.63, 15.53, 18.62, 13.82, 19.25, 14.44, 2.7]
    combination_1 = []
    combination_2 = []
    combination_3 = []
    for i in range(0, 5):
        for j in range(i + 1, 6):
            for k in range(j + 1, 7):
                combination_1.append([subname_7[i] + '+' + subname_7[j] + '+' + subname_7[k], subname_7_percent[i], subname_7[i]])
                combination_2.append([subname_7[i] + '+' + subname_7[j] + '+' + subname_7[k], subname_7_percent[j], subname_7[j]])
                combination_3.append([subname_7[i] + '+' + subname_7[j] + '+' + subname_7[k], subname_7_percent[k], subname_7[k]])
    print(combination_1)
    print(combination_2)
    print(combination_3)

create_combination_data()