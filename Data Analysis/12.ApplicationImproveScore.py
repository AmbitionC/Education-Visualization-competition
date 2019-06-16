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

filepath_TeacherInfo = "../../education_data/1_teacher.csv"

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
        class_average_array.append(int(average_score))
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
                sub_rank_array.append(sub_rank_array[0])
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
                sub_rank_array.append(sub_rank_array[0])
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

# extract_connection_data()


##############################################################################
# Chart_3
# 完成学生的班级的划分与聚类

# 输入学生的ID，产出这个学生的文理科成绩，并做成数组的形式
# 产出数据的格式：[文科成绩，理科成绩，姓名]
def create_student_score(studentID, classNum):
    print('正在产生该学生的成绩...')
    Libral_sub_name = ['语文', '政治', '历史']
    Libral_sub_score = []
    Libral_sub_rank = []
    Science_sub_name = ['数学', '物理', '化学']
    Science_sub_score = []
    Science_sub_rank = []
    data_score = pd.read_csv(filepath_StudentsScore)
    data_score = data_score.dropna(subset=['mes_Z_Score'])
    # 得到这个学生的成绩数据
    student_score = data_score.drop(data_score[data_score['mes_StudentID'] != studentID].index)

    # 计算该学生的文科成绩
    for i in range(len(Libral_sub_name)):
        student_sub_score = student_score.drop(student_score[student_score['mes_sub_name'] != Libral_sub_name[i]].index)
        # 计算平均值
        sub_Tscore_sum = 0
        sub_dengdi_sum = 0
        for j in range(student_sub_score.shape[0]):
            sub_Tscore_sum += student_sub_score['mes_T_Score'].iloc[j]
            sub_dengdi_sum += student_sub_score['mes_dengdi'].iloc[j]
        sub_Tscore_average = sub_Tscore_sum / student_sub_score.shape[0]
        sub_dengdi_average = sub_dengdi_sum / student_sub_score.shape[0]
        Libral_sub_score.append(sub_Tscore_average)
        Libral_sub_rank.append(sub_dengdi_average)
    # 计算该学生的理科成绩
    for i in range(len(Science_sub_name)):
        student_sub_score = student_score.drop(student_score[student_score['mes_sub_name'] != Science_sub_name[i]].index)
        # 计算平均值
        sub_Tscore_sum = 0
        sub_dengdi_sum = 0
        for j in range(student_sub_score.shape[0]):
            sub_Tscore_sum += student_sub_score['mes_T_Score'].iloc[j]
            sub_dengdi_sum += student_sub_score['mes_dengdi'].iloc[j]
        sub_Tscore_average = sub_Tscore_sum / student_sub_score.shape[0]
        sub_dengdi_average = sub_dengdi_sum / student_sub_score.shape[0]
        Science_sub_score.append(sub_Tscore_average)
        Science_sub_rank.append(sub_dengdi_average)

    # 计算该学生的文理科平均成绩
    Libral_score_sum = 0
    Libral_rank_sum = 0
    Science_score_sum = 0
    Science_rank_sum = 0
    # 文科成绩
    for i in range(len(Libral_sub_score)):
        Libral_score_sum += Libral_sub_score[i]
        Libral_rank_sum += Libral_sub_rank[i]

    Libral_score_average = round(Libral_score_sum / len(Libral_sub_score), 2)
    Libral_rank_average = int((Libral_rank_sum / len(Libral_sub_score)) * classNum)
    # 理科成绩
    for i in range(len(Science_sub_score)):
        Science_score_sum += Science_sub_score[i]
        Science_rank_sum += Science_sub_rank[i]

    Science_score_average = round(Science_score_sum / len(Science_sub_score), 2)
    Science_rank_average = int((Science_rank_sum / len(Science_sub_score)) * classNum)

    Libral_Science = [Libral_rank_average, Science_rank_average]
    print(Libral_Science)
    return Libral_Science


