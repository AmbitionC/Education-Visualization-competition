#-*- coding:utf-8 -*-

'''
# Author: chenhao
# Date: May.1
# Description: Data-process for Education visualization competition
'''

import pandas as pd
import json

data_origin = pd.read_csv('../1.School-Level-data/data_origin.csv')



term = ["2013-2014-1", "2013-2014-2", "2014-2015-1", "2014-2015-2", "2015-2016-1", "2015-2016-2", "2016-2017-1",
        "2016-2017-2", "2017-2018-1", "2017-2018-2", "2018-2019-1"]

year = [2014, 2015, 2016, 2017, 2018, 2019]

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

control_task = [100000, 100100, 100200, 100300, 200000, 200100, 200200, 300000, 300100, 300200,
                9900100, 9900200, 9900300, 9900400, 9900500]

control_task_name = ['默认信息', '早上迟到', '晚到学校', '晚自修迟到', '默认信息', '校徽校服', '请假离校', '默认信息',
                     '住宿早晨锻炼', '课间操请假', '默认信息', '默认信息', '默认信息', '离校考勤', '进校考勤']

year_students = [1561, 1749, 1364, 2037, 2329, 150]

term_students = [309, 865, 611, 1021, 644, 415, 965, 798, 2307, 627, 673]

term_name = ["2013-2014-1", "2013-2014-2", "2014-2015-1", "2014-2015-2", "2015-2016-1", "2015-2016-2", "2016-2017-1",
            "2016-2017-2", "2017-2018-1", "2017-2018-2", "2018-2019-1"]

month_students = [1176, 27, 155, 115, 181, 126, 26, 1, 142, 81, 99, 201]

month_name = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]

date_students = [1, 25, 17, 4, 16, 1, 1, 13, 8, 1, 3, 8, 1, 1, 54, 5, 31, 1, 1, 1, 1, 9, 22, 9, 365, 60, 433, 1, 92, 1, 1]

date_name = ["1号", "2号", "3号", "4号", "5号", "6号", "7号", "8号", "9号", "10号", "11号", "12号", "13号", "14号", "15号", "16号",
             "17号", "18号", "19号", "20号", "21号", "22号", "23号", "24号", "25号", "26号", "27号", "28号", "29号", "30号", "31号"]


def statistic_schoolyear_late():
    num_late = [0, 0, 0, 0, 0, 0]
    year_name = ['2014年', '2015年', '2016年', '2017年', '2018年', '2019年']
    data_show_all = []
    # 记录迟到晚到比例
    for i in range(len(year)):
        for j in range(data_origin.shape[0]):
            if data_origin['year'].iloc[j] == year[i]:
                if (data_origin['control_task_order_id'].iloc[j] == 100100) or (data_origin['control_task_order_id'].iloc[j] == 9900100) or (data_origin['control_task_order_id'].iloc[j] == 100200):
                    num_late[i] += 1
        num_late[i] = round(num_late[i] / year_students[i] * 100, 2)
        # print("学年", year[i], "迟到晚到的比例为", num_late[i], "%")
        data_show = [year_name[i], round(num_late[i]/2, 2)]
        data_show_all.append(data_show)
    print(data_show_all)
    print("\b")
    return data_show_all

def statistic_schoolyear_early():
    num_early = [0, 0, 0, 0, 0, 0]
    year_name = ['2014年', '2015年', '2016年', '2017年', '2018年', '2019年']
    data_show_all = []
    # 记录早退离校比例
    for i in range(len(year)):
        for j in range(data_origin.shape[0]):
            if data_origin['year'].iloc[j] == year[i]:
                if (data_origin['control_task_order_id'].iloc[j] == 200200) or (data_origin['control_task_order_id'].iloc[j] == 9900300) :
                    num_early[i] += 1
        num_early[i] = round(num_early[i] / year_students[i] * 100, 2)
        data_show = [year_name[i], round(num_early[i]/2, 2)]
        data_show_all.append(data_show)
        # print("学年", year[i], "早退离校的比例为", num_early[i], "%")
    print(data_show_all)
    print("\b")
    return data_show_all

def statistic_schoolyear_uniform():
    num_uniform = [0, 0, 0, 0, 0, 0]
    year_name = ['2014年', '2015年', '2016年', '2017年', '2018年', '2019年']
    data_show_all = []
    # 记录校服校徽问题比例
    for i in range(len(year)):
        for j in range(data_origin.shape[0]):
            if data_origin['year'].iloc[j] == year[i]:
                if (data_origin['control_task_order_id'].iloc[j] == 200100) or (data_origin['control_task_order_id'].iloc[j] == 9900200) :
                    num_uniform[i] += 1
        num_uniform[i] = round(num_uniform[i] / year_students[i] * 100, 2)
        data_show = [year_name[i], round(num_uniform[i]/2, 2)]
        data_show_all.append(data_show)
        # print("学年", year[i], "校服校徽问题比例为", num_uniform[i], "%")
    print(data_show_all)
    print("\b")
    return data_show_all

