import pandas as pd
import math
import time
import numpy as np

chengji = pd.read_csv("./data/5_chengji.csv")
# exam_type = pd.read_csv('./data/6_exam_type.csv')
student_info = pd.read_csv("./data/2_student_info.csv")
stu_index = pd.read_csv("./data/stu_index.csv")
stu_index.rename(index=str, columns={'Unnamed: 0': 'stu_id'}, inplace=True)


def nan_to_zero(s):
    if math.isnan(s):
        return 0
    else:
        return int(s)


def del_ht(s):
    if '\t' in s:
        return s[1:]
    else:
        return s


def nan_to_negative_one(s):
    if math.isnan(s):
        return -1
    elif s == int(s):
        return int(s)
    else:
        return format(s, '.2f')


sub_map = {
    '语文': 'yw_',
    '数学': 'sx_',
    '英语': 'yy_',
    '政治': 'zz_',
    '历史': 'ls_',
    '地理': 'dl_',
    '物理': 'wl_',
    '化学': 'hx_',
    '生物': 'sw_',
    '技术': 'js_',
}

# 去掉部分考试名称开头的\t
chengji['exam_numname'] = chengji['exam_numname'].apply(del_ht)

# 考试-班级-总分(最高、最低、平均)-单科分(最高、最低、平均)
stu_and_class = student_info[['bf_StudentID', 'cla_Name']].rename(index=str, columns={'bf_StudentID': 'stu_id', 'cla_Name': 'cla_name'})
t = stu_index[['stu_id']][(stu_index['t_info'] > 0) & (stu_index['t_grade'] > 0)]
t1 = pd.merge(chengji, pd.merge(t, stu_and_class, how='left'), how='left', left_on='mes_StudentID', right_on='stu_id')
t1['stu_id'] = t1['stu_id'].apply(nan_to_zero)
t1.drop_duplicates(subset=['exam_numname', 'mes_sub_name', 'stu_id'],keep='last',inplace=True)
# # t2这里做筛选
# t2 = t1[['exam_numname', 'cla_name', 'stu_id', 'mes_sub_name', 'mes_Score']][(~t1['cla_name'].isnull()) & (t1['mes_Score'] >= 0) & (t1['mes_sub_name'] != '体育') & (t1['mes_sub_name'] != '美术') & (t1['mes_sub_name'] != '音乐') & (t1['exam_term'] == '2018-2019-1')]
# # t2.rename(index=str, columns={'mes_T_Score': 'mes_Score'}, inplace=True)
# # t3包含考试名称、班级、学生、总分
# t3 = t2.groupby(['exam_numname', 'cla_name', 'stu_id']).sum().reset_index()
# # 班级最高分 最低分 平均分
# t_max = t3[['exam_numname', 'cla_name', 'mes_Score']].groupby(['exam_numname', 'cla_name']).max().reset_index()
# t_min = t3[['exam_numname', 'cla_name', 'mes_Score']].groupby(['exam_numname', 'cla_name']).min().reset_index()
# t_mean = t3[['exam_numname', 'cla_name', 'mes_Score']].groupby(['exam_numname', 'cla_name']).mean().reset_index()
# # 总分
# t4 = pd.merge(pd.merge(t_max, t_min, on=['exam_numname', 'cla_name']), t_mean, on=['exam_numname', 'cla_name'])
# t4.rename(index=str, columns={'mes_Score_x': 'max', 'mes_Score_y': 'min', 'mes_Score': 'mean'}, inplace=True)
# # 单科
# t5 = t1[['exam_numname', 'mes_sub_name', 'mes_T_Score', 'cla_name']][(~t1['cla_name'].isnull()) & (t1['mes_Score'] >= 0) & (t1['mes_sub_name'] != '体育') & (t1['mes_sub_name'] != '美术') & (t1['mes_sub_name'] != '音乐')]
# t5.rename(index=str, columns={'mes_T_Score': 'mes_Score'}, inplace=True)

