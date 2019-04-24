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

filepath_StudentsInfo_processed = '../../education_data/CH/Student/1.StudentInfo.csv'

filepath_AttendenceInfo = '../../education_data/3_kaoqin.csv'

filepath_StudentsScore = '../../education_data/5_chengji.csv'

filepath_StudentsConsumption = '../../education_data/7_consumption.csv'


##############################################################################
# 完成对学生所在的班级的授课教师的统计

# 定义一些常规变量
subname = ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理', '技术', '体育', '音乐']
# 统计一个学生所在的班级的各个学科的授课教师的信息
def statistic_teachers_info(studentID):
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

# statistic_teachers_info(14454)
# ['顾老师', '戴老师', '朱老师', '杨老师', '王老师', '陈老师', '冯老师', 'NaN', 'NaN', '庄老师', '效老师', '沈老师']
# 学科 语文 的教师是 顾老师
# 学科 数学 的教师是 戴老师
# 学科 英语 的教师是 朱老师
# 学科 物理 的教师是 杨老师
# 学科 化学 的教师是 王老师
# 学科 生物 的教师是 陈老师
# 学科 政治 的教师是 冯老师
# 学科 历史 的教师是 NaN
# 学科 地理 的教师是 NaN
# 学科 技术 的教师是 庄老师
# 学科 体育 的教师是 效老师
# 学科 音乐 的教师是 沈老师

# 统计一个学生的基本信息
# 统计学生的姓名、学号、性别、民族、班级名、出生日期、籍贯、政治面貌、住宿信息（寝室号、人数）

##############################################################################
# 完成对学生的个人信息的统计

# 首先需要对数据进行预处理与保存
def data_preprocess_studentInfo():
    data_StudentInfo = pd.read_csv(filepath_StudentsInfo)
    # 去除掉姓名为空的数据
    # 填充缺失数据
    data_StudentInfo['bf_BornDate'] = data_StudentInfo['bf_BornDate'].fillna(method='pad')
    data_StudentInfo['bf_qinshihao'] = data_StudentInfo['bf_qinshihao'].fillna(-1)
    data_StudentInfo['bf_zhusu'] = data_StudentInfo['bf_zhusu'].fillna(-1)
    # 处理出生地错误的数据
    data_StudentInfo = data_StudentInfo.drop(data_StudentInfo[data_StudentInfo['bf_NativePlace'] == '汉族'].index)
    data_StudentInfo = data_StudentInfo.drop(data_StudentInfo[data_StudentInfo['bf_NativePlace'] == '汉'].index)
    # 保存
    data_StudentInfo.to_csv('../../education_data/CH/Student/1.StudentInfo.csv', encoding='utf_8_sig')
    print('文件保存完成！')
# data_preprocess_studentInfo()

# 读取已经处理后的数据
studentInfo_field = ['姓名', '学号', '性别', '民族', '班级名', '出生日期', '籍贯', '政治面貌', '住宿信息', '寝室号', '寝室人数']
# print(len(studentInfo_field))
def statistic_student_info(studentID):
    data_StudentInfo = pd.read_csv(filepath_StudentsInfo_processed)
    # 初始化数组
    studentInfo_Array = ['NaN'] * 11
    # 提取相应学号的学生
    studentInfo = data_StudentInfo.drop(data_StudentInfo[data_StudentInfo['bf_StudentID'] != studentID].index)
    studentInfo_Array[0] = studentInfo['bf_Name'].iloc[0]
    studentInfo_Array[1] = studentInfo['bf_StudentID'].iloc[0]
    studentInfo_Array[2] = studentInfo['bf_sex'].iloc[0]
    studentInfo_Array[3] = studentInfo['bf_nation'].iloc[0]
    studentInfo_Array[4] = studentInfo['cla_Name'].iloc[0]
    studentInfo_Array[5] = str(int(studentInfo['bf_BornDate'].iloc[0])) + '年'
    studentInfo_Array[6] = studentInfo['bf_NativePlace'].iloc[0]
    studentInfo_Array[7] = studentInfo['bf_policy'].iloc[0]
    studentInfo_Array[8] = '非住校'
    if studentInfo['bf_zhusu'].iloc[0] == 1:
        studentInfo_Array[8] = '住校'
        if studentInfo['bf_qinshihao'].iloc[0] != 'Null':
            studentInfo_Array[9] = str(int(studentInfo['bf_qinshihao'].iloc[0])) + '号'
            roomNumber = studentInfo['bf_qinshihao'].iloc[0]
            data_groupbyRoomNum = data_StudentInfo.drop(data_StudentInfo[data_StudentInfo['bf_qinshihao'] != roomNumber].index)
            studentInfo_Array[10] = data_groupbyRoomNum.shape[0]
    print(studentInfo_Array)

# statistic_student_info(14572)

# data_StudentInfo = pd.read_csv(filepath_StudentsInfo_processed)
# for i in range(300):
#     studentID = data_StudentInfo['bf_StudentID'].iloc[i]
#     statistic_student_info(studentID)

##############################################################################
# 统计每个班级的人数

def statistic_class_studentsNum():
    data_studentsInfo = pd.read_csv(filepath_StudentsInfo)
    class_name = []
    students_num = []
    data_studentsInfo['count'] = 1
    class_studentsNum = data_studentsInfo.groupby(['cla_Name']).count().reset_index()
    class_studentsNum = class_studentsNum.drop(class_studentsNum[class_studentsNum['count'] < 30].index)
    for i in range(class_studentsNum.shape[0]):
        class_name.append(class_studentsNum['cla_Name'].iloc[i])
        students_num.append(class_studentsNum['count'].iloc[i])
    print(class_name)
    print(students_num)

