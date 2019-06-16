import pandas as pd
import numpy as np
import time
import math
import json
import matplotlib.pyplot as plt

# teacher = pd.read_csv("./data/1_teacher.csv")
student_info = pd.read_csv("./data/2_student_info.csv")
kaoqin = pd.read_csv("./data/3_kaoqin.csv")
# kaoqin_type = pd.read_csv("./data/4_kaoqintype.csv")
chengji = pd.read_csv("./data/5_chengji.csv")
csp = pd.read_csv("./data/7_consumption.csv")
# stu_index = pd.read_csv("./data/stu_index.csv")
# stu_index.rename(index=str, columns={'Unnamed: 0': 'stu_id'}, inplace=True)

def formatDatetime(s):
    return time.strftime("%Y-%m-%d", time.strptime(s, "%Y/%m/%d %H:%M:%S"))

def to_int(s):
    return int(s)

def percentile25(arr):
    return np.percentile(arr, (25), interpolation='midpoint')

def percentile50(arr):
    return np.percentile(arr, (50), interpolation='midpoint')

def percentile75(arr):
    return np.percentile(arr, (75), interpolation='midpoint')

def sum_per(s):
    return sum(s)/len(s)

def round_int(s):
    return math.ceil(s)

# 高三1班到高三10班的id
class_id_arr = [921, 916, 917, 918, 922, 924, 919, 920, 923, 925]
class_id = 920
# 班级数据
# one_class = student_info[student_info['cla_id'] == class_id]
# a = one_class[(one_class['bf_leaveSchool'] != '1')].drop(['cla_term', 'bf_leaveSchool'], axis=1)
# 各学科教师
# b = teacher[(teacher['cla_id'] == class_id)]
# 消费
def xiaofei(class_id):
    # 班级数据
    one_class = student_info[student_info['cla_id'] == class_id]
    a = one_class[(one_class['bf_leaveSchool'] != '1')].drop(['cla_term', 'bf_leaveSchool'], axis=1)
    c = pd.merge(csp, a[['bf_StudentID']], how='right')
    c.dropna(axis=0, how='any', inplace=True)
    c['MonDeal'] = c['MonDeal'].apply(lambda s: -float(s))
    c['DealTime'] = c['DealTime'].apply(formatDatetime)
    c1 = c[['DealTime', 'MonDeal']]
    c11 = c1.groupby('DealTime').sum().reset_index()  # 每天消费总额
    c2 = c[['DealTime', 'bf_StudentID']]
    c2.drop_duplicates(subset=['DealTime', 'bf_StudentID'], keep='first', inplace=True)
    c2.insert(2, 'csp_num', 1)
    c2.drop(['bf_StudentID'], axis=1, inplace=True)
    c22 = c2.groupby('DealTime').sum().reset_index()  # 每天消费人数
    c3 = pd.merge(c11, c22, how='outer')
    c3 = c3[c3['csp_num'] >= 20]
    c4 = c[['DealTime', 'MonDeal', 'bf_StudentID']]
    c4_1 = c4.groupby(['DealTime', 'bf_StudentID']).sum().reset_index()
    c4_2 = c4_1[['DealTime', 'MonDeal']]
    c4_2_max = c4_2.groupby('DealTime').max().reset_index().rename(index=str, columns={'MonDeal': 'max'})
    c4_2_min = c4_2.groupby('DealTime').min().reset_index().rename(index=str, columns={'MonDeal': 'min'})
    c4_2_mean = c4_2.groupby('DealTime').mean().reset_index().rename(index=str, columns={'MonDeal': 'mean'})
    c_res = pd.merge(c3, c4_2_max, how='left')
    c_res = pd.merge(c_res, c4_2_min, how='left')
    c_res = pd.merge(c_res, c4_2_mean, how='left')
    c_res = c_res.set_index('DealTime')
    c_res.rename(index=str, columns={'MonDeal': 'total', 'csp_num': 'peo_num'}, inplace=True)
    c_res = c_res[
        (c_res['total'] > 200) &
        (c_res['total'] < 1500)]
    return c_res