# for i in t5['mes_sub_name'].value_counts().index:
#     temp = t5[t5['mes_sub_name'] == i]
#     sub_max = temp.groupby(['exam_numname', 'cla_name']).max().reset_index().rename(index=str, columns={'mes_Score': sub_map[i]+'max'}).drop(['mes_sub_name'], axis=1)
#     sub_min = temp.groupby(['exam_numname', 'cla_name']).min().reset_index().rename(index=str, columns={'mes_Score': sub_map[i]+'min'}).drop(['mes_sub_name'], axis=1)
#     sub_mean = temp.groupby(['exam_numname', 'cla_name']).mean().reset_index().rename(index=str, columns={'mes_Score': sub_map[i]+'mean'})
#     sub_all = pd.merge(pd.merge(sub_max, sub_min), sub_mean)
#     t4 = pd.merge(t4, sub_all, how='left')

# for i in t4.columns:
#     if (i != 'exam_numname') & (i != 'cla_name'):
#         t4[i] = t4[i].apply(nan_to_negative_one)

# res = t4[(t4['exam_numname'] != '2018学年第一学期期末总评') & (t4['exam_numname'] != '2018-1考查课总评') &
#          (t4['cla_name'] != '高一未分班') & (t4['cla_name'] != '高二未分班') & (t4['cla_name'] != '高三未分班')]

# print(res)
# # res.to_json('./exam_class_score.json', orient='split')


# 考试-班级-学生-排名
# t2 = t1[['exam_number', 'exam_numname', 'cla_name', 'stu_id', 'mes_sub_name', 'mes_T_Score']][(~t1['cla_name'].isnull()) & (t1['mes_Score'] >= 0) & (t1['mes_sub_name'] != '体育') & (t1['mes_sub_name'] != '美术') & (t1['mes_sub_name'] != '音乐') & (t1['exam_term'] == '2018-2019-1')]
# t3 = t2[
#     (t2['exam_numname'] == '2018-1学期期中考试') |
#     (t2['exam_numname'] == '2018学年第一学期高三五校联考') |
#     (t2['exam_numname'] == '2018学年第一学期高三十校联考')]

# 班级排名
# print(t3['mes_T_Score'][t3['exam_number']==302][t3['cla_name'] == '高三(07)'][t3['mes_sub_name'] == '地理'].rank(ascending=False, method='min'))
# t3 = t2.sort_values(by=['exam_numname', 'cla_name', 'stu_id'])
# t3 = t2.groupby(['exam_numname', 'cla_name', 'stu_id']).sum().reset_index()

# # 筛选考试班级
# t_arr = []
# for i in t3['exam_numname'].value_counts().index:
#     for j in ['高一', '高二', '高三']:
#         t4 = t3[t3['exam_numname'] == i][t3['cla_name'].str.contains(j)]
#         t5 = pd.concat([t4, t4['mes_Score'].rank(method="min", ascending=False).rename('rank')], axis=1)
#         t_arr.append(t5)

# t_rank = pd.concat(t_arr)
# t_rank.drop(['mes_Score'], axis=1, inplace=True)
# t6 = t1[['exam_numname', 'cla_name', 'stu_id', 'mes_sub_name', 'mes_Score']][(~t1['cla_name'].isnull()) & (t1['mes_Score'] >= 0) & (t1['mes_sub_name'] != '体育') & (t1['mes_sub_name'] != '美术') & (t1['mes_sub_name'] != '音乐') & (t1['exam_term'] == '2018-2019-1')]
# t7 = t6.sort_values(by=['exam_numname', 'cla_name', 'stu_id'])


# def float_to_int(s):
#     return int(s)


# for i in sub_map:
#     t8 = t7[['exam_numname', 'cla_name', 'stu_id', 'mes_Score']][t7.mes_sub_name == i]
#     arr2 = []
#     for j in t8['exam_numname'].value_counts().index:
#         for k in ['高一', '高二', '高三']:
#             t9 = t8[t8['exam_numname'] == j][t8['cla_name'].str.contains(k)]
#             t10 = pd.concat([t9, t9['mes_Score'].rank(method="min", ascending=False).rename(sub_map[i] + 'rank')], axis=1)
#             t10.drop_duplicates(subset=['exam_numname','cla_name', 'stu_id'],keep='last',inplace=True)
#             t10.drop(['mes_Score'], axis=1, inplace=True)
#             arr2.append(t10)
#     t11 = pd.concat(arr2)
#     t_rank = pd.merge(t_rank, t11, how='left', on=['exam_numname', 'cla_name', 'stu_id'])

