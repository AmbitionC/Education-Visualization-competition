#-*- coding:utf-8 -*-

'''
# Author: chenhao
# Date: March. 22
# Description: Data-process for Education visualization competition
'''

##############################################################################
#Part3：统计学校的老师的数据
##############################################################################

import pandas as pd
import json

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

data_origin = pd.read_csv("../../education_data/1_teacher.csv")

##############################################################################
# Step1: 统计数据的整体缺失情况

def statistic_null_num():
    num_term_null = len(data_origin['term'][pd.isnull(data_origin['term'])])
    num_classid_null = len(data_origin['cla_id'][pd.isnull(data_origin['cla_id'])])
    num_classname_null = len(data_origin['cla_Name'][pd.isnull(data_origin['cla_Name'])])
    num_graname_null = len(data_origin['gra_Name'][pd.isnull(data_origin['gra_Name'])])
    num_subid_null = len(data_origin['sub_id'][pd.isnull(data_origin['sub_id'])])
    num_subname_null = len(data_origin['sub_Name'][pd.isnull(data_origin['sub_Name'])])
    num_basid_null = len(data_origin['bas_id'][pd.isnull(data_origin['bas_id'])])
    num_basname_null = len(data_origin['bas_Name'][pd.isnull(data_origin['bas_Name'])])

    print(num_term_null, num_classid_null, num_classname_null, num_graname_null, num_subid_null, num_subname_null, num_basid_null, num_basname_null)

# statistic_null_num()
# 该表的缺失值为0

##############################################################################
# Step2: 统计教师在各个年级的数量

def statistic_gra_teachers():
    gra_name = ['高一', '高二', '高三']
    for i in range(len(gra_name)):
        data_gra = data_origin.drop(data_origin[data_origin['gra_Name'] != gra_name[i]].index)
        data_gra['label'] = 1
        data_gra = data_gra.groupby('bas_id').sum()
        sum = 0
        sum = data_gra['label'].shape[0]
        print(gra_name[i], '的教师人数为', sum)

# statistic_gra_teachers()
# 高一 的教师人数为 171
# 高二 的教师人数为 134
# 高三 的教师人数为 119

##############################################################################
# Step3: 统计学校在各个学科的师资分配情况

def statistic_sub_teachers():
    sub_name = ['语文', '数学', '英语', '英语2', '英语选修9', '物理', '化学', '政治', '历史', '生物', '地理', '技术', '美术',
                '体育', '通用技术', '信息技术', '音乐', '1B模块总分']
    for i in range(len(sub_name)):
        data_sub = data_origin.drop(data_origin[data_origin['sub_Name'] != sub_name[i]].index)
        data_sub['label'] = 1
        data_sub = data_sub.groupby('bas_id').sum()
        sum = 0
        sum = data_sub['label'].shape[0]
        print('学科', sub_name[i], '的教师数为', sum)

# statistic_sub_teachers()
# 学科 语文 的教师数为 27
# 学科 数学 的教师数为 31
# 学科 英语 的教师数为 59
# 学科 物理 的教师数为 20
# 学科 化学 的教师数为 20
# 学科 政治 的教师数为 10
# 学科 历史 的教师数为 9
# 学科 生物 的教师数为 12
# 学科 地理 的教师数为 11
# 学科 技术 的教师数为 9
# 学科 美术 的教师数为 3
# 学科 体育 的教师数为 1
# 学科 音乐 的教师数为 2
# 学科 1B模块总分 的教师数为 23
# 全校在职教师 189

##############################################################################
# Step3: 统计每个老师所带班级的数量

def statistic_class_teachers():
    data_origin['label'] = 1
    data_class = data_origin.groupby('bas_id').sum()
    data_class = data_class.drop(['cla_id', 'sub_id'], axis=1)
    print('全校在职教师人数', data_class.shape[0])
    # 可以统计全校各个老师的授课情况
    print(data_class['label'].describe())
    print(data_class)

# statistic_class_teachers()
# 全校在职教师人数 189
#             lable
# count  189.000000
# mean    16.338624
# std     26.534835
# min      1.000000
# 25%      4.000000
# 50%     12.000000
# 75%     17.000000
# max    296.000000



##############################################################################
# Step4: 统计学校的班级数

def statistic_class_num():
    data_origin['label'] = 1
    data_classNum = data_origin.groupby('cla_id').sum()
    print('全校班级数量为', data_classNum.shape[0])

# statistic_class_num()
# 全校班级数量为 193

##############################################################################
# Step5: 通过划分高一到高三的，统计不同的学科人数

