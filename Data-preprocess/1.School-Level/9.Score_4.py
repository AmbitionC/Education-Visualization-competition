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
import json

# 读取原始的数据集
filename_score = '../../education_data/5_chengji.csv'

filename_student_info = '../../education_data/2_student_info.csv'

exam_name_filtered = [265, 266, 267, 269, 271, 277, 279, 280, 281, 284, 285, 286, 287, 288, 289, 291, 292, 293, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308]

score_categories = ['mes_Score', 'mes_T_Score', 'mes_dengdi']

score_category = score_categories[2]

def extract_exam_data(exam_name):
    data_score = pd.read_csv(filename_score)
    data_student_info = pd.read_csv(filename_student_info)
    data_exam = data_score.drop(data_score[data_score['exam_number'] != exam_name].index)
    data_merge_byStdID = pd.merge(data_exam, data_student_info, left_on='mes_StudentID', right_on='bf_StudentID', how='left')
    data_merge_byStdID = data_merge_byStdID.drop(['bf_Name', 'mes_TestID', 'exam_number', 'bf_sex', 'bf_nation', 'bf_BornDate', 'bf_NativePlace', 'Bf_ResidenceType', 'bf_policy', 'cla_term', 'bf_zhusu', 'bf_leaveSchool', 'bf_qinshihao'], axis=1)
    data_merge_byStdID = data_merge_byStdID.dropna(subset=['cla_Name'])
    # print(data_merge_byStdID)
    return data_merge_byStdID

# 产生一个学生的十个学科的成绩
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


def split_data_byGrade():
    grade = ['高一', '高二', '高三']
    # grade = ['高二']
    data_merge_byStdID = extract_exam_data(303)
    for j in range(len(grade)):
        cla_Name = []
        data_split_byGrade = data_merge_byStdID[data_merge_byStdID['cla_Name'].str.contains(grade[j])]
        # 删除白高二一班数据
        data_split_byGrade = data_split_byGrade.drop(data_split_byGrade[data_split_byGrade['cla_Name'] == '白-高二(01)'].index)
        data_split_byGrade = data_split_byGrade.drop(data_split_byGrade[data_split_byGrade['cla_Name'] == '高二未分班'].index)
        data_split_byGrade[score_category] = data_split_byGrade[score_category].fillna(method='pad')
        # 获得班级名
        data_claName_byGrade = data_split_byGrade.groupby('cla_Name').count().reset_index()
        # print(data_claName_byGrade)
        for k in range(data_claName_byGrade.shape[0]):
            cla_Name.append(data_claName_byGrade['cla_Name'].iloc[k])
        # 按照学生ID来划分
        score_grade = generate_data_byStdID(data_split_byGrade)
        print(cla_Name)
        print(score_grade)
        print(len(score_grade))
        score_grade_new = []
        for i in range(len(score_grade)):
            if i % 2 == 1:
                score_grade_new.append(score_grade[i])
        print(len(score_grade_new))
        # 存储数据
        json_data = {'xAxis': cla_Name, 'score_total': score_grade_new}
        print(json_data)
        filepath = '../1.School-Level-data/4.Score_cla_total_' + str(j) + '.json'
        with open(filepath, 'w') as file:
            json.dump(json_data, file)
        print('完成文件加载')

split_data_byGrade()
