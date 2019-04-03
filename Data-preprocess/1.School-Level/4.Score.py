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

data_origin = pd.read_csv('../../education_data/5_chengji.csv')

data_origin = data_origin.groupby(['exam_numname']).count().reset_index()

print(data_origin.shape[0])
