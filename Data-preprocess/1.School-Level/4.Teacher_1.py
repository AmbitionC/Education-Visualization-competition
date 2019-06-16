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
import numpy as np
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

# data_teacher_class()

##############################################################################
# Step7: 制作教师与班级的网络拓扑关系图

def create_net_teachers():
    sub_name = ['语文', '数学', '英语', '物理', '化学', '政治', '历史', '生物', '地理', '技术', '美术',
                '体育', '音乐']
    color = ['#ff9797', '#b3d9d9', '#adadad', '#d48265', '#91c7ae', '#749f83', '#ca8622', '#bda29a', '#6e7074',
             '#546570', '#c4ccd3', '#ff9797','#b3d9d9',]
    total_teacher = pd.DataFrame()
    for i in range(len(sub_name)):
        data_origin['sum'] = 1
        data_teacher = data_origin[data_origin['sub_Name'].str.contains(sub_name[i])]
        data_teacher = data_teacher.groupby(['bas_id']).count().reset_index()
        # print(data_teacher)
        for k in range(data_teacher.shape[0]):
            if data_teacher['sum'].iloc[k] >= 50:
                data_teacher['sum'].iloc[k] = 50
        data_teacher['size'] = data_teacher['sum']
        data_teacher['color'] = color[i]
        data_teacher['label'] = data_teacher['bas_id']
        data_teacher['id'] = data_teacher['bas_id']
        data_teacher = data_teacher.drop(['bas_id', 'cla_id', 'term', 'cla_Name', 'sub_id', 'sub_Name', 'bas_Name', 'sum','gra_Name'], axis=1)
        total_teacher = total_teacher.append(data_teacher)
    total_teacher['x'] = 0
    total_teacher['y'] = 0
    for j in range(total_teacher.shape[0]):
        total_teacher['x'].iloc[j] = 0
        total_teacher['y'].iloc[j] = 0
    # print(total_teacher)
    return total_teacher

def create_net_classes():
    data_class = data_origin.groupby(['cla_id']).count().reset_index()
    data_class['id'] = data_class['cla_id']
    data_class['label'] = data_class['cla_id']
    data_class['size'] = 2
    data_class['color'] = '#ADADAD'
    data_class = data_class.drop(['term', 'cla_id', 'cla_Name', 'gra_Name', 'sub_id', 'sub_Name', 'bas_id', 'bas_Name', 'sum'], axis=1)
    data_class['x'] = 0
    data_class['y'] = 0
    data_class.rename(columns={0: 'id'}, inplace=True)
    for i in range(data_class.shape[0]):
        data_class['x'].iloc[i] = 0
        data_class['y'].iloc[i] = 0
    # print(data_class)
    return data_class

def create_net_conneting():
    total_teacher = create_net_teachers()
    array_cache_total = []
    for i in range(total_teacher.shape[0]):
        teacher_to_class = pd.DataFrame(columns=['sourceID', 'targetID'])
        for j in range(data_origin.shape[0]):
            if total_teacher['id'].iloc[i] == data_origin['bas_id'].iloc[j]:
                array_cache = [total_teacher['id'].iloc[i], data_origin['cla_id'].iloc[j]]
                array_cache_total.append(array_cache)
    print(array_cache_total)
    teacher_to_class_all = pd.DataFrame(array_cache_total)
    teacher_to_class_all.rename(columns={0: 'sourceID', 1: 'targetID'}, inplace=True)
    print(teacher_to_class_all)
    return teacher_to_class_all

def transfer_to_json():
    data_trans_all = []
    data_trans_all_edges = []
    data_trans_1 = create_net_teachers()
    data_trans_2 = create_net_classes()
    data_trans = pd.concat([data_trans_1, data_trans_2], axis=0, ignore_index=True)
    data_trans_3 = create_net_conneting()
    for i in range(data_trans.shape[0]):
        data_trans_piece = {"color": data_trans['color'].iloc[i], "label": str(data_trans['label'].iloc[i]),
                            "attributes": {}, "y": int(data_trans['y'].iloc[i]), "x": int(data_trans['x'].iloc[i]),
                            "id": str(data_trans['id'].iloc[i]), "size": int(data_trans['size'].iloc[i])}
        data_trans_all.append(data_trans_piece)
    print(data_trans_all)
    for j in range(data_trans_3.shape[0]):
        data_trans_piece_edges = {"sourceID": str(data_trans_3['sourceID'].iloc[j]), "attributes": {},
                                  "targetID": str(data_trans_3['targetID'].iloc[j]), "size": 1}
        data_trans_all_edges.append(data_trans_piece_edges)
    json_data = {"nodes": data_trans_all, "edges": data_trans_all_edges}
    with open('../1.School-Level-data/Teacher_3.json', "w") as file:
        json.dump(json_data, file)
    print("完成文件加载")