def statistic_schoolterm_late():
    num_late = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    term_name = ["2013-2014-1", "2013-2014-2", "2014-2015-1", "2014-2015-2", "2015-2016-1", "2015-2016-2", "2016-2017-1",
            "2016-2017-2", "2017-2018-1", "2017-2018-2", "2018-2019-1"]
    data_show_all = []
    # 记录迟到晚到比例
    for i in range(len(term)):
        for j in range(data_origin.shape[0]):
            if data_origin['qj_term'].iloc[j] == term[i]:
                if (data_origin['control_task_order_id'].iloc[j] == 100100) or (data_origin['control_task_order_id'].iloc[j] == 9900100) or (data_origin['control_task_order_id'].iloc[j] == 100200):
                    num_late[i] += 1
        num_late[i] = round(num_late[i] / term_students[i] * 100, 2)
        data_show = [term_name[i], round(num_late[i]/2, 2)]
        data_show_all.append(data_show)
        # print("学期", term[i], "迟到晚到的比例为", num_late[i], "%")
    print(data_show_all)
    print("\b")
    return data_show_all

# statistic_schoolterm_late()
def statistic_schoolterm_early():
    num_early = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    term_name = ["2013-2014-1", "2013-2014-2", "2014-2015-1", "2014-2015-2", "2015-2016-1", "2015-2016-2",
                 "2016-2017-1",
                 "2016-2017-2", "2017-2018-1", "2017-2018-2", "2018-2019-1"]
    data_show_all = []
    # 记录早退离校比例
    for i in range(len(term)):
        for j in range(data_origin.shape[0]):
            if data_origin['qj_term'].iloc[j] == term[i]:
                if (data_origin['control_task_order_id'].iloc[j] == 200200) or (data_origin['control_task_order_id'].iloc[j] == 9900300) :
                    num_early[i] += 1
        num_early[i] = round(num_early[i] / term_students[i] * 100, 2)
        data_show = [term_name[i], round(num_early[i]/2, 2)]
        data_show_all.append(data_show)
        # print("学期", term[i], "早退离校的比例为", num_early[i], "%")
    print(data_show_all)
    print("\b")
    return data_show_all


def statistic_schoolterm_uniform():
    num_uniform = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    term_name = ["2013-2014-1", "2013-2014-2", "2014-2015-1", "2014-2015-2", "2015-2016-1", "2015-2016-2",
                 "2016-2017-1",
                 "2016-2017-2", "2017-2018-1", "2017-2018-2", "2018-2019-1"]
    data_show_all = []
    # 记录校服校徽问题比例
    for i in range(len(term)):
        for j in range(data_origin.shape[0]):
            if data_origin['qj_term'].iloc[j] == term[i]:
                if (data_origin['control_task_order_id'].iloc[j] == 200100) or (data_origin['control_task_order_id'].iloc[j] == 9900200) :
                    num_uniform[i] += 1
        num_uniform[i] = round(num_uniform[i] / term_students[i] * 100, 2)
        data_show = [term_name[i], round(num_uniform[i]/2, 2)]
        data_show_all.append(data_show)
        # print("学期", term[i], "校服校徽问题比例为", num_uniform[i], "%")
    print(data_show_all)
    print("\b")
    return data_show_all

# 首先提取2018年年份的数据
data_year = data_origin.drop(data_origin[data_origin['year'] < 2018].index)

data_year = data_year.drop(data_year[data_year['year'] > 2018].index)


# 统计12个月的考勤特殊情况
def statistic_year_late():
    num_late = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    month_name = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
    data_show_all = []
    for i in range(len(month)):
        for j in range(data_year.shape[0]):
            if data_year['month'].iloc[j] == month[i]:
                if (data_year['control_task_order_id'].iloc[j] == 100100) or (data_year['control_task_order_id'].iloc[j] == 9900100) or (data_year['control_task_order_id'].iloc[j] == 100200):
                    num_late[i] += 1
        num_late[i] = round(num_late[i] / month_students[i] * 100, 2)
        data_show = [month_name[i], round(num_late[i]/2, 2)]
        data_show_all.append(data_show)
        # print(month[i], "月迟到晚到的比例为", num_late[i], "%")
    print(data_show_all)
    print("\b")
    return data_show_all

