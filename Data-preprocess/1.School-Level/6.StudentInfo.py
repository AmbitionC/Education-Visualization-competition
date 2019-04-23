#-*- coding:utf-8 -*-

'''
# Author: chenhao
# Date: April. 23
# Description: Data-process for Education visualization competition
'''

##############################################################################
#Part6：统计学生层次的数据
##############################################################################

import pandas as pd
import numpy as np
import json

# 读取原始的数据集
filepath_TeacherInfo = '../../education_data/1_teacher.csv'

filepath_StudentsInfo = '../../education_data/2_student_info.csv'

filepath_AttendenceInfo = '../../education_data/3_kaoqin.csv'

filepath_StudentsScore = '../../education_data/5_chengji.csv'

filepath_StudentsConsumption = '../../education_data/7_consumption.csv'

# 统计一个学生所在的班级的各个学科的授课教师的信息
def statistic_teachers_info(studentID):
    subname = ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理', '技术', '体育', '音乐']
    data_StudentInfo = pd.read_csv(filepath_StudentsInfo)
    data_TeacherInfo = pd.read_csv(filepath_TeacherInfo)
    teacherName = ['NaN'] * 12
    studentInfo = data_StudentInfo.drop(data_StudentInfo[data_StudentInfo['bf_StudentID'] != studentID].index)
    if studentInfo.shape[0] == 0:
        print('没有该学生的信息，请重新输入！')
    else:
        classID = studentInfo['cla_id'].iloc[0]
        teacherInfo = data_TeacherInfo.drop(data_TeacherInfo[data_TeacherInfo['cla_id'] != classID].index)
        for i in range(len(subname)):
            for j in range(teacherInfo.shape[0]):
                if subname[i] == teacherInfo['sub_Name'].iloc[j]:
                    teacherName[i] = teacherInfo['bas_Name'].iloc[j]
        print(teacherName)
        for i in range(len(teacherName)):
            print('学科', subname[i], '的教师是', teacherName[i])
        return teacherName


statistic_teachers_info(14454)