# transfer_to_json()

##############################################################################
# Step8: 制作教师与班级的树状图

def create_tree_teacher():
    sub_name = ['语文', '数学', '英语', '物理', '化学', '政治', '历史', '生物', '地理', '技术', '美术',
                '体育', '音乐']
    array_allInfo = []
    for i in range(len(sub_name)):
        # data_show = pd.DataFrame(columns=['name', 'value'])
        data_teacher = data_origin[data_origin['sub_Name'].str.contains(sub_name[i])]
        # 以学科为单位，以教师ID对教师进行groupby
        data_groupby_teacherID = data_teacher.groupby(['bas_id']).count().reset_index()
        teacherID_array = []
        for j in range(data_groupby_teacherID.shape[0]):
            teacherID_array.append(data_groupby_teacherID['bas_id'].iloc[j])
        children_array = []
        for j in range(len(teacherID_array)):
            for k in range(data_teacher.shape[0]):
                if teacherID_array[j] == data_teacher['bas_id'].iloc[k]:
                    teacher_name = data_teacher['bas_Name'].iloc[k]
                    # 插入\n
                    teacher_name_new = teacher_name[0] + '\n' + teacher_name[1] + '\n' + teacher_name[2]
                    teacher_object = {"name": teacher_name_new, "value": 1}
                    children_array.append(teacher_object)
                    break
        sub_teacher_object = {"name": sub_name[i],
                              "children": children_array}
        print(sub_teacher_object)
        array_allInfo.append(sub_teacher_object)
        school_all_object = {"name": "效实中学", "children": array_allInfo}
        with open('../1.School-Level-data/Teacher_4.json', "w") as file:
            json.dump(school_all_object, file)
        print("完成文件加载！")

# create_tree_teacher()

def create_sankey_data():
    # 产生两排名字
    teacher_class_array = []
    data_groupby_teacherID = data_origin.groupby('bas_id').count().reset_index()
    for i in range(data_groupby_teacherID.shape[0]):
        for j in range(data_origin.shape[0]):
            if data_groupby_teacherID['bas_id'].iloc[i] == data_origin['bas_id'].iloc[j]:
                teacherName_piece = {"name": (str(data_origin['bas_id'].iloc[j]) + data_origin['bas_Name'].iloc[j])}
                teacher_class_array.append(teacherName_piece)
                break
    data_groupby_className = data_origin.groupby('cla_Name').count().reset_index()
    for i in range(data_groupby_className.shape[0]):
        className_piece = {"name": data_groupby_className['cla_Name'].iloc[i]}
        teacher_class_array.append(className_piece)
    print(teacher_class_array)
    links_all = []
    for i in range(data_groupby_teacherID.shape[0]):
        teacher_class_data = data_origin.drop(data_origin[data_origin['bas_id'] != data_groupby_teacherID['bas_id'].iloc[i]].index)
        if teacher_class_data.shape[0] > 0:
            for j in range(teacher_class_data.shape[0]):
                link_single = {"source": (str(teacher_class_data['bas_id'].iloc[0]) + teacher_class_data['bas_Name'].iloc[0]),
                                "target": teacher_class_data['cla_Name'].iloc[j],
                                "value": 1}
                links_all.append(link_single)
    print(links_all)
    with open('../1.School-Level-data/Teacher_5.json', "w") as file:
        json.dump(teacher_class_array, file)
    print("完成文件加载！")
    with open('../1.School-Level-data/Teacher_6.json', "w") as file:
        json.dump(links_all, file)
    print("完成文件加载！")

# create_sankey_data()

