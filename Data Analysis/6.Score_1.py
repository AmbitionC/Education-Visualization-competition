#-*- coding:utf-8 -*-

'''
# Author: chenhao
# Date: April. 2
# Description: Data-process for Education visualization competition
'''

##############################################################################
#Part4：统计学校的学生成绩
##############################################################################

import pandas as pd
import numpy as np
import json

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

# 读取原始数据集合
data_origin = pd.read_csv('../../education_data/5_chengji.csv')

data_sample = pd.read_csv('../../education_data/CH/5.chengji_1.csv')

data_student_info = pd.read_csv('../../education_data/2_student_info.csv')

data_merge_byStdId = pd.read_csv('../../education_data/CH/5.chengji_2_claID.csv')


##############################################################################
#Step1: 找到考试数据最多的那一次考试

def find_datamax_exam():
    data_origin['sum'] = 1
    data_max_exam = data_origin.groupby(['exam_numname']).count().reset_index().sort_values(by='sum', axis=0, ascending=False)
    print(data_max_exam)

find_datamax_exam()
# find_datamax_exam()
# 考试数据最多的一次考试为2017学年度第一学期期末考试和2017学年度第一学期期末总评
# \t2017学年度第一学期期末考试 数据量为13168
# 2017学年度第一学期期末总评 数据量为13161


##############################################################################
#Step2：剔除其他的数据，观察2017学年度第一学期期末两次考试的数据

def find_2017_finalExam():
    exam_name = '2017学年度第一学期期末总评'
    data_2017_finalExam = data_origin[data_origin['exam_numname'].str.contains(exam_name)]
    # data_2017_finalExam = data_2017_finalExam.groupby(['exam_numname']).count().reset_index()
    print(data_2017_finalExam.shape)
    data_2017_finalExam.to_csv('../../education_data/CH/5.chengji_1.csv', encoding='utf_8_sig')

# find_2017_finalExam()

# find_2017_finalExam()

##############################################################################
#Step3：确定使用2017学年度第一学期期末总评作为样本数据

def statistic_sample_data():
    print('2017学年度第一学期期末总评总数据量为', data_sample.shape)
    data_statis = data_sample.groupby(['mes_sub_name']).count().reset_index()
    # print(data_statis)
    for i in range(data_statis.shape[0]):
        print('学科', data_statis['mes_sub_name'].iloc[i], '的数据量为', data_statis['mes_TestID'].iloc[i])
    students_groupby = data_sample.groupby(['mes_StudentID']).count().reset_index().sort_values(by='mes_TestID', axis=0, ascending=False)
    print(students_groupby.shape)
    print(students_groupby)

# statistic_sample_data()
# 2017学年度第一学期期末总评总数据量为 13161
# 考试的科目一共为10科，每一科目数据量分布较为一致
# 学科 化学 的数据量为 1365
# 学科 历史 的数据量为 1365
# 学科 地理 的数据量为 1365
# 学科 技术 的数据量为 876
# 学科 政治 的数据量为 1365
# 学科 数学 的数据量为 1365
# 学科 物理 的数据量为 1365
# 学科 生物 的数据量为 1365
# 学科 英语 的数据量为 1365
# 学科 语文 的数据量为 1365
# 如果以学生的ID进行groupby，则可以得到最多的一个学生的学科数为20（只有两个），绝大多数情况下都是9～10
# 那么就证明每个学生的数据覆盖还是挺齐全

##############################################################################
#Step4：确定数据想要展示的层次
# 该部分主要展示学校层次的学科的成绩分布情况，其中每一个科目大概包含2731条数据
# 学科和学科之间的比较没有意义
# 1.学科内的班级之间的比较
# 2.学科内所有的数据的分布情况，应该是真实的成绩分布而不是排名。同时里面也要展示平均成绩以及该学科的及格线
# 可以用来评估这一次考试的整体难度情况
# 让处于达标线以下的同学数量与考试的难度形成映射，有助于学校对试题难度把控提供理论依据

##############################################################################
#Step5：获得成绩的分布情况，按照班级对成绩的文件进行分析
#根据成绩数据集的学生ID数据与学生信息的数据集的学生ID进行比对，获得他们的班级号

