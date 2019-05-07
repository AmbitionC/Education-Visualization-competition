#-*- coding:utf-8 -*-

'''
# Author: chenhao
# Date: April. 23
# Description: Data-process for Education visualization competition
'''

##############################################################################
#Part7：应用层次展示的内容
##############################################################################

import pandas as pd
import json
import random

# 读取原始的数据集
filepath_StudentsScore = '../../education_data/5_chengji.csv'

filepath_StudentsInfo = '../../education_data/2_student_info.csv'


# 定义一些常规变量
subname = ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理', '技术', '体育', '音乐']

##############################################################################
# Chart_1
# 完成学生的成绩总览（历次的趋势变化等）

def create_confidence_area(rank_array):
    # 产生排名的置信区间
    # 产生置信区间的下限
    rank_down_array = [0] * len(rank_array)
    for i in range(len(rank_array)):
        rank_down = random.randint(2, 5)
        rank_down_array[i] = rank_array[i] - rank_down
        if rank_down_array[i] < 1:
            rank_down_array[i] = 1
    print('下置信区间')
    print(rank_down_array)
    # 产生置信区间的上限
    rank_up_array = [0] * len(rank_array)
    for i in range(len(rank_array)):
        # 判断上升趋势或者下降趋势
        if i > 0:
            if rank_array[i] - rank_array[i - 1] > 0:
                # 排名变差，置信区间变小
                rank_up = random.randint(1, 3)
                rank_up_array[i] = rank_array[i] - rank_down_array[i] + rank_up
            else:
                rank_up = random.randint(2, 6)
                rank_up_array[i] = rank_array[i] - rank_down_array[i] + rank_up
        else:
            rank_up_array[i] = rank_array[i] - rank_down_array[i] + 3
    print('上置信区间')
    print(rank_up_array)
    return rank_down_array, rank_up_array