def statistic_gra_sub_teachers():
    gra_name = ['高一', '高二', '高三']
    sub_name = ['语文', '数学', '英语', '英语2', '英语选修9', '物理', '化学', '政治', '历史', '生物', '地理', '技术', '美术',
                '体育', '通用技术', '信息技术', '音乐', '1B模块总分']
    for i in range(len(gra_name)):
        data_gra = data_origin.drop(data_origin[data_origin['gra_Name'] != gra_name[i]].index)
        data_gra['label'] = 1
        for j in range(len(sub_name)):
            data_sub = data_gra.drop(data_gra[data_gra['sub_Name'] != sub_name[j]].index)
            data_sub = data_sub.groupby('bas_id').sum()
            sum = 0
            sum = data_sub['label'].shape[0]
            print(gra_name[i], '的学科', sub_name[j], '的教师数为', sum)

# statistic_gra_sub_teachers()
# 高一 的学科 语文 的教师数为 24
# 高一 的学科 数学 的教师数为 27
# 高一 的学科 英语 的教师数为 47
# 高一 的学科 物理 的教师数为 19
# 高一 的学科 化学 的教师数为 18
# 高一 的学科 政治 的教师数为 10
# 高一 的学科 历史 的教师数为 9
# 高一 的学科 生物 的教师数为 12
# 高一 的学科 地理 的教师数为 11
# 高一 的学科 技术 的教师数为 1
# 高一 的学科 美术 的教师数为 3
# 高一 的学科 体育 的教师数为 1
# 高一 的学科 音乐 的教师数为 2

# 高二 的学科 语文 的教师数为 22
# 高二 的学科 数学 的教师数为 24
# 高二 的学科 英语 的教师数为 40
# 高二 的学科 物理 的教师数为 11
# 高二 的学科 化学 的教师数为 8
# 高二 的学科 政治 的教师数为 8
# 高二 的学科 历史 的教师数为 4
# 高二 的学科 生物 的教师数为 11
# 高二 的学科 地理 的教师数为 4
# 高二 的学科 技术 的教师数为 9
# 高二 的学科 美术 的教师数为 3
# 高二 的学科 体育 的教师数为 1
# 高二 的学科 音乐 的教师数为 2

# 高三 的学科 语文 的教师数为 21
# 高三 的学科 数学 的教师数为 20
# 高三 的学科 英语 的教师数为 32
# 高三 的学科 物理 的教师数为 9
# 高三 的学科 化学 的教师数为 10
# 高三 的学科 政治 的教师数为 4
# 高三 的学科 历史 的教师数为 4
# 高三 的学科 生物 的教师数为 8
# 高三 的学科 地理 的教师数为 4
# 高三 的学科 技术 的教师数为 6
# 高三 的学科 美术 的教师数为 2
# 高三 的学科 体育 的教师数为 1
# 高三 的学科 音乐 的教师数为 2

##############################################################################
# Step6: 制作每个教师带班的数量统计

# 根据各个学科进行统计
def data_teacher_class():
    sub_name = ['语文', '数学', '英语', '物理', '化学', '政治', '历史', '生物', '地理', '技术', '美术',
                '体育', '音乐']
    teacher_label_all = []
    teacher_name_all = []
    name_label_all = []
    for i in range(len(sub_name)):
        teacher_label_piece = []
        teacher_name_piece = []
        name_label_piece = []
        data_origin['label'] = 1
        data_teacher = data_origin[data_origin['sub_Name'].str.contains(sub_name[i])]
        data_teacher = data_teacher.groupby(['bas_id']).count().reset_index()
        data_teacher['bas_name'] = 0
        # print(data_teacher)
        for j in range(data_teacher.shape[0]):
            for k in range(data_origin.shape[0]):
                if data_teacher['bas_id'].iloc[j] == data_origin['bas_id'].iloc[k]:
                    data_teacher['bas_name'].iloc[j] = data_origin['bas_Name'].iloc[k]
                    break
        # print(data_teacher)
        for m in range(data_teacher.shape[0]):
            teacher_label_piece.append(int(data_teacher['label'].iloc[m]))
            teacher_name_piece.append(data_teacher['bas_name'].iloc[m])
            name_label = [data_teacher['bas_name'].iloc[m], int(data_teacher['label'].iloc[m])]
            name_label_piece.append(name_label)
        name_label_all.append(name_label_piece)
        teacher_label_all.append(teacher_label_piece)
        teacher_name_all.append(teacher_name_piece)

    print(name_label_all)

    # print(len(teacher_label_all))
    print(teacher_name_all)
    json_data = {'row': name_label_all, 'name': teacher_name_all}
    # json_data = {'Chinese': name_label_all[0], 'Math': name_label_all[1], 'English': name_label_all[2],
    #             'Physics': name_label_all[3], 'Chemical': name_label_all[4], 'Political': name_label_all[5],
    #              'History': name_label_all[6], 'Biology': name_label_all[7], 'Geography': name_label_all[8],
    #              'Technology': name_label_all[9], 'Art': name_label_all[10], 'Gym': name_label_all[11],
    #              'Music': name_label_all[12]}
    print(json_data)
    with open('../1.School-Level-data/2.Teacher_1.json', "w") as file:
        json.dump(json_data, file)
    print("完成文件加载")

data_teacher_class()