# 考勤
d = kaoqin[kaoqin['bf_classid'] == 920]
d1 = d[['DataDateTime', 'controler_name', 'bf_studentID']]
d1['DataDateTime'] = d1['DataDateTime'].apply(formatDatetime)
d1['controler_name'] = d1['controler_name'].apply(lambda s: s[:2])
d1.insert(3, 'peo_num', 1)
d2 = d1.groupby(['DataDateTime', 'controler_name']).sum().reset_index().sort_values(by=['DataDateTime'])
print(d2)
# obj = {}
# obj['离校'] = np.array(d2[['DataDateTime', 'peo_num']][d2['controler_name']=='离校']).tolist()
# obj['进校'] = np.array(d2[['DataDateTime', 'peo_num']][d2['controler_name']=='进校']).tolist()
# obj['迟到'] = np.array(d2[['DataDateTime', 'peo_num']][d2['controler_name']=='迟到']).tolist()
# obj['校服'] = np.array(d2[['DataDateTime', 'peo_num']][d2['controler_name']=='校服']).tolist()
# print(obj)
# json1 = json.dumps(obj,ensure_ascii=False,indent=2)
# print(json1)
# fl=open('./class920_kq.json', 'w')
# fl.write(json1)
# fl.close()
# 成绩
'''
2	期中
3	期末
4	平时(总评用)
5	总评
6	五校联考
7	十校联考
8	初三模拟考
9	模拟考
10	中考估分
11	体育健康标准
12	中考
13	等级
14	学分
15	选修课
16	总评
17	校本课程
18	考查课总评
19	期始考
20	期中考试
21	期末考试
22	平时1
'''
# chengji['exam_numname'] = chengji['exam_numname'].apply(lambda s: s[1:] if '\t' in s else s)
# chengji.drop_duplicates(subset=['exam_number', 'mes_sub_id', 'mes_StudentID'], keep='last', inplace=True)
# e = pd.merge(chengji, a[['bf_StudentID']], how='right', left_on='mes_StudentID', right_on='bf_StudentID')
# e1表示主学科
'''
2016学年度第一学期期中考试   265
2016学年度第一学期期末考试   267
2016学年度第一学期期末总评   269 

2016学年度第二学期期中考试   271 
2016学年度第二学期期末考试    279
2016学年度第二学期总评      280

2017学年度第一学期期中考试     284
2017学年度第一学期期末考试     288
2017学年度第一学期期末总评     289

2017学年度第二学期期中考试       292
2017学年度第二学期期末考试       298
2017学年第二学期期末总评        299

2018学年第一学期高三十校联考    301
2018学年第一学期高三五校联考    302
2018-1学期期中考试         304
'''
def zhuxueke(class_id):
    # 班级数据
    one_class = student_info[student_info['cla_id'] == class_id]
    a = one_class[(one_class['bf_leaveSchool'] != '1')].drop(['cla_term', 'bf_leaveSchool'], axis=1)
    e = pd.merge(chengji, a[['bf_StudentID']], how='right', left_on='mes_StudentID', right_on='bf_StudentID')
    e1 = e[['exam_number', 'exam_numname', 'mes_sub_id', 'mes_sub_name', 'exam_term', 'mes_StudentID', 'mes_Score', 'mes_Z_Score', 'mes_T_Score', 'mes_dengdi']][(~e['exam_numname'].str.contains('考查')) & (~e['exam_numname'].str.contains('考察'))]
    e1 = e1[
        (e1['exam_number'] == 265) |
        (e1['exam_number'] == 267) |
        (e1['exam_number'] == 269) |
        (e1['exam_number'] == 271) |
        (e1['exam_number'] == 279) |
        (e1['exam_number'] == 280) |
        (e1['exam_number'] == 284) |
        (e1['exam_number'] == 288) |
        (e1['exam_number'] == 289) |
        (e1['exam_number'] == 292) |
        (e1['exam_number'] == 298) |
        (e1['exam_number'] == 299) |
        (e1['exam_number'] == 301) |
        (e1['exam_number'] == 302) |
        (e1['exam_number'] == 304)]
    # # 学科分数-人数
    # e1_1 = e1[['exam_number', 'exam_numname', 'mes_sub_name', 'mes_StudentID', 'mes_Score']][e1['mes_Score'] >= 0]
    # e1_2 = e1_1.groupby(['exam_number', 'exam_numname', 'mes_StudentID']).sum().reset_index()
    # e1_2.insert(2, 'mes_sub_name', '总分')
    # e1_3 = pd.concat([e1_1, e1_2]).sort_values(by=['exam_numname', 'mes_StudentID']).drop(['mes_StudentID'], axis=1)
    # e1_3.insert(0, 'peo_num', 1)
    # e1_3['mes_Score'] = e1_3['mes_Score'].apply(round_int)
    # e1_4 = e1_3.groupby(['exam_number', 'exam_numname', 'mes_sub_name', 'mes_Score']).sum().reset_index()
    # e1_5 = e1_4[e1_4['mes_sub_name']!='总分'].sort_values(by=['exam_number', 'mes_sub_name', 'mes_Score']).drop(['exam_number'], axis=1).set_index('exam_numname')
    # # print(e1_5)
    # # e1_5[['mes_Score', 'peo_num', 'mes_sub_name']].to_json('./class920_sub_score_peo_num.json', orient='split')
    # e1_6 = e1_4[e1_4['mes_sub_name']=='总分']
    # e1_6.insert(0, '>700', 0)
    # e1_6.insert(0, '600_700', 0)
    # e1_6.insert(0, '500_600', 0)
    # e1_6.insert(0, '400_500', 0)
    # e1_6.insert(0, '300_400', 0)
    # e1_6.insert(0, '200_300', 0)
    # e1_6.insert(0, '100_200', 0)
    # def t(df):
    #     if df['mes_Score'] < 200:
    #         df['100_200'] += df['peo_num']
    #     elif df['mes_Score'] < 300:
    #         df['200_300'] += df['peo_num']
    #     elif df['mes_Score'] < 400:
    #         df['300_400'] += df['peo_num']
    #     elif df['mes_Score'] < 500:
    #         df['400_500'] += df['peo_num']
    #     elif df['mes_Score'] < 600:
    #         df['500_600'] += df['peo_num']
    #     elif df['mes_Score'] < 700:
    #         df['600_700'] += df['peo_num']
    #     else:
    #         df['>700'] += df['peo_num']
    #     return df
    # e1_7 = e1_6.apply(t, axis=1).groupby(['exam_number', 'exam_numname']).sum().reset_index()
    # e1_8 = e1_7.drop(['exam_number', 'mes_Score', 'peo_num'], axis=1).set_index('exam_numname')
    # # print(e1_8)
    # # e1_8.to_json('./class920_total_score_segment.json', orient='split')

    # # 学科箱线图
    # e1_1 = e1[['exam_number', 'exam_numname', 'mes_sub_name', 'mes_StudentID', 'mes_T_Score']][e1['mes_Score'] >= 0]
    # e1_2 = e1_1.groupby(['exam_number', 'exam_numname', 'mes_StudentID']).sum().reset_index()
    # e1_2.insert(2, 'mes_sub_name', '总分')
    # e1_3 = pd.concat([e1_1, e1_2]).sort_values(by=['exam_numname', 'mes_StudentID']).drop(['mes_StudentID'], axis=1)
    # e1_q1 = e1_3.groupby(['exam_number', 'exam_numname', 'mes_sub_name']).agg(percentile25).reset_index().rename(index=str, columns={'mes_T_Score': 'q1'})
    # e1_q2 = e1_3.groupby(['exam_number', 'exam_numname', 'mes_sub_name']).agg(percentile50).reset_index().rename(index=str, columns={'mes_T_Score': 'q2'})
    # e1_q3 = e1_3.groupby(['exam_number', 'exam_numname', 'mes_sub_name']).agg(percentile75).reset_index().rename(index=str, columns={'mes_T_Score': 'q3'})
    # e1_4 = pd.merge(e1_q1, pd.merge(e1_q2, e1_q3, how='outer'), how='outer')
    # e1_4.insert(3, 'lower', e1_4['q1'] - 1.5*(e1_4['q3'] - e1_4['q1']))
    # e1_4.insert(7, 'upper', e1_4['q3'] + 1.5*(e1_4['q3'] - e1_4['q1']))
    # e1_5 = pd.merge(e1_3, e1_4, how='left')
    # e1_5.insert(0, 'state', 0)
    # e1_5.loc[e1_5['mes_T_Score'] < e1_5['lower'], 'state'] = 1
    # e1_5.loc[e1_5['mes_T_Score'] > e1_5['upper'], 'state'] = 2
    # e1_5 = e1_5.sort_values(by=['exam_number'])
    # e1_6 = e1_5[['exam_numname', 'mes_sub_name', 'mes_T_Score']][e1_5['state'] != 0].set_index('exam_numname')
    # e1_7 = e1_4.sort_values(by=['exam_number', 'mes_sub_name']).drop(['exam_number'], axis=1).set_index('exam_numname')
    # print(e1_7)
    # print(e1_6)
    # # e1_7[['lower', 'q1', 'q2', 'q3', 'upper', 'mes_sub_name']].to_json('./class920_box_data.json', orient='split');
    # # e1_6[['mes_T_Score', 'mes_sub_name']].to_json('./class920_box_outlier.json', orient='split')


    # 成绩趋势
    # e2 = e1[['exam_number', 'exam_numname', 'mes_sub_name', 'mes_StudentID', 'mes_T_Score']][e1['mes_Score'] >= 0].sort_values(by=['exam_number'])
    # e2_max = e2.drop(['mes_StudentID'], axis=1).groupby(['exam_number', 'exam_numname', 'mes_sub_name']).max().reset_index().sort_values(by=['mes_sub_name', 'exam_number'])
    # e2_min = e2.drop(['mes_StudentID'], axis=1).groupby(['exam_number', 'exam_numname', 'mes_sub_name']).min().reset_index().sort_values(by=['mes_sub_name', 'exam_number'])
    # e2_mean = e2.drop(['mes_StudentID'], axis=1).groupby(['exam_number', 'exam_numname', 'mes_sub_name']).mean().reset_index().sort_values(by=['mes_sub_name', 'exam_number'])
    # e2_sum = e2.groupby(['exam_number', 'exam_numname', 'mes_StudentID']).agg(sum_per).reset_index()
    # e2_sum_max = e2_sum.drop(['mes_StudentID'],axis=1).groupby(['exam_number', 'exam_numname']).max().reset_index().sort_values(by=['exam_number'])
    # e2_sum_min = e2_sum.drop(['mes_StudentID'],axis=1).groupby(['exam_number', 'exam_numname']).min().reset_index().sort_values(by=['exam_number'])
    # e2_sum_mean = e2_sum.drop(['mes_StudentID'],axis=1).groupby(['exam_number', 'exam_numname']).mean().reset_index().sort_values(by=['exam_number'])
    # e2_sum_max.insert(2, 'mes_sub_name', '总分')
    # e2_sum_min.insert(2, 'mes_sub_name', '总分')
    # e2_sum_mean.insert(2, 'mes_sub_name', '总分')
    # e2_max_res = pd.concat([e2_max, e2_sum_max]).sort_values(by=['mes_sub_name', 'exam_number']).rename(index=str, columns={'mes_T_Score': 'max'})
    # e2_min_res = pd.concat([e2_min, e2_sum_min]).sort_values(by=['mes_sub_name', 'exam_number']).rename(index=str, columns={'mes_T_Score': 'min'})
    # e2_mean_res = pd.concat([e2_mean, e2_sum_mean]).sort_values(by=['mes_sub_name', 'exam_number']).rename(index=str, columns={'mes_T_Score': 'mean'})
    # e2_res = pd.merge(e2_max_res, pd.merge(e2_min_res, e2_mean_res, how='outer'), how='outer').sort_values(by=['mes_sub_name', 'exam_numname']).drop(['exam_number', 'exam_numname'], axis=1)
    # print(e2_res)

    # obj = {}
    # for i in e2_res['mes_sub_name']:
    #     t_list = []
    #     t_list.append(list(e2_res['max'][e2_res['mes_sub_name']==i]))
    #     t_list.append(list(e2_res['min'][e2_res['mes_sub_name']==i]))
    #     t_list.append(list(e2_res['mean'][e2_res['mes_sub_name']==i]))
    #     obj[i] = t_list
    # json1 = json.dumps(obj,ensure_ascii=False,indent=2)
    # print(json1)
    # fl=open('./sub_trend.json', 'w')
    # fl.write(json1)
    # fl.close()