def merge_student_id():
    data_merge_byStdID = pd.merge(data_sample, data_student_info, left_on='mes_StudentID', right_on='bf_StudentID', how='left')
    print(data_merge_byStdID)
    data = data_merge_byStdId.drop(['bf_Name', 'mes_TestID', 'exam_number', 'bf_sex', 'bf_nation', 'bf_BornDate', 'bf_NativePlace', 'Bf_ResidenceType', 'bf_policy', 'cla_term', 'bf_zhusu', 'bf_leaveSchool', 'bf_qinshihao'], axis=1)
    data.to_csv('../../education_data/CH/5.chengji_2_claID.csv', encoding='utf_8_sig')

# merge_student_id()

# 获取学科名
def acquire_sub_name():
    sub_name = []
    data_subname = data_sample.groupby('mes_sub_name').count().reset_index()
    for i in range(data_subname.shape[0]):
        sub_name.append(data_subname['mes_sub_name'].iloc[i])
    return sub_name
# 学科为['化学', '历史', '地理', '技术', '政治', '数学', '物理', '生物', '英语', '语文']
# 但是为了展示符合使用者的认知，将学科顺序改为
# ['语文', '数学', '英语', '物理', '化学', '政治', '历史', '生物', '地理', '技术']

def Statistic_sub_byCla(sub):
    cla_id = []
    data_sub = data_merge_byStdId.drop(data_merge_byStdId[data_merge_byStdId['mes_sub_name'] != sub].index).reset_index()
    data_groupby_claID = data_sub.groupby('cla_id').count().reset_index()
    for i in range(data_groupby_claID.shape[0]):
        cla_id.append(data_groupby_claID['cla_id'].iloc[i])
    # 删除缺失值
    data_sub = data_sub.dropna(subset=['mes_T_Score'])
    data_sub = data_sub.dropna(subset=['cla_id'])
    return data_sub


# 计算各个学科的平均成绩
def caculate_sub_average():
    sub_name = ['语文', '数学', '英语', '物理', '化学', '政治', '历史', '生物', '地理', '技术']
    for i in range(len(sub_name)):
        data_sub = Statistic_sub_byCla(sub_name[i])
        average_score = round((data_sub['mes_T_Score'].sum()) / data_sub.shape[0], 2)
        print(average_score)

# caculate_sub_average()
# 因为T-Score的计算方法，则根据T-Score计算方法得到的平均分都是80分