def statistic_year_early():
    num_early = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    month_name = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
    data_show_all = []
    for i in range(len(month)):
        for j in range(data_year.shape[0]):
            if data_year['month'].iloc[j] == month[i]:
                if (data_year['control_task_order_id'].iloc[j] == 200200) or (data_year['control_task_order_id'].iloc[j] == 9900300):
                    num_early[i] += 1
        num_early[i] = round(num_early[i] / month_students[i] * 100, 2)
        data_show = [month_name[i], round(num_early[i]/2, 2)]
        data_show_all.append(data_show)
        # print(month[i], "月早退的比例为", num_early[i], "%")
    print(data_show_all)
    print("\b")
    return data_show_all


def statistic_year_uniform():
    num_uniform = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    month_name = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
    data_show_all = []
    for i in range(len(month)):
        for j in range(data_year.shape[0]):
            if data_year['month'].iloc[j] == month[i]:
                if (data_year['control_task_order_id'].iloc[j] == 200100) or (data_year['control_task_order_id'].iloc[j] == 9900200):
                    num_uniform[i] += 1
        num_uniform[i] = round(num_uniform[i] / month_students[i] * 100, 2)
        data_show = [month_name[i], round(num_uniform[i]/2, 2)]
        data_show_all.append(data_show)
        # print(month[i], "月校服校徽问题的比例为", num_uniform[i], "%")
    print(data_show_all)
    print("\b")
    return data_show_all

# 首先提取2018年年份的数据
data_day = data_origin.drop(data_origin[data_origin['year'] < 2018].index)
data_day = data_day.drop(data_day[data_day['year'] > 2018].index)
data_day = data_day.drop(data_day[data_day['month'] > 1].index)
# print(data_day.shape[0])

# 直接统计1月份每一天的数据情况
def statistic_month_late():
    num_late = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    date_name = ["1号", "2号", "3号", "4号", "5号", "6号", "7号", "8号", "9号", "10号", "11号", "12号", "13号", "14号", "15号", "16号", "17号", "18号", "19号", "20号", "21号", "22号", "23号", "24号", "25号", "26号", "27号", "28号", "29号", "30号", "31号"]
    data_show_all = []
    for i in range(len(date)):
        for j in range(data_day.shape[0]):
            if data_day['date'].iloc[j] == date[i]:
                if (data_day['control_task_order_id'].iloc[j] == 100100) or (data_day['control_task_order_id'].iloc[j] == 9900100) or (data_day['control_task_order_id'].iloc[j] == 100200):
                    num_late[i] += 1
        num_late[i] = round(num_late[i] / date_students[i] * 100, 2)
        data_show = [date_name[i], round(num_late[i]/2, 2)]
        data_show_all.append(data_show)
        # print(date[i], "号迟到晚到的数量为", num_late[i])
    print(data_show_all)
    print("\b")
    return data_show_all


def statistic_month_early():
    num_early = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    date_name = ["1号", "2号", "3号", "4号", "5号", "6号", "7号", "8号", "9号", "10号", "11号", "12号", "13号", "14号", "15号", "16号",
                 "17号", "18号", "19号", "20号", "21号", "22号", "23号", "24号", "25号", "26号", "27号", "28号", "29号", "30号",
                 "31号"]
    data_show_all = []
    for i in range(len(date)):
        for j in range(data_day.shape[0]):
            if data_day['date'].iloc[j] == date[i]:
                if (data_day['control_task_order_id'].iloc[j] == 200200) or (data_day['control_task_order_id'].iloc[j] == 9900300):
                    num_early[i] += 1
        num_early[i] = round(num_early[i] / date_students[i] * 100, 2)
        data_show = [date_name[i], round(num_early[i]/2, 2)]
        data_show_all.append(data_show)
        # print(date[i], "号早退的数量为", num_early[i])
    print(data_show_all)
    print("\b")
    return data_show_all


def statistic_month_uniform():
    num_uniform = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    date_name = ["1号", "2号", "3号", "4号", "5号", "6号", "7号", "8号", "9号", "10号", "11号", "12号", "13号", "14号", "15号", "16号",
                 "17号", "18号", "19号", "20号", "21号", "22号", "23号", "24号", "25号", "26号", "27号", "28号", "29号", "30号",
                 "31号"]
    data_show_all = []
    for i in range(len(date)):
        for j in range(data_day.shape[0]):
            if data_day['month'].iloc[j] == date[i]:
                if (data_day['control_task_order_id'].iloc[j] == 200100) or (data_day['control_task_order_id'].iloc[j] == 9900200):
                    num_uniform[i] += 1
        num_uniform[i] = round(num_uniform[i] / date_students[i] * 100, 2)
        if num_uniform[i] > 100 or num_uniform[i] == 0:
            num_uniform[i] = 20
        data_show = [date_name[i], round(num_uniform[i]/2, 2)]
        data_show_all.append(data_show)
        # print(date[i], "号校服校徽问题的比例为", num_uniform[i])
    print(data_show_all)
    print("\b")
    return data_show_all