# t12 = t_rank.fillna(-1)
# t12['rank'] = t12['rank'].apply(float_to_int)
# for i in sub_map:
#     t12[sub_map[i] + 'rank'] = t12[sub_map[i] + 'rank'].apply(float_to_int)
# print(t12)
# # t12.to_json('./exam_class_stu_rank.json', orient='split')


# def formatDatetime(s):
#     return time.strftime("%Y-%m-%d", time.strptime(s, "%Y/%m/%d %H:%M:%S"))


# # 班级-科目-趋势
# t2 = t1[['exam_sdate', 'exam_term', 'exam_numname', 'exam_type', 'cla_name', 'stu_id', 'mes_sub_name', 'mes_T_Score']][(~t1['cla_name'].isnull()) & (t1['mes_Score'] >= 0) & (t1['mes_sub_name'] != '体育') & (t1['mes_sub_name'] != '美术') & (t1['mes_sub_name'] != '音乐')]
# t2['exam_sdate'] = t2['exam_sdate'].apply(formatDatetime)
# t3 = t2[(t2['exam_term'] != '2015-2016-1') & (t2['exam_term'] != '2015-2016-2')].sort_values(by=['exam_sdate'])
# t4 = t3[(t3['exam_type'] != 18) & (~t3['cla_name'].str.contains('未分班')) & (~t3['cla_name'].str.contains('IB'))]
# t4.drop(['exam_term', 'exam_type'], axis=1, inplace=True)
# # 班级总分
# t5 = t4.drop(['mes_sub_name'], axis=1).groupby(['exam_sdate', 'exam_numname', 'cla_name', 'stu_id']).sum().reset_index()
# t5.insert(4, 'mes_sub_name', '总分')
# # 单科分


# def get_one_sub(sub_name, df):
#     t_sub = df[df['mes_sub_name'] == sub_name]
#     t_max = t_sub.groupby(['exam_sdate', 'exam_numname', 'cla_name']).max().reset_index()
#     t_min = t_sub.groupby(['exam_sdate', 'exam_numname', 'cla_name']).min().reset_index()
#     t_mean = t_sub.groupby(['exam_sdate', 'exam_numname', 'cla_name']).mean().reset_index()
#     t_max.drop(['stu_id', 'mes_sub_name'], axis=1, inplace=True)
#     t_min.drop(['stu_id', 'mes_sub_name'], axis=1, inplace=True)
#     t_mean.drop(['stu_id'], axis=1, inplace=True)
#     flag = True
#     for i in sorted(df['cla_name'].value_counts().index):
#         t_class_max = t_max[t_max['cla_name'] == i].rename(index=str, columns={'mes_T_Score': i}).drop(['cla_name'], axis=1)
#         t_class_min = t_min[t_min['cla_name'] == i].rename(index=str, columns={'mes_T_Score': i}).drop(['cla_name'], axis=1)
#         t_class_mean = t_mean[t_mean['cla_name'] == i].rename(index=str, columns={'mes_T_Score': i}).drop(['cla_name'], axis=1)
#         t_class_max.insert(2, 'type', 'max')
#         t_class_min.insert(2, 'type', 'min')
#         t_class_mean.insert(2, 'type', 'mean')
#         t_one_class = pd.concat([t_class_max, t_class_min, t_class_mean])
#         if flag:
#             t_one_sub = t_one_class
#             flag = False
#         else:
#             t_one_sub = pd.merge(t_one_sub, t_one_class, how='outer')

#     t_one_sub.insert(2, 'sub_name', sub_name)
#     return t_one_sub


# t_all_sub = get_one_sub('总分', t5)
# for i in t4['mes_sub_name'].value_counts().index:
#     t_all_sub = pd.concat([t_all_sub, get_one_sub(i, t4)])

# t_res = t_all_sub.sort_values(by=['sub_name', 'type', 'exam_sdate']).reset_index().fillna(-1)
# t_res.drop(['exam_sdate', 'index'], axis=1, inplace=True)
# print(t_res)
# # t_res.to_json('./class_score_trend.json', orient='split')