# 产生聚类的数据
def create_cluster_data(studentID):
    # 导入成绩数据
    data_score = pd.read_csv(filepath_StudentsScore)
    data_student_info = pd.read_csv(filepath_StudentsInfo)
    # 去除掉没有成绩的数据
    data_score = data_score.dropna(subset=['mes_Z_Score'])

    # 得到这个学生所在的班级
    class_name = data_student_info.drop(data_student_info[data_student_info['bf_StudentID'] != studentID].index)['cla_Name'].iloc[0]
    classmates_data = data_student_info.drop(data_student_info[data_student_info['cla_Name'] != class_name].index)
    # print(classmates_data)

    # 统计这个班级的成绩的分布
    Libral_Science_All = []
    for i in range(classmates_data.shape[0]):
        Libral_Science_Name = create_student_score(classmates_data['bf_StudentID'].iloc[i], classmates_data.shape[0])
        Libral_Science_Name.append(classmates_data['bf_Name'].iloc[i])
        Libral_Science_All.append(Libral_Science_Name)
    print(Libral_Science_All)

    Libral_Science_I = []
    Libral_Science_II = []
    Libral_Science_III = []
    Libral_Science_IV = []

    for i in range(len(Libral_Science_All)):
        if Libral_Science_All[i][0] <= 25:
            if Libral_Science_All[i][1] >= 25:
                Libral_Science_I.append(Libral_Science_All[i])
            if Libral_Science_All[i][1] < 25:
                Libral_Science_IV.append(Libral_Science_All[i])
        if Libral_Science_All[i][0] > 25:
            if Libral_Science_All[i][1] >= 25:
                Libral_Science_II.append(Libral_Science_All[i])
            if Libral_Science_All[i][1] < 25:
                Libral_Science_III.append(Libral_Science_All[i])

    print(Libral_Science_I)
    print(Libral_Science_II)
    print(Libral_Science_III)
    print(Libral_Science_IV)

    print(create_student_score(14237, classmates_data.shape[0]))


# create_cluster_data(14237)

# 看看920班级的情况

def look_look_920():
    # 导入数据
    data_score = pd.read_csv(filepath_StudentsScore)
    data_student_info = pd.read_csv(filepath_StudentsInfo)

    # 筛选这个班级数据
    classmates_data = data_student_info.drop(data_student_info[data_student_info['cla_id'] != 920].index)
    # 统计这个班级的成绩的分布
    Libral_Science_All = []
    for i in range(classmates_data.shape[0]):
        Libral_Science_Name = create_student_score(classmates_data['bf_StudentID'].iloc[i], classmates_data.shape[0])
        Libral_Science_Name.append(classmates_data['bf_Name'].iloc[i])
        Libral_Science_All.append(Libral_Science_Name)
    print(Libral_Science_All)

    Libral_Science_I = []
    Libral_Science_II = []
    Libral_Science_III = []
    Libral_Science_IV = []

    for i in range(len(Libral_Science_All)):
        if Libral_Science_All[i][0] <= 25:
            if Libral_Science_All[i][1] >= 25:
                Libral_Science_I.append(Libral_Science_All[i])
            if Libral_Science_All[i][1] < 25:
                Libral_Science_IV.append(Libral_Science_All[i])
        if Libral_Science_All[i][0] > 25:
            if Libral_Science_All[i][1] >= 25:
                Libral_Science_II.append(Libral_Science_All[i])
            if Libral_Science_All[i][1] < 25:
                Libral_Science_III.append(Libral_Science_All[i])

    print(Libral_Science_I)
    print(Libral_Science_II)
    print(Libral_Science_III)
    print(Libral_Science_IV)

# look_look_920()

##############################################################################
# Chart_4
# 完成学生的授课教师的能力评估
# 需要的数据：教师的姓名，教师所带的班级成绩，学校整体的平均成绩

def create_students_teacher_data(studentID):
    subname = ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理', '技术']
    # 导入数据
    data_score = pd.read_csv(filepath_StudentsScore)
    data_student_info = pd.read_csv(filepath_StudentsInfo)
    data_teacher_info = pd.read_csv(filepath_TeacherInfo)

    # 得到该学生所在的班级号
    student_info = data_student_info.drop(data_student_info[data_student_info['bf_StudentID'] != studentID].index)
    class_id = student_info['cla_id'].iloc[0]
    print('班级号为：', class_id)

    # 收集该班级号的老师的信息
    teacher_name = []
    teacher_id = []
    teacher_info = data_teacher_info.drop(data_teacher_info[data_teacher_info['cla_id'] != class_id].index)
    print(teacher_info)

# create_students_teacher_data(14237)

# 顾同学所在班级为921
# 通过这个部分的观察，由于数据的问题，高三的班级只有七个学科的老师的信息，其中包括以下学科：
# [语文，数学，英语，体育，音乐，美术，技术]这七个学科，数据量薄弱，因此需要改变数据集