def kaochake(class_id):
    # 班级数据
    one_class = student_info[student_info['cla_id'] == class_id]
    a = one_class[(one_class['bf_leaveSchool'] != '1')].drop(['cla_term', 'bf_leaveSchool'], axis=1)
    e = pd.merge(chengji, a[['bf_StudentID']], how='right', left_on='mes_StudentID', right_on='bf_StudentID')
    # e2表示考查课
    # 2016-1 266
    # 2016-2 277
    # 2017-1 286
    # 2017-2 293
    # 2018-1 306
    e2 = e[['exam_number', 'exam_numname', 'mes_sub_id', 'mes_sub_name', 'mes_StudentID', 'mes_Score']][e['mes_Score'] >= 0]
    e2 = e2[
        (e2['exam_number'] == 266) |
        (e2['exam_number'] == 277) |
        (e2['exam_number'] == 286) |
        (e2['exam_number'] == 293) |
        (e2['exam_number'] == 306)].sort_values(by=['exam_number'])

    e2 = e2.fillna({'mes_sub_id': 9, 'mes_sub_name': '体育'})
    e2.loc[e2['mes_sub_id'] == 9, 'mes_sub_id'] = 0  # 体育
    e2.loc[e2['mes_sub_id'] == 11, 'mes_sub_id'] = 1  # 音乐
    e2.loc[e2['mes_sub_id'] == 12, 'mes_sub_id'] = 2  # 美术
    e2.loc[e2['exam_number'] == 266, 'exam_numname'] = '2016-2017-1'
    e2.loc[e2['exam_number'] == 277, 'exam_numname'] = '2016-2017-2'
    e2.loc[e2['exam_number'] == 286, 'exam_numname'] = '2017-2018-1'
    e2.loc[e2['exam_number'] == 293, 'exam_numname'] = '2017-2018-2'
    e2.loc[e2['exam_number'] == 306, 'exam_numname'] = '2018-2019-1'
    e2_1 = e2[['exam_numname', 'mes_sub_id', 'mes_Score']].rename(index=str, columns={'mes_sub_id': 'y', 'mes_Score': 'x'})
    e2_1.insert(0, 'z', 1)
    e2_2 = e2_1.groupby(['exam_numname', 'x', 'y']).sum().reset_index()
    e2_res = e2_2.set_index('exam_numname')
    e2_res['x'] = e2_res['x'] - 60
    e2_res['x'] = e2_res['x'].apply(to_int)
    e2_res['y'] = e2_res['y'].apply(to_int)
    e2_res['z'] = e2_res['z'].apply(to_int)
    return e2_res


# 输出高三各班考查课数据
# for i in class_id_arr:
    # kaochake(i).to_json('./class' + str(i) + '_associate_sub.json', orient='split')
# 输出高三各班的消费数据
# for i in class_id_arr:
    # xiaofei(i).to_json('./class' + str(i) + '_csp.json', orient='split')
# 输出高三各班的主学科数据
# for i in class_id_arr:
#     print('*** ' + str(i) + ' ***')
#     zhuxueke(i)
# zhuxueke(920)
# for i in class_id_arr:
    # 班级数据
    # one_class = student_info[student_info['cla_id'] == class_id]
    # a = one_class[(one_class['bf_leaveSchool'] != '1')].drop(['cla_term', 'bf_leaveSchool'], axis=1)
    # e = pd.merge(chengji, a[['bf_StudentID']], how='right', left_on='mes_StudentID', right_on='bf_StudentID')

# print(chengji[['exam_number', 'exam_numname']][
#     (chengji['exam_term'].str.contains('2016-2017')) |
#     (chengji['exam_term'].str.contains('2017-2018')) |
#     (chengji['exam_term'].str.contains('2018-2019'))].drop_duplicates(keep='first'))