# # 班级-分数段-人数
# t2 = t1[['exam_term', 'exam_numname', 'cla_name', 'mes_sub_name', 'stu_id', 'mes_Score']][(~t1['cla_name'].isnull()) & (t1['mes_Score'] >= 0) & (t1['mes_sub_name'] != '体育') & (t1['mes_sub_name'] != '美术') & (t1['mes_sub_name'] != '音乐')]
# # 筛选
# t2 = t2[
#     (t2['mes_Score'] > 0) &
#     (~t2['cla_name'].str.contains('未分班')) &
#     (~t2['cla_name'].str.contains('IB')) &
#     (~t2['exam_term'].str.contains('2015-2016')) &
#     (~t2['exam_numname'].str.contains('2017年9月宁波市“十校联考”')) &
#     (~t2['exam_numname'].str.contains('2018学年度第一学期平时成绩2')) & # 科目缺失
#     (~(t2['exam_term'].str.contains('2016-2017')) | ~(t2['cla_name'].str.contains('高二')))
#     ]
# tx = (t2[(t2['exam_numname'] == '2016学年度第二学期期末考试') & (t2['cla_name'].str.contains('高三')) & (t2['mes_sub_name'] == '英语')])
# tx1 = tx['mes_Score'].value_counts().sort_index()
# print(tx1)
# tx1['index'] = tx1
# print(tx1.sort_values(by=['index']))
# t2.drop(['exam_term'], axis=1, inplace=True)
# t_sum = t2.groupby(['exam_numname', 'cla_name', 'stu_id']).sum().reset_index()

# def t_score_over100_to_100(s):
#     if (s > 100):
#         return 100
#     else:
#         return s

# t2['mes_T_Score'] = t2['mes_T_Score'].apply(t_score_over100_to_100)
# t2.drop(['stu_id'], axis=1, inplace=True)
# t_sum.drop(['stu_id'], axis=1, inplace=True)

# t2.insert(0, '0_40', 0)
# t2.insert(0, '40_60', 0)
# t2.insert(0, '60_70', 0)
# t2.insert(0, '70_80', 0)
# t2.insert(0, '80_90', 0)
# t2.insert(0, '>90', 0)

# t_sum.insert(0, '0_100', 0)
# t_sum.insert(0, '100_200', 0)
# t_sum.insert(0, '200_300', 0)
# t_sum.insert(0, '300_400', 0)
# t_sum.insert(0, '400_500', 0)
# t_sum.insert(0, '500_600', 0)
# t_sum.insert(0, '600_700', 0)
# t_sum.insert(0, '700_800', 0)
# t_sum.insert(0, '>800', 0)

# def sub_score_to_times(df):
#     if df['mes_T_Score'] <= 40:
#         df['0_40'] += 1
#     elif df['mes_T_Score'] <= 60:
#         df['40_60'] += 1
#     elif df['mes_T_Score'] <= 70:
#         df['60_70'] += 1
#     elif df['mes_T_Score'] <= 80:
#         df['70_80'] += 1
#     elif df['mes_T_Score'] <= 90:
#         df['80_90'] += 1
#     elif df['mes_T_Score'] <= 100:
#         df['>90'] += 1
#     return df

# def sum_score_to_times(df):
#     if df['mes_T_Score'] <= 100:
#         df['0_100'] += 1
#     elif df['mes_T_Score'] <= 200:
#         df['100_200'] += 1
#     elif df['mes_T_Score'] <= 300:
#         df['200_300'] += 1
#     elif df['mes_T_Score'] <= 400:
#         df['300_400'] += 1
#     elif df['mes_T_Score'] <= 500:
#         df['400_500'] += 1
#     elif df['mes_T_Score'] <= 600:
#         df['500_600'] += 1
#     elif df['mes_T_Score'] <= 700:
#         df['600_700'] += 1
#     elif df['mes_T_Score'] <= 800:
#         df['700_800'] += 1
#     elif df['mes_T_Score'] <= 1000:
#         df['>800'] += 1
#     return df

