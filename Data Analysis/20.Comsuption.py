import pandas as pd
import numpy as np
import math
# import datetime
# import time
from datetime import time, datetime
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt

consumption = pd.read_csv('./data/7_consumption.csv')

consumption['PerSex'] = consumption['PerSex'].apply(lambda x: np.NaN if str(x).isspace() else x)
consumption.dropna()
consumption.drop(['AccName'], axis=1, inplace=True)


def absolute_value(s):
    return s if(s > 0) else -s


def string_toDatetime_toWeekday(string):
    return datetime.strptime(string, "%Y/%m/%d").weekday() + 1


def get_date(s):
    date_arr = s.split(' ')[0].split('/')
    if int(date_arr[1]) < 10:
        date_arr[1] = '0' + date_arr[1]
    if int(date_arr[2]) < 10:
        date_arr[2] = '0' + date_arr[2]
    return date_arr[0] + '-' + date_arr[1] + '-' + date_arr[2]


def get_time(s):
    return s.split(' ')[1]


def get_month(s):
    return s[:7]


def nan_to_zero(s):
    if math.isnan(s):
        return 0
    else:
        return int(s)


def get_weekday(s):
    return string_toDatetime_toWeekday(s)


def time_to_idx(s):
    time_arr = gen_time()
    for i in range(len(time_arr)):
        if (s >= time_arr[i][0]) & (s < time_arr[i][1]):
            return i
        else:
            continue
    return -1


def gen_time():
    time_arr = []
    for i in range(24):
        if i < 9:
            time_arr.append(['0' + str(i) + ':00:00', '0' + str(i) + ':30:00'])
            time_arr.append(['0' + str(i) + ':30:00', '0' + str(i+1) + ':00:00'])
        elif i == 9:
            time_arr.append(['0' + str(i) + ':00:00', '0' + str(i) + ':30:00'])
            time_arr.append(['0' + str(i) + ':30:00', str(i+1) + ':00:00'])
        else:
            time_arr.append([str(i) + ':00:00', str(i) + ':30:00'])
            time_arr.append([str(i) + ':30:00', str(i+1) + ':00:00'])
    return time_arr


