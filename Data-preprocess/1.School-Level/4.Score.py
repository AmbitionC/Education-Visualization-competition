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

# #显示所有列
# pd.set_option('display.max_columns', None)
# #显示所有行
# pd.set_option('display.max_rows', None)
# #设置value的显示长度为100，默认为50
# pd.set_option('max_colwidth', 100)

# 读取原始数据集合
data_origin = pd.read_csv('../../education_data/5_chengji.csv')

data_sample = pd.read_csv('../../education_data/CH/5.chengji_1.csv')


##############################################################################
#Step1: 找到考试数据最多的那一次考试

def find_datamax_exam():
    data_origin['sum'] = 1
    data_max_exam = data_origin.groupby(['exam_numname']).count().reset_index().sort_values(by='sum', axis=0, ascending=False)
    print(data_max_exam)

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
    data_2017_finalExam.to_csv('../../education_data/CH/5.chengji_1.csv')


find_2017_finalExam()

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

statistic_sample_data()
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