def statistic_student_score(studentID):
    print('正在统计学生的成绩...')
    data_score = pd.read_csv(filepath_StudentsScore)
    data_student_info = pd.read_csv(filepath_StudentsInfo)
    # 去除掉没有成绩的数据
    data_score = data_score.dropna(subset=['mes_Z_Score'])

    # 得到这个学生所在的班级的人数
    class_name = data_student_info.drop(data_student_info[data_student_info['bf_StudentID'] != studentID].index)['cla_Name'].iloc[0]
    classmates_num = data_student_info.drop(data_student_info[data_student_info['cla_Name'] != class_name].index).shape[0]
    # print('班级的人数为', classmates_num)

    # 首先观察学生成绩的数量
    # 选取学号为14295的学生进行分析
    data_score['count'] = 1
    score_groupby_stdid = data_score.groupby(['mes_StudentID']).count().reset_index().sort_values(by='count', axis=0, ascending=False)
    # print(score_groupby_stdid)

    # 筛选这个学生的成绩
    student_score = data_score.drop(data_score[data_score['mes_StudentID'] != studentID].index)
    student_score = student_score.drop(student_score[student_score['mes_Score'] == -2].index)

    # 统计这个学生每一次考试的排名的情况并以数组形式保存
    # 获取每一次考试的考试ID
    score_groupby_examnum = student_score.groupby(['exam_number']).count().reset_index()
    # 统计每一次考试的排名情况
    exam_rank_array = []
    exam_score_array = []
    class_average_array = []
    exam_name_array = []
    for i in range(score_groupby_examnum.shape[0]):
        exam_score = student_score.drop(student_score[student_score['exam_number'] != score_groupby_examnum['exam_number'].iloc[i]].index)
        # print(exam_score)
        mes_sum = 0
        mes_score_sum = 0
        exam_name_array.append(score_groupby_examnum['exam_number'].iloc[i])
        for j in range(exam_score.shape[0]):
            mes_sum += exam_score['mes_dengdi'].iloc[j]
            mes_score_sum += exam_score['mes_T_Score'].iloc[j]
        average_rank = mes_sum / (exam_score.shape[0])
        average_score = mes_score_sum / (exam_score.shape[0])
        exam_rank_array.append(int(average_rank * classmates_num))
        exam_score_array.append(int(average_score))
        class_average_array.append(int(average_score + random.randint(-3, 3)))
    print('成绩的数组为：')
    # 计算总分
    for i in range(len(exam_score_array)):
        exam_score_array[i] = exam_score_array[i] * 6
    print(exam_score_array)
    print('班级平均分为：')
    for i in range(len(class_average_array)):
        class_average_array[i] = class_average_array[i] * 6
    print(class_average_array)
    print('排名的数组为')
    print(exam_rank_array)
    for i in range(len(exam_name_array)):
        for j in range(student_score.shape[0]):
            if exam_name_array[i] == student_score['exam_number'].iloc[j]:
                exam_name_array[i] = student_score['exam_numname'].iloc[j]
                break
    print('考试的学科名为：')
    print(exam_name_array)
    create_confidence_area(exam_rank_array)

    # 计算该学生的平均排名
    rank_sum = 0
    for i in range(len(exam_rank_array)):
        rank_sum += exam_rank_array[i]
    rank_average = rank_sum / len(exam_rank_array)
    print('该学生的平均排名为：', rank_average)
    # return rank_average


    # 统计这个学生的每一次考试各个科目的排名情况，并以数组的形式进行保存
    # 首先按照学科的类型对其进行groupby
    rank_array_new = []
    for i in range(len(subname)):
        student_sub_score = student_score.drop(student_score[student_score['mes_sub_name'] != subname[i]].index)
        sub_rank_array = []
        sub_examname_array = []
        for j in range(student_sub_score.shape[0]):
            # sub_score_array.append(student_sub_score['mes_dengdi'].iloc[j])
            sub_rank_array.append(int(float(student_sub_score['mes_dengdi'].iloc[j]) * classmates_num))
            sub_examname_array.append(student_sub_score['exam_numname'].iloc[j])
        if len(sub_rank_array) >= 18:
            rank_array_new_piece = []
            for j in range(18):
                rank_array_new_piece.append(sub_rank_array[j])
            rank_array_new.append(rank_array_new_piece)
        else:
            for j in range(18 - len(sub_rank_array)):
                sub_rank_array.append(sub_rank_array[0] + random.randint(-3, 3))
            rank_array_new.append(sub_rank_array)
        print(subname[i])
        print(sub_rank_array)
        print(sub_examname_array)
    print(rank_array_new)
    print(len(rank_array_new))

    # 产生雷达图的数据
    sub_radar_array_all = []
    for i in range(18):
        sub_radar_array = []
        for j in range(9):
            sub_radar_array.append(rank_array_new[j][i])
        sub_radar_array_all.append(sub_radar_array)
    print(sub_radar_array_all)
    xlabel_name_all = []
    for i in range(18):
        filename = 'const Score_' + str(i + 1) + ' = '
        print(filename, sub_radar_array_all[i], ';')
        xlabel_name = '考试' + str(i + 1)
        xlabel_name_all.append(xlabel_name)
    print(xlabel_name_all)
        # radar_array_name = 'radar_data_' + str(i + 1)

# statistic_student_score(14237)

# for i in range(50):
#     studentID = 14234 + i
#     rank_average = statistic_student_score(studentID)
#     if rank_average > 35:
#         print('找到那个啦')
#         print(studentID)
#         break

##############################################################################
# Chart_2
# 完成学生的各个科目的关联性验证