# 删除掉没有10个科目的学生数据
# 删除掉没有10个科目的班级数据
def delete_error_data():
    # 统计班级的情况，取交集
    sub_name = ['语文', '数学', '英语', '物理', '化学', '政治', '历史', '生物', '地理', '技术']
    # 统计十个科目的成绩在班级的分布情况
    for i in range(len(sub_name)):
        xAxis_data = []
        data_sub = Statistic_sub_byCla(sub_name[i])
        data_sub_groupBy = data_sub.groupby('cla_id').count().reset_index()
        for j in range(data_sub_groupBy.shape[0]):
            xAxis_data.append(str(data_sub_groupBy['cla_id'].iloc[j]))
            # xAxis_data.append(str(data_sub_groupBy['cla_Name'].iloc[j]))
        # print('各个学科在班级的分布情况')
        # print(xAxis_data)
    # 剔除掉班级id为947的数据
    data_dropNaN = data_merge_byStdId.dropna(subset=['cla_id'])
    data_dropNaN = data_dropNaN.drop(data_dropNaN[data_dropNaN['cla_id'] == 947].index)
    # 剔除掉没有10个科目的学生数据
    # data_complete_id表示十个科目都是全的数据的学生
    data_complete_id = data_dropNaN
    data_complete_id['label'] = 1
    data_complete_id = data_complete_id.groupby('mes_StudentID').count().reset_index()
    data_complete_id = data_complete_id.drop(data_complete_id[data_complete_id['label'] != 10].index)
    # print(data_complete_id)
    score_total = []

    scatter_xAxis = ['901.0', '902.0', '903.0', '904.0', '905.0', '906.0', '907.0', '908.0', '909.0', '910.0', '911.0',
                     '912.0', '916.0', '917.0', '918.0', '919.0', '920.0', '921.0', '922.0', '923.0', '924.0', '925.0',
                     '943.0', '945.0']

    xAxis_name = ['高一(10)', '高二(01)', '高二(02)', '高二(03)', '高二(04)', '高二(05)', '高二(06)', '高二(07)', '高二(08)'
        , '高二(09)', '高二(10)', '高二(11)', '高二(12)', '高三(01)', '高三(02)', '高三(03)', '高三(04)', '高三(05)', '高三(06)'
        , '高三(07)', '高三(08)', '高三(09)', '高三(10)', '高二未分班']

    for i in range(data_dropNaN.shape[0]):
        for j in range(len(scatter_xAxis)):
            if data_dropNaN['cla_id'].iloc[i] == scatter_xAxis[j]:
                data_dropNaN['cla_Name'].iloc[i] = xAxis_name[j]

    for i in range(data_complete_id.shape[0]):
        data_dropNaN_groupByID = data_dropNaN.drop(data_dropNaN[data_dropNaN['mes_StudentID'] != data_complete_id['mes_StudentID'].iloc[i]].index)
        data_dropNaN_groupByID['mes_T_Score'] = data_dropNaN_groupByID['mes_T_Score'].fillna(80)
        score_piece = []
        for j in range(len(sub_name)):
            if data_dropNaN_groupByID['mes_sub_name'].iloc[j] == sub_name[j]:
                score_piece.append(round(data_dropNaN_groupByID['mes_T_Score'].iloc[j], 2))
            else:
                score_piece.append(80)
        score_piece.append(str(data_dropNaN_groupByID['mes_StudentID'].iloc[0]))
        score_piece.append(str(data_dropNaN_groupByID['cla_Name'].iloc[0]))
        score_total.append(score_piece)
    print(score_total)

    json_data = {'xAxis': xAxis_name, 'score_total': score_total}
    with open('../1.School-Level-data/4.Score_cla_total.json', 'w') as file:
        json.dump(json_data, file)
    print(json_data)
    print('完成文件加载')


# 经过统计，前九科目只有947班级存在不齐全的情况
# 对于技术科目的成绩，只有['916.0', '917.0', '918.0', '919.0', '920.0', '921.0', '922.0', '923.0', '924.0', '925.0', '947.0']
# 班级有成绩
#
# delete_error_data()
# 该方法创造的数据集存在科目的缺失

# 再次尝试
def create_score_sub():
    # 统计班级的情况，取交集
    sub_name = ['语文', '数学', '英语', '物理', '化学', '政治', '历史', '生物', '地理', '技术']
    # 统计十个科目的成绩在班级的分布情况
    for i in range(len(sub_name)):
        xAxis_data = []
        data_sub = Statistic_sub_byCla(sub_name[i])
        data_sub_groupBy = data_sub.groupby('cla_id').count().reset_index()
        for j in range(data_sub_groupBy.shape[0]):
            xAxis_data.append(str(data_sub_groupBy['cla_id'].iloc[j]))
            # xAxis_data.append(str(data_sub_groupBy['cla_Name'].iloc[j]))
        # print('各个学科在班级的分布情况')
        # print(xAxis_data)
    # 剔除掉班级id为947的数据
    print(data_merge_byStdId.shape)
    data_dropNaN = data_merge_byStdId.dropna(subset=['cla_id'])
    print(data_dropNaN.shape[0])

    # data_dropNaN = data_dropNaN.drop(data_dropNaN[data_dropNaN['cla_id'] == 947].index)
    # # 剔除掉没有10个科目的学生数据
    # # data_complete_id表示十个科目都是全的数据的学生
    # data_complete_id = data_dropNaN
    # data_complete_id['label'] = 1
    # data_complete_id = data_complete_id.groupby('mes_StudentID').count().reset_index()
    # # data_complete_id = data_complete_id.drop(data_complete_id[data_complete_id['label'] != 10].index)
    # print(data_complete_id)

# create_score_sub()