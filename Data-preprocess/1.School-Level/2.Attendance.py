#-*- coding:utf-8 -*-

'''
# Author: chenhao
# Date: March. 12
# Description: Data-process for Education visualization competition
'''

##############################################################################
#Part2：统计学校范围内学生的考勤情况
##############################################################################

import pandas as pd

# 导入数据集
data_origin = pd.read_csv('../../education_data/3_kaoqin.csv')

##############################################################################
# Step1: 实现数据集学期数据的补齐
# 从Excel中观察，不可以直接进行补齐

# 统计学期一栏数据缺失的数量
num_term_null = len(data_origin['qj_term'][pd.isnull(data_origin['qj_term'])])
print("学期栏缺失数量为：", num_term_null)
# 缺失的数量为947

# 首先获得DataDateTime数据
DataDateTime = data_origin['DataDateTime']
print(DataDateTime)

'''
# 将统计学期一栏缺失数据进行补齐
# 通过观察可以得到，缺失的数据全部都是2014年3月份的数据，所以直接补齐2013-2014-2
data_origin['qj_term'][pd.isnull(data_origin['qj_term'])] = "2013-2014-1"

print(len(data_origin['qj_term'][pd.isnull(data_origin['qj_term'])]))

##############################################################################
# Step2: 以各个学期为单位，对数据进行划分
# 学期跨度为2013-2014-1，到2018-2019-1

term = ["2013-2014-1", "2013-2014-2", "2014-2015-1", "2014-2015-2", "2015-2016-1", "2015-2016-2", "2016-2017-1",
        "2016-2017-2", "2017-2018-1", "2017-2018-2", "2018-2019-1", ]
'''