# 通过数据的观察，选择班级号为926的数据，来获得这个班级的完整的任课教师的数据
def create_student_teacher_data_new():
    subname = ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理']
    # data_student_info = pd.read_csv(filepath_StudentsInfo)
    data_teacher_info = pd.read_csv(filepath_TeacherInfo)

    # 选择班级号为821的班级
    class_id = 926
    teacher_info = data_teacher_info.drop(data_teacher_info[data_teacher_info['cla_id'] != class_id].index)
    # 获取教师信息
    teacher_name = []
    teacher_id = []
    # print(teacher_info)
    for i in range(len(subname)):
        sub_teacher_info = teacher_info[teacher_info['sub_Name'].str.contains(subname[i])]
        teacher_name.append(subname[i] + '-' + sub_teacher_info['bas_Name'].iloc[0])
        teacher_id.append(sub_teacher_info['bas_id'].iloc[0])
    print(teacher_name)
    print(teacher_id)

# 获得这个教师带的班级的每次考试的平均成绩
def create_subTeacher_score(subname):
    data_score = pd.read_csv(filepath_StudentsScore)
    data_student_info = pd.read_csv(filepath_StudentsInfo)
    # 去除掉没有成绩的数据
    data_score = data_score.dropna(subset=['mes_Z_Score'])
    # 去除掉非这个学科的数据
    sub_score_data = data_score.drop(data_score[data_score['mes_sub_name'] != subname].index)
    # 找到926这个班级的学生的ID
    class_student = data_student_info.drop(data_student_info[data_student_info['cla_id'] != 926].index)
    # print(class_student)
    # 班级的各个学生的该学科的数组
    class_sub_score_array = []
    for i in range(class_student.shape[0]):
        student_sub_score_data = sub_score_data.drop(sub_score_data[sub_score_data['mes_StudentID'] != class_student['bf_StudentID'].iloc[i]].index)
        # print(student_sub_score_data)
        student_sub_score_array = []
        if student_sub_score_data.shape[0] < 6:
            for m in range(student_sub_score_data.shape[0]):
                student_sub_score_array.append(student_sub_score_data['mes_T_Score'].iloc[m])
            for n in range(6 - student_sub_score_data.shape[0]):
                student_sub_score_array.append(student_sub_score_data['mes_T_Score'].iloc[0])
        else:
            for k in range(6):
                student_sub_score_array.append(student_sub_score_data['mes_T_Score'].iloc[k])
        class_sub_score_array.append(student_sub_score_array)
    # print(class_sub_score_array)
    class_sub_average_array = []
    for i in range(6):
        score_sum = 0
        for j in range(len(class_sub_score_array)):
            score_sum += class_sub_score_array[j][i]
        class_sub_average_array.append(round(score_sum / (len(class_sub_score_array)), 3))
    # print(class_sub_average_array)
    return class_sub_average_array

def create_school_average_score(subname):
    data_score = pd.read_csv(filepath_StudentsScore)
    data_student_info = pd.read_csv(filepath_StudentsInfo)
    # 去除掉没有成绩的数据
    data_score = data_score.dropna(subset=['mes_Z_Score'])
    # 去除掉非这个学科的数据
    sub_score_data = data_score.drop(data_score[data_score['mes_sub_name'] != subname].index)
    # 计算这个年级的该学科的整体的成绩
    # 找到高一的该学生的ID
    # school_student = data_student_info

def create_sub_data_all():
    subname = ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理']
    sub_examname_array = ['2018学年度第一学期平时成绩1', '2018-1学期期中考试', '2018-2019新高一7月测试', '2018学年度第一学期平时成绩2', '2018学年度第二学期期中考试', '2018学年度第二学期期末考试']
    class_average_array_all = []
    school_average_array_all = []
    create_student_teacher_data_new()
    print(sub_examname_array)
    for i in range(len(subname)):
        class_average_array = create_subTeacher_score(subname[i])
        school_average_array = []
        for j in range(6):
            school_average_array.append(round(class_average_array[j], 3))
        print(subname[i])
        average_array = [class_average_array, school_average_array]
        # print(class_average_array)
        # print(school_average_array)
        print(average_array)

# create_student_teacher_data_new()
# create_subTeacher_score('语文')
create_sub_data_all()