def gen_date_week():
    arr = []
    for i in range(30):
        if i+1 < 10:
            arr.append(['2018/09/' + '0' + str(i+1)])
        else:
            arr.append(['2018/09/' + str(i+1)])
    for i in range(31):
        if i+1 < 10:
            arr.append(['2018/10/' + '0' + str(i+1)])
        else:
            arr.append(['2018/10/' + str(i+1)])
    for i in range(30):
        if i+1 < 10:
            arr.append(['2018/11/' + '0' + str(i+1)])
        else:
            arr.append(['2018/11/' + str(i+1)])
    for i in range(31):
        if i+1 < 10:
            arr.append(['2018/12/' + '0' + str(i+1)])
        else:
            arr.append(['2018/12/' + str(i+1)])
    for i in range(30):
        if i+1 < 10:
            arr.append(['2019/01/' + '0' + str(i+1)])
        else:
            arr.append(['2019/01/' + str(i+1)])
    for i in range(2, len(arr)-3):
        arr[i].append(((i - 2) // 7) + 1)
    return pd.DataFrame(arr).rename(index=str, columns={0: 'Date', 1: 'Week'})


def init_time_num():
    arr = []
    for i in range(21):
        for j in range(48):
            arr.append([i+1, j])
    return pd.DataFrame(arr).rename(index=str, columns={0: 'Week', 1: 'time_index'})


# 金额变成正数
consumption['MonDeal'] = consumption['MonDeal'].apply(absolute_value)
# 增加日期
consumption['Date'] = consumption['DealTime'].apply(get_date)
# 增加时间
consumption['Time'] = consumption['DealTime'].apply(get_time)
# 增加月份
# consumption['Month'] = consumption['Date'].apply(get_month)

# 日期表
# t1 = consumption[['Date', 'bf_StudentID']][consumption['PerSex'] == '男']
# t1.insert(0, 'male', 1)
# male_num = t1.drop_duplicates()[['Date', 'male']].groupby('Date').sum()
# male_num_df = male_num.reset_index().rename(str.lower, axis='columns')
# t2 = consumption[['Date', 'bf_StudentID']][consumption['PerSex'] == '女']
# t2.insert(0, 'female', 1)
# female_num = t2.drop_duplicates()[['Date', 'female']].groupby('Date').sum()
# female_num_df = female_num.reset_index().rename(str.lower, axis='columns')
# gender_df = pd.merge(male_num_df, female_num_df, how='outer')
# gender_df['female'] = gender_df['female'].apply(nan_to_zero)
# gender_df.insert(3, 'weekday', 0)
# gender_df['weekday'] = gender_df['date'].apply(get_weekday)
# t3 = consumption[['Date', 'MonDeal']][consumption['PerSex'] == '男'].groupby('Date').sum().reset_index()
# t4 = consumption[['Date', 'MonDeal']][consumption['PerSex'] == '女'].groupby('Date').sum().reset_index()
# male_money = t3.rename(index=str, columns={'Date': 'date', 'MonDeal': 'male_money'})
# female_money = t4.rename(index=str, columns={'Date': 'date', 'MonDeal': 'female_money'})
# gender_money = pd.merge(male_money, female_money, how='outer')
# gender_money['female_money'] = gender_money['female_money'].apply(nan_to_zero)
# csp_date = pd.merge(gender_df, gender_money, how='outer')
# print(csp_date)
# csp_date.to_json('./csp_date_gender.json', orient='split')

# 消费次数-消费金额表
# t1 = consumption[['bf_StudentID']]
# t1.insert(0, 'times', 1)
# t_t = t1.groupby('bf_StudentID').sum().reset_index()
# t2 = consumption[['bf_StudentID', 'MonDeal']]
# t_m = t2.groupby('bf_StudentID').sum().reset_index()
# times_money_df = pd.merge(t_t, t_m, how='outer')
# times_money_df['mean_money'] = times_money_df['MonDeal'] / times_money_df['times']
# # times_money_df.drop(['bf_StudentID'], axis=1, inplace=True)
# times_money_df.rename(index=str, columns={'MonDeal': 'total_money'}, inplace=True)
# print(times_money_df['bf_StudentID'][times_money_df['times'] < 180][times_money_df['total_money'] < 1700][times_money_df['mean_money'] < 7.5].value_counts().index)
# # times_money_df.to_json('./csp_times_money.json', orient='split')

# 周时刻表
# t = consumption[['Date', 'Time', 'bf_StudentID']][consumption['Time'] > '05:30:00']
# t.insert(0, 'time_index', t['Time'].apply(time_to_idx))
# t1 = pd.merge(t, gen_date_week(), how='left')[['Week', 'time_index']].dropna()
# t1['Week'] = t1['Week'].apply(nan_to_zero)
# t1.insert(2, 'people_num', 1)
# t2 = t1.groupby(['Week', 'time_index']).sum().reset_index()
# t3 = pd.merge(t2, init_time_num(), how='outer')
# t3['people_num'] = t3['people_num'].apply(nan_to_zero)
# week_time = t3.sort_values(by=['Week', 'time_index']).rename(str.lower, axis='columns')
# print(week_time)
# week_time.to_json('./csp_time_num.json', orient='split')

def date_str(s):
    return str(s).split(' ')[0]

def no_date(s):
    return int(s.split('-')[2]) - 1

def date_del_day(s):
    return s[:7]

def to_int(s):
    if math.isnan(s):
        return -1
    return int(s)

pinkunsheng = [14716, 14397, 14395, 15546, 15928, 14390, 14389, 14899, 15922,
               15744, 14381, 14891, 15914, 14887, 14374, 14884, 15907, 15777,
               14365, 14411, 15926, 14987, 14994, 14190, 15936, 15954, 14978,
               15932, 14910, 14118, 15935, 14330, 15861, 14387, 14939, 14442,
               14439, 15718, 14050, 14940, 14427, 14936, 15574, 13012, 14931,
               14930, 14928, 14925, 14155, 15690, 14921, 14535, 14917, 15939,
               14913, 14912, 14080]
pks_id = pd.DataFrame(pinkunsheng).rename(index=str, columns={0: 'bf_StudentID'})
# a = (pd.merge(consumption[['bf_StudentID', 'PerSex', 'Date', 'Time', 'MonDeal']], pks_id, how='right'))
# a.insert(0, 'z', 1)
# a1 = a.groupby(['bf_StudentID', 'Date']).sum().reset_index().drop(['MonDeal'], axis=1)
# date_all = pd.DataFrame(pd.date_range('9/1/2018','1/30/2019', name='Date'))
# date_all['Date'] = date_all['Date'].apply(date_str)
# a2 = pd.merge(date_all, a1, how='left').sort_values(by=['bf_StudentID', 'Date'])
# no_stu = a2['bf_StudentID'].value_counts().sort_index().reset_index().drop(['bf_StudentID'], axis=1).reset_index().rename(index=str, columns={'level_0': 'y', 'index': 'bf_StudentID'})
# a2.insert(0, 'x', a2['Date'])
# a2['x'] = a2['x'].apply(no_date)
# a3 = pd.merge(a2, no_stu, how='left')
# a3['Date'] = a3['Date'].apply(date_del_day)
# a3 = a3.rename(index=str, columns={'Date': 'Month', 'bf_StudentID': 'ID'}).set_index('Month').sort_index()
# a3['x'] = a3['x'].apply(to_int)
# a3['y'] = a3['y'].apply(to_int)
# a3['z'] = a3['z'].apply(to_int)
# a3['ID'] = a3['ID'].apply(to_int)
# a_res = a3[['x', 'y', 'z', 'ID']]
# print(a_res)
# # a_res.to_json('./poor_stu_csp_times.json', orient='split')

b = (pd.merge(consumption[['bf_StudentID', 'PerSex', 'Date', 'Time', 'MonDeal']], pks_id, how='right'))
b1 = b.drop(['PerSex'], axis=1).rename(index=str, columns={'bf_StudentID': 'ID', 'MonDeal': 'Money'}).sort_values(by=['ID', 'Date', 'Time'])
b2 = b1.set_index('ID').drop(['Time'], axis=1)
print(b2)
b2.to_json('./poor_stu_csp_money.json', orient='split')