def statistic_sub_score_connection(studentID):
    # subname = ['数学', '生物']
    subname = ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理']
    print('正在产生学生成绩关联性验证数据...')
    data_score = pd.read_csv(filepath_StudentsScore)
    data_student_info = pd.read_csv(filepath_StudentsInfo)
    # 去除掉没有成绩的数据
    data_score = data_score.dropna(subset=['mes_Z_Score'])

    # 得到这个学生所在的班级的人数
    class_name = \
    data_student_info.drop(data_student_info[data_student_info['bf_StudentID'] != studentID].index)['cla_Name'].iloc[0]
    classmates_num = data_student_info.drop(data_student_info[data_student_info['cla_Name'] != class_name].index).shape[
        0]
    # print('班级的人数为', classmates_num)

    # 首先观察学生成绩的数量
    # 选取学号为14295的学生进行分析
    data_score['count'] = 1
    score_groupby_stdid = data_score.groupby(['mes_StudentID']).count().reset_index().sort_values(by='count', axis=0,
                                                                                                  ascending=False)
    # print(score_groupby_stdid)

    # 筛选这个学生的成绩
    student_score = data_score.drop(data_score[data_score['mes_StudentID'] != studentID].index)
    student_score = student_score.drop(student_score[student_score['mes_Score'] == -2].index)

    # 统计这个学生每一次考试的排名的情况并以数组形式保存
    # 获取每一次考试的考试ID
    score_groupby_examnum = student_score.groupby(['exam_number']).count().reset_index()

    # 统计这个学生的每一次考试各个科目的排名情况，并以数组的形式进行保存
    # 首先按照学科的类型对其进行groupby
    rank_array_new = []
    examname_array_new = []
    for i in range(len(subname)):
        student_sub_score = student_score.drop(student_score[student_score['mes_sub_name'] != subname[i]].index)
        sub_rank_array = []
        sub_examname_array = []
        for j in range(student_sub_score.shape[0]):
            sub_rank_array.append(round(float(student_sub_score['mes_T_Score'].iloc[j]), 2))
            # sub_rank_array.append(int(float(student_sub_score['mes_dengdi'].iloc[j]) * classmates_num))
            sub_examname_array.append(student_sub_score['exam_numname'].iloc[j])
        if len(sub_rank_array) >= 10:
            rank_array_new_piece = []
            examname_array_new_piece = []
            for j in range(10):
                rank_array_new_piece.append(sub_rank_array[j])
                examname_array_new_piece.append(sub_examname_array[j])
            rank_array_new.append(rank_array_new_piece)
            examname_array_new.append(examname_array_new_piece)
        else:
            for j in range(10 - len(sub_rank_array)):
                sub_rank_array.append(sub_rank_array[0] + random.randint(-3, 3))
                sub_examname_array.append(sub_examname_array[0])
            rank_array_new.append(sub_rank_array)
            examname_array_new.append(sub_examname_array)
        # print(subname[i])
        # print(rank_array_new_piece)
        # print(examname_array_new_piece)
    print(rank_array_new)
    return rank_array_new



# statistic_sub_score_connection(14237)

# 提取10个学生的10次考试成绩验证关联性
def extract_connection_data():
    subname = ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理']
    connection_data_1 = []
    connection_data_2 = []
    connection_data_3 = []
    connection_data_4 = []
    connection_data_5 = []
    connection_data_6 = []
    connection_data_7 = []
    connection_data_8 = []
    connection_data_9 = []

    for i in range(10):
        rank_array_c = statistic_sub_score_connection(14217 + i)
        connection_data_1.extend(rank_array_c[0]) # 10个学生的10次语文考试
        connection_data_2.extend(rank_array_c[1]) # 10个学生的10次语文考试
        connection_data_3.extend(rank_array_c[2]) # 10个学生的10次语文考试
        connection_data_4.extend(rank_array_c[3]) # 10个学生的10次语文考试
        connection_data_5.extend(rank_array_c[4]) # 10个学生的10次语文考试
        connection_data_6.extend(rank_array_c[5]) # 10个学生的10次语文考试
        connection_data_7.extend(rank_array_c[6]) # 10个学生的10次语文考试
        connection_data_8.extend(rank_array_c[7]) # 10个学生的10次语文考试
        connection_data_9.extend(rank_array_c[8]) # 10个学生的10次语文考试

    student_sub_score = []
    for i in range(100):
        student_sub_score_piece = []
        student_sub_score_piece.append(connection_data_1[i])
        student_sub_score_piece.append(connection_data_2[i])
        student_sub_score_piece.append(connection_data_3[i])
        student_sub_score_piece.append(connection_data_4[i])
        student_sub_score_piece.append(connection_data_5[i])
        student_sub_score_piece.append(connection_data_6[i])
        student_sub_score_piece.append(connection_data_7[i])
        student_sub_score_piece.append(connection_data_8[i])
        student_sub_score_piece.append(connection_data_9[i])
        student_sub_score.append(student_sub_score_piece)
    print('niubi')

    for i in range(len(student_sub_score)):
        for j in range(9):
            if student_sub_score[i][j] < 50 :
                student_sub_score[i][j] = 50

    print(student_sub_score)

extract_connection_data()

# rank_array_1 = []
# rank_array_2 = []
# for i in range(1):
#     rank_array_c = statistic_sub_score_connection(14217 + i)
#     rank_array_1.extend(rank_array_c[0])
#     rank_array_2.extend(rank_array_c[1])
# print(rank_array_1)
# # print('var A =', rank_array_1)
# print(rank_array_2)
# # print('var B =', rank_array_2)
# # print(len(rank_array_1), len(rank_array_2))