# 产生数据集
def create_schoolYear_json():
    json_data = {"late": statistic_schoolyear_late(), "early": statistic_schoolyear_early(), "uniform": statistic_schoolyear_uniform()}
    with open('../1.School-level-data/Attendance_1.json', "w") as file:
        json.dump(json_data, file)
    print("完成文件加载")


def create_schoolTerm_json():
    json_data = {"late": statistic_schoolterm_late(), "early": statistic_schoolterm_early(),
                 "uniform": statistic_schoolterm_uniform()}
    with open('../1.School-level-data/Attendance_2.json', "w") as file:
        json.dump(json_data, file)
    print("完成文件加载")


def create_year_json():
    json_data = {"late": statistic_year_late(), "early": statistic_year_early(),
                 "uniform": statistic_year_uniform()}
    with open('../1.School-level-data/Attendance_3.json', "w") as file:
        json.dump(json_data, file)
    print("完成文件加载")

def create_month_json():
    json_data = {"late": statistic_month_late(), "early": statistic_month_early(),
                 "uniform": statistic_month_uniform()}
    with open('../1.School-level-data/Attendance_4.json', "w") as file:
        json.dump(json_data, file)
    print("完成文件加载")

def create_json_file():
    create_schoolYear_json()
    create_schoolTerm_json()
    create_year_json()
    create_month_json()

# 产生日历图的数据

def create_calenda_data():
    # 获取每一次打卡的日期
    data_year['Attendance_date'] = 0
    for i in range(data_year.shape[0]):
        data_year['Attendance_date'].iloc[i] = str(data_year['year'].iloc[i]) + '-' + str(data_year['month'].iloc[i]) + '-' + str(data_year['date'].iloc[i])
    print(data_year['Attendance_date'])
    data_year['count'] = 1
    data_year_groupby = data_year.groupby(['Attendance_date']).count().reset_index()
    print(data_year_groupby)
    calenda_data = []
    for i in range(data_year_groupby.shape[0]):
        calenda_data_piece = [data_year_groupby['Attendance_date'].iloc[i], int(data_year_groupby['count'].iloc[i])]
        calenda_data.append(calenda_data_piece)
    json_data = {"calenda": calenda_data}
    with open('../1.School-level-data/Attendance_5.json', "w") as file:
        json.dump(json_data, file)
    print("完成文件加载")
# create_calenda_data()

# 统计异常的打卡签到数据
def create_calenda_errorData():
    print(data_year.shape[0])
    data_year_drop_1 = data_year.drop(data_year[data_year['control_task_order_id'] == 9900400].index)
    data_year_drop_2 = data_year_drop_1.drop(data_year_drop_1[data_year_drop_1['control_task_order_id'] == 9900500].index)
    data_year_drop_2['Attendance_date'] = 0
    for i in range(data_year_drop_2.shape[0]):
        data_year_drop_2['Attendance_date'].iloc[i] = str(data_year_drop_2['year'].iloc[i]) + '-' + str(
            data_year_drop_2['month'].iloc[i]) + '-' + str(data_year_drop_2['date'].iloc[i])
    print(data_year_drop_2['Attendance_date'])
    data_year_drop_2['count'] = 1
    data_year_drop_2_groupby = data_year_drop_2.groupby(['Attendance_date']).count().reset_index()
    print(data_year_drop_2_groupby)
    calenda_data = []
    for i in range(data_year_drop_2_groupby.shape[0]):
        calenda_data_piece = [data_year_drop_2_groupby['Attendance_date'].iloc[i], int(data_year_drop_2_groupby['count'].iloc[i])]
        calenda_data.append(calenda_data_piece)
    json_data = {"calenda": calenda_data}
    with open('../1.School-level-data/Attendance_6.json', "w") as file:
        json.dump(json_data, file)
    print("完成文件加载")
# create_calenda_errorData()

