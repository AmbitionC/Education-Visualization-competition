#-*- coding:utf-8 -*-

'''
# Author: chenhao
# Date: April. 14
# Description: Data-process for Education visualization competition
'''

##############################################################################
#Part4：统计学校的学生成绩
##############################################################################

import pandas as pd
import numpy as np
import json

# 读取原始的数据集
data_orgin = pd.read_csv('../../education_data/5_chengji.csv')

data_student_info = pd.read_csv('../../education_data/2_student_info.csv')

exam_name_filtered = [265, 266, 267, 269, 271, 277, 279, 280, 281, 284, 285, 286, 287, 288, 289, 291, 292, 293, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308]

score_categories = ['mes_Score', 'mes_T_Score', 'mes_dengdi']

score_category = score_categories[2]

def extract_exam_id():
    data_exam = data_orgin.groupby(['exam_number']).count().reset_index()
    exam_name = []
    for i in range(data_exam.shape[0]):
        exam_name.append(data_exam['exam_number'].iloc[i])
    # print(exam_name)
    return exam_name

# 该函数用来得到考试类型的ID
# 返回的值为[221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 277, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308]

def verify_exam_NaN():
    exam_name = extract_exam_id()
    exam_name_verified = []
    for i in range(len(exam_name)):
        data_exam = data_orgin.drop(data_orgin[data_orgin['exam_number'] != exam_name[i]].index)
        data_merge_byStdID = pd.merge(data_exam, data_student_info, left_on='mes_StudentID', right_on='bf_StudentID', how='left')
        data_merge_byStdID = data_merge_byStdID.dropna(subset=['cla_Name'])
        if data_merge_byStdID.shape[0] != 0:
            exam_name_verified.append(exam_name[i])
    print(exam_name_verified)
    return exam_name_verified

# verify_exam_NaN()
# 该函数用来返回考试类型与学生id进行合并后班级信息不为空的考试类型
# [250, 252, 253, 254, 257, 261, 262, 263, 265, 266, 267, 269, 271, 277, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308]

def acquire_dataset_size():
    exam_name_filter = []
    for i in range(len(exam_name_filtered)):
        data_exam = data_orgin.drop(data_orgin[data_orgin['exam_number'] != exam_name_filtered[i]].index)
        data_merge_byStdID = pd.merge(data_exam, data_student_info, left_on='mes_StudentID', right_on='bf_StudentID', how='left')
        data_merge_byStdID = data_merge_byStdID.dropna(subset=['cla_Name'])
        print('考试号为', exam_name_filtered[i], '的数据量为', data_merge_byStdID.shape[0])
        if data_merge_byStdID.shape[0] >= 1000:
            exam_name_filter.append(exam_name_filtered[i])
    print(exam_name_filter)

# acquire_dataset_size()
# 该函数用来返回每一次考试的数据量
# 考试号为 265 的数据量为 3951
# 考试号为 266 的数据量为 1301
# 考试号为 267 的数据量为 4165
# 考试号为 269 的数据量为 3944
# 考试号为 271 的数据量为 4277
# 考试号为 277 的数据量为 1483
# 考试号为 279 的数据量为 4279
# 考试号为 280 的数据量为 4043
# 考试号为 281 的数据量为 3879
# 考试号为 284 的数据量为 7467
# 考试号为 285 的数据量为 7393
# 考试号为 286 的数据量为 1901
# 考试号为 287 的数据量为 7699
# 考试号为 288 的数据量为 8725
# 考试号为 289 的数据量为 8721
# 考试号为 291 的数据量为 8701
# 考试号为 292 的数据量为 6684
# 考试号为 293 的数据量为 1142
# 考试号为 297 的数据量为 4165
# 考试号为 298 的数据量为 8701
# 考试号为 299 的数据量为 8701
# 考试号为 300 的数据量为 5724
# 考试号为 301 的数据量为 3400
# 考试号为 302 的数据量为 3400
# 考试号为 303 的数据量为 12544
# 考试号为 304 的数据量为 9866
# 考试号为 305 的数据量为 11870
# 考试号为 306 的数据量为 3673
# 考试号为 307 的数据量为 11015
# 考试号为 308 的数据量为 5670
# [265, 266, 267, 269, 271, 277, 279, 280, 281, 284, 285, 286, 287, 288, 289, 291, 292, 293, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308]

def extract_exam_data(exam_name):
    data_exam = data_orgin.drop(data_orgin[data_orgin['exam_number'] != exam_name].index)
    data_merge_byStdID = pd.merge(data_exam, data_student_info, left_on='mes_StudentID', right_on='bf_StudentID', how='left')
    data_merge_byStdID = data_merge_byStdID.drop(['bf_Name', 'mes_TestID', 'exam_number', 'bf_sex', 'bf_nation', 'bf_BornDate', 'bf_NativePlace', 'Bf_ResidenceType', 'bf_policy', 'cla_term', 'bf_zhusu', 'bf_leaveSchool', 'bf_qinshihao'], axis=1)
    data_merge_byStdID = data_merge_byStdID.dropna(subset=['cla_Name'])
    # print(data_merge_byStdID)
    return data_merge_byStdID

# extract_exam_data()
# 该函数用来提取考试类型的数据并与学生info合并，以data_exam形式存储，如果需要全体的数据则需要通过循环遍历exam_name

def generate_data_byStdID(data_split_byGrade):
    sub_name = ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理', '技术']
    data_group_byStuID = data_split_byGrade.groupby('mes_StudentID').count().reset_index()
    score_grade = []
    for i in range(data_group_byStuID.shape[0]):
        # 按照学生ID划分，一个学生的各科考试成绩放到data_split_byStuID
        data_split_byStuID = data_split_byGrade.drop(data_split_byGrade[data_split_byGrade['mes_StudentID'] != data_group_byStuID['mes_StudentID'].iloc[i]].index)
        # 将每一个学科数据按照顺序进行保存
        score_stuID = ['NaN'] * 10
        for j in range(data_split_byStuID.shape[0]):
            for k in range(len(sub_name)):
                if data_split_byStuID['mes_sub_name'].iloc[j] == sub_name[k]:
                    score_stuID[k] = data_split_byStuID[score_category].iloc[j]
        score_stuID.append(int(data_split_byStuID['mes_StudentID'].iloc[0]))
        score_stuID.append(data_split_byStuID['cla_Name'].iloc[0])
        score_grade.append(score_stuID)
    return score_grade

# 该函数用来得到一个年级的成绩状况

def split_data_byGrade():
    grade = ['高一', '高二', '高三']
    data_merge_byStdID = extract_exam_data(303)
    for j in range(len(grade)):
        cla_Name = []
        data_split_byGrade = data_merge_byStdID[data_merge_byStdID['cla_Name'].str.contains(grade[j])]
        data_split_byGrade[score_category] = data_split_byGrade[score_category].fillna(method='pad')
        # 获得班级名
        data_claName_byGrade = data_split_byGrade.groupby('cla_Name').count().reset_index()
        for k in range(data_claName_byGrade.shape[0]):
            cla_Name.append(data_claName_byGrade['cla_Name'].iloc[k])
        # 按照学生ID来划分
        score_grade = generate_data_byStdID(data_split_byGrade)
        print(cla_Name)
        # 存储数据
        json_data = {'xAxis': cla_Name, 'score_total': score_grade}
        filepath = '../1.School-Level-data/4.Score_cla_total_' + str(j) + '.json'
        with open(filepath, 'w') as file:
            json.dump(json_data, file)
        print('完成文件加载')

split_data_byGrade()