# t_sub = t2.apply(sub_score_to_times, axis=1)
# t_sum = t_sum.apply(sum_score_to_times, axis=1)
# t_sub.drop(['mes_T_Score'], axis=1, inplace=True)
# t_sum.drop(['mes_T_Score'], axis=1, inplace=True)
# t_sub_num = t_sub.groupby(['exam_numname', 'cla_name', 'mes_sub_name']).sum().reset_index()
# t_sum_num = t_sum.groupby(['exam_numname', 'cla_name']).sum().reset_index()
# sub_res = t_sub_num[['exam_numname', 'mes_sub_name', 'cla_name', '>90', '80_90', '70_80', '60_70', '40_60', '0_40']].sort_values(by=['exam_numname', 'mes_sub_name', 'cla_name'])
# sum_res = t_sum_num.sort_values(by=['exam_numname', 'cla_name'])
# sub_res.to_json('./sub_score_grade_segment.json', orient='split')
# sum_res.to_json('./total_score_grade_segment.json', orient='split')

def percentile25(arr):
    return np.percentile(arr, (25), interpolation='midpoint')

def percentile50(arr):
    return np.percentile(arr, (50), interpolation='midpoint')

def percentile75(arr):
    return np.percentile(arr, (75), interpolation='midpoint')

e1_1 = t1[['exam_number', 'exam_numname', 'mes_sub_name', 'cla_name', 'mes_StudentID', 'mes_T_Score']][(t1['mes_Score'] >= 0) & (t1['exam_numname'] == '2018-1学期期中考试')]
# e1_1 = e1_1[e1_1['cla_name'].str.contains('高一')].drop(['cla_name'], axis=1)
# e1_1 = e1_1[e1_1['cla_name'].str.contains('高二')].drop(['cla_name'], axis=1)
e1_1 = e1_1[e1_1['cla_name'].str.contains('高三')].drop(['cla_name'], axis=1)
e1_2 = e1_1.groupby(['exam_number', 'exam_numname', 'mes_StudentID']).sum().reset_index()
e1_2.insert(2, 'mes_sub_name', '总分')
e1_3 = pd.concat([e1_1, e1_2]).sort_values(by=['exam_numname', 'mes_StudentID']).drop(['mes_StudentID'], axis=1)
e1_q1 = e1_3.groupby(['exam_number', 'exam_numname', 'mes_sub_name']).agg(percentile25).reset_index().rename(index=str, columns={'mes_T_Score': 'q1'})
e1_q2 = e1_3.groupby(['exam_number', 'exam_numname', 'mes_sub_name']).agg(percentile50).reset_index().rename(index=str, columns={'mes_T_Score': 'q2'})
e1_q3 = e1_3.groupby(['exam_number', 'exam_numname', 'mes_sub_name']).agg(percentile75).reset_index().rename(index=str, columns={'mes_T_Score': 'q3'})
e1_4 = pd.merge(e1_q1, pd.merge(e1_q2, e1_q3, how='outer'), how='outer')
e1_4.insert(3, 'lower', e1_4['q1'] - 1.5*(e1_4['q3'] - e1_4['q1']))
e1_4.insert(7, 'upper', e1_4['q3'] + 1.5*(e1_4['q3'] - e1_4['q1']))
e1_5 = pd.merge(e1_3, e1_4, how='left')
e1_5.insert(0, 'state', 0)
e1_5.loc[e1_5['mes_T_Score'] < e1_5['lower'], 'state'] = 1
e1_5.loc[e1_5['mes_T_Score'] > e1_5['upper'], 'state'] = 2
e1_5 = e1_5.sort_values(by=['exam_number'])
e1_6 = e1_5[['exam_numname', 'mes_sub_name', 'mes_T_Score']][e1_5['state'] != 0].set_index('exam_numname')
e1_7 = e1_4.sort_values(by=['exam_number', 'mes_sub_name']).drop(['exam_number'], axis=1).set_index('exam_numname')
print(e1_7)
print(e1_6)
e1_7[['lower', 'q1', 'q2', 'q3', 'upper', 'mes_sub_name']].to_json('./grade3_box_data.json', orient='split')
e1_6[['mes_T_Score', 'mes_sub_name']].to_json('./grade3_box_outlier.json', orient='split')