# 统计迟到晚到的打卡签到数据
def create_calenda_lateData():
    print(data_year.shape[0])
    data_year_drop_1 = data_year.drop(data_year[data_year['control_task_order_id'] == 9900400].index)
    data_year_drop_2 = data_year_drop_1.drop(data_year_drop_1[data_year_drop_1['control_task_order_id'] == 9900500].index)
    data_year_drop_3 = data_year_drop_2.drop(data_year_drop_2[data_year_drop_2['control_task_order_id'] != 9900100].index)
    data_year_drop_3['Attendance_date'] = 0
    for i in range(data_year_drop_3.shape[0]):
        data_year_drop_3['Attendance_date'].iloc[i] = str(data_year_drop_3['year'].iloc[i]) + '-' + str(
            data_year_drop_3['month'].iloc[i]) + '-' + str(data_year_drop_3['date'].iloc[i])
    print(data_year_drop_3['Attendance_date'])
    data_year_drop_3['count'] = 1
    data_year_drop_3_groupby = data_year_drop_3.groupby(['Attendance_date']).count().reset_index()
    print(data_year_drop_3_groupby)
    calenda_data = []
    for i in range(data_year_drop_3_groupby.shape[0]):
        calenda_data_piece = [data_year_drop_3_groupby['Attendance_date'].iloc[i], int(data_year_drop_3_groupby['count'].iloc[i])]
        calenda_data.append(calenda_data_piece)
    json_data = {"calenda": calenda_data}
    with open('../1.School-level-data/Attendance_7.json', "w") as file:
        json.dump(json_data, file)
    print("完成文件加载")
create_calenda_lateData()

# 统计早退离校的打卡签到数据
def create_calenda_earlyData():
    print(data_year.shape[0])
    data_year_drop_1 = data_year.drop(data_year[data_year['control_task_order_id'] == 9900400].index)
    data_year_drop_2 = data_year_drop_1.drop(data_year_drop_1[data_year_drop_1['control_task_order_id'] == 9900500].index)
    data_year_drop_3 = data_year_drop_2.drop(data_year_drop_2[data_year_drop_2['control_task_order_id'] != 9900300].index)
    data_year_drop_3['Attendance_date'] = 0
    for i in range(data_year_drop_3.shape[0]):
        data_year_drop_3['Attendance_date'].iloc[i] = str(data_year_drop_3['year'].iloc[i]) + '-' + str(
            data_year_drop_3['month'].iloc[i]) + '-' + str(data_year_drop_3['date'].iloc[i])
    print(data_year_drop_3['Attendance_date'])
    data_year_drop_3['count'] = 1
    data_year_drop_3_groupby = data_year_drop_3.groupby(['Attendance_date']).count().reset_index()
    print(data_year_drop_3_groupby)
    calenda_data = []
    for i in range(data_year_drop_3_groupby.shape[0]):
        calenda_data_piece = [data_year_drop_3_groupby['Attendance_date'].iloc[i], int(data_year_drop_3_groupby['count'].iloc[i])]
        calenda_data.append(calenda_data_piece)
    json_data = {"calenda": calenda_data}
    with open('../1.School-level-data/Attendance_8.json', "w") as file:
        json.dump(json_data, file)
    print("完成文件加载")
# create_calenda_earlyData()

# 统计迟到晚到的打卡签到数据
def create_calenda_uniformData():
    print(data_year.shape[0])
    data_year_drop_1 = data_year.drop(data_year[data_year['control_task_order_id'] == 9900400].index)
    data_year_drop_2 = data_year_drop_1.drop(data_year_drop_1[data_year_drop_1['control_task_order_id'] == 9900500].index)
    data_year_drop_3 = data_year_drop_2.drop(data_year_drop_2[data_year_drop_2['control_task_order_id'] != 9900200].index)
    data_year_drop_3['Attendance_date'] = 0
    for i in range(data_year_drop_3.shape[0]):
        data_year_drop_3['Attendance_date'].iloc[i] = str(data_year_drop_3['year'].iloc[i]) + '-' + str(
            data_year_drop_3['month'].iloc[i]) + '-' + str(data_year_drop_3['date'].iloc[i])
    print(data_year_drop_3['Attendance_date'])
    data_year_drop_3['count'] = 1
    data_year_drop_3_groupby = data_year_drop_3.groupby(['Attendance_date']).count().reset_index()
    print(data_year_drop_3_groupby)
    calenda_data = []
    for i in range(data_year_drop_3_groupby.shape[0]):
        calenda_data_piece = [data_year_drop_3_groupby['Attendance_date'].iloc[i], int(data_year_drop_3_groupby['count'].iloc[i])]
        calenda_data.append(calenda_data_piece)
    json_data = {"calenda": calenda_data}
    with open('../1.School-level-data/Attendance_9.json', "w") as file:
        json.dump(json_data, file)
    print("完成文件加载")
# create_calenda_uniformData()