def create_sankey_data_new():
    print(data_origin.shape[0])
    data_origin_new = data_origin.drop(data_origin[data_origin['term'] != '2014-2015-1'].index)
    print(data_origin_new.shape[0])
    teacher_class_array = []
    data_groupby_teacherID = data_origin_new.groupby('bas_id').count().reset_index()
    for i in range(data_groupby_teacherID.shape[0]):
        for j in range(data_origin_new.shape[0]):
            if data_groupby_teacherID['bas_id'].iloc[i] == data_origin_new['bas_id'].iloc[j]:
                teacherName_piece = {"name": (str(data_origin_new['bas_id'].iloc[j]) + data_origin_new['bas_Name'].iloc[j])}
                teacher_class_array.append(teacherName_piece)
                break
    data_groupby_className = data_origin_new.groupby('cla_Name').count().reset_index()
    for i in range(data_groupby_className.shape[0]):
        className_piece = {"name": data_groupby_className['cla_Name'].iloc[i]}
        teacher_class_array.append(className_piece)
    print(teacher_class_array)
    links_all = []
    for i in range(data_groupby_teacherID.shape[0]):
        teacher_class_data = data_origin_new.drop(data_origin_new[data_origin_new['bas_id'] != data_groupby_teacherID['bas_id'].iloc[i]].index)
        if teacher_class_data.shape[0] > 0:
            for j in range(teacher_class_data.shape[0]):
                link_single = {"source": (str(teacher_class_data['bas_id'].iloc[0]) + teacher_class_data['bas_Name'].iloc[0]),
                                "target": teacher_class_data['cla_Name'].iloc[j],
                                "value": 1}
                links_all.append(link_single)
    print(links_all)
    with open('../1.School-Level-data/Teacher_5.json', "w") as file:
        json.dump(teacher_class_array, file)
    print("完成文件加载！")
    with open('../1.School-Level-data/Teacher_6.json', "w") as file:
        json.dump(links_all, file)
    print("完成文件加载！")

# create_sankey_data_new()

#
# def observe_sankey_data():
#     data_origin['count'] = 1
#     data_groupby = data_origin.groupby(['term']).count().reset_index()
#     print(data_groupby)
#
# # observe_sankey_data()

# 产生根据学科划分的桑基图的数据
def create_sankey_data_divided():
    data_origin_new = data_origin.drop(data_origin[data_origin['term'] != '2014-2015-1'].index)
    print(data_origin_new.shape[0])
    sub_name = ['语文', '数学', '英语', '物理', '化学', '政治', '历史', '生物', '地理', '技术', '美术',
                '体育', '音乐']
    for i in range(len(sub_name)):
        print("正在统计的学科数据：", sub_name[i])
        data_divided = data_origin_new[data_origin_new['sub_Name'].str.contains(sub_name[i])]
        sub_teacher_class_array = []
        data_groupby_teacherID = data_divided.groupby('bas_id').count().reset_index()
        for j in range(data_groupby_teacherID.shape[0]):
            for k in range(data_divided.shape[0]):
                if data_groupby_teacherID['bas_id'].iloc[j] == data_divided['bas_id'].iloc[k]:
                    teacherName_piece = {'name': (str(data_divided['bas_id'].iloc[k]) + data_divided['bas_Name'].iloc[k])}
                    sub_teacher_class_array.append(teacherName_piece)
                    break
        data_groupby_className = data_divided.groupby('cla_Name').count().reset_index()
        for j in range(data_groupby_className.shape[0]):
            className_piece = {"name": data_groupby_className['cla_Name'].iloc[j]}
            sub_teacher_class_array.append(className_piece)
        print(sub_teacher_class_array)
        links_all = []
        for j in range(data_groupby_teacherID.shape[0]):
            teacher_class_data = data_divided.drop(data_divided[data_divided['bas_id'] != data_groupby_teacherID['bas_id'].iloc[j]].index)
            if teacher_class_data.shape[0] > 0:
                for k in range(teacher_class_data.shape[0]):
                    link_single = {"source": (str(teacher_class_data['bas_id'].iloc[0]) + teacher_class_data['bas_Name'].iloc[0]),
                                    "target": teacher_class_data['cla_Name'].iloc[k],
                                    "value": 1}
                    links_all.append(link_single)
        file_path_teacher = '../1.School-Level-data/Teacher_class_' + str(i) + '.json'
        file_path_link = '../1.School-Level-data/Teacher_link_' + str(i) + '.json'
        with open(file_path_teacher, "w") as file:
            json.dump(sub_teacher_class_array, file)
        print("完成文件加载！")
        with open(file_path_link, "w") as file:
            json.dump(links_all, file)
        print("完成文件加载！")

create_sankey_data_divided()