# statistic_class_studentsNum()
# ['东-高一(01)', '东-高一(02)', '东-高一(03)', '东-高一(04)', '东-高一(05)', '东-高一(06)', '东-高一(07)', '东-高一(08)', '东-高一(09)-IB', '东-高一(10)-IB', '白-高一(01)', '白-高一(02)', '白-高一(03)', '白-高一(04)', '白-高一(05)', '白-高一(06)', '白-高一(07)', '白-高一(08)', '白-高二(01)', '白-高二(02)', '白-高二(03)', '白-高二(04)', '白-高二(05)', '白-高二(06)', '白-高二(07)', '白-高二(08)', '白-高二(09)', '白-高二(10)', '白-高二(12)', '高三(01)', '高三(02)', '高三(03)', '高三(04)', '高三(05)', '高三(06)', '高三(07)', '高三(08)', '高三(09)', '高三(10)', '高三(11)IB', '高三(12)IB', '高二(13)IB']
# [40, 40, 40, 40, 38, 33, 40, 40, 32, 33, 43, 43, 45, 43, 45, 46, 30, 30, 47, 44, 44, 44, 43, 45, 44, 40, 43, 43, 31, 47, 41, 42, 44, 44, 44, 42, 45, 41, 45, 37, 35, 57]

##############################################################################
# 统计学生的考勤信息，用于展示展示学生的考勤记录，迟到、早退、校服校徽的情况统计
# 统计学生所在的班级处于的水平与学生数据形成对比
# 统计学生正常进出校园的时间统计

# 统计学生考勤数据集和学生信息的数据集的耦合情况
def statistic_students_attendance():
    data_attendance = pd.read_csv(filepath_AttendenceInfo)
    data_studentInfo = pd.read_csv(filepath_StudentsInfo)
    # 首先通过goupby统计考勤数据集中有多少组学生的数据
    data_attendance['count'] = 1
    data_attendance_grounpby = data_attendance.groupby(['bf_studentID']).count().reset_index().sort_values(by='count', axis=0, ascending=False)
    # 统计得到的数据有3058条
    # 对数据进行筛选，选取前300个学生的数据
    data_attendance_grounpby = data_attendance_grounpby.iloc[0: 100]
    # 验证这300个数据是否有学生信息
    studentID_Array = []
    count = 0
    for i in range(data_attendance_grounpby.shape[0]):
        studentID_Array.append(data_attendance_grounpby['bf_studentID'].iloc[i])
    for i in range(len(studentID_Array)):
        for j in range(data_studentInfo.shape[0]):
            if studentID_Array[i] == data_studentInfo['bf_StudentID'].iloc[j]:
                print(studentID_Array[i])
                count += 1
    # 考勤中的数据存在的，在studentinfo中只有76组
    print(count)
    print(data_attendance_grounpby.iloc[99])
    print(data_attendance_grounpby.shape)

# statistic_students_attendance()
# 学生的考勤数据和学生信息的数据耦合程度较差

# 使用学号为14856的学生为例子
def statistic_student_attendance(studentID):
    data_attendance = pd.read_csv(filepath_AttendenceInfo)
    student_attendance = data_attendance.drop(data_attendance[data_attendance['bf_studentID'] != studentID].index)
    # 首先统计该学生的考勤记录
    # 统计该学生的迟到、早退、校服校徽问题
    late_taskName = [100100, 9900100, 10020]
    early_taskName = [200200, 9900300]
    uniform_taskName = [200100, 9900200]
    student_problems_num = [0] * 3
    class_problems_num = [0] * 3
    for i in range(len(late_taskName)):
        student_attendance_late = student_attendance.drop(student_attendance[student_attendance['control_task_order_id'] != late_taskName[i]].index)
        student_problems_num[0] = student_attendance_late.shape[0]
    for i in range(len(early_taskName)):
        student_attendance_early = student_attendance.drop(student_attendance[student_attendance['control_task_order_id'] != early_taskName[i]].index)
        student_problems_num[1] = student_attendance_early.shape[0]
    for i in range(len(uniform_taskName)):
        student_attendance_uniform = student_attendance.drop(student_attendance[student_attendance['control_task_order_id'] != uniform_taskName[i]].index)
        student_problems_num[2] = student_attendance_uniform.shape[0]
    print(student_problems_num)

    # 统计该学生所在的班级的考勤的情况
    student_classid = student_attendance['bf_classid'].iloc[0]
    print(student_classid)
    class_attendance = data_attendance.drop(data_attendance[data_attendance['bf_classid'] != student_classid].index)
    print(class_attendance.shape[0])
    for i in range(len(late_taskName)):
        class_attendance_late = class_attendance.drop(class_attendance[class_attendance['control_task_order_id'] != late_taskName[i]].index)
        class_problems_num[0] = class_attendance_late.shape[0]
    for i in range(len(early_taskName)):
        class_attendance_early = class_attendance.drop(class_attendance[class_attendance['control_task_order_id'] != early_taskName[i]].index)
        class_problems_num[1] = class_attendance_early.shape[0]
    for i in range(len(uniform_taskName)):
        class_attendance_uniform = class_attendance.drop(class_attendance[class_attendance['control_task_order_id'] != uniform_taskName[i]].index)
        class_problems_num[2] = class_attendance_uniform.shape[0]
    print(class_problems_num)

    # 统计该学生的一天的考勤的情况
    # 统计学生每天早晨上学期间的打卡记录，以及晚上放学的打卡记录，并与班级的平均水平进行对比
    print(student_attendance)

statistic_student_attendance(14856)