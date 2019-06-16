import pandas as pd

chengji = pd.read_csv("./data/5_chengji.csv")
exam_type = pd.read_csv('./data/6_exam_type.csv')
student_info = pd.read_csv("./data/2_student_info.csv")

# 缺失值查看
print('\n********** 缺失值查看 **********')
for i in chengji.columns:
    if len(chengji[chengji[i].isnull()==True]) != 0:
        print(i, '有缺失值')

# 考试科目
print('\n********** 考试科目 **********')
print(chengji['mes_sub_name'].value_counts().index)

# 总共有86次考试
print('\n********** 考试次数 **********')
print('根据考试编号，总共有', len(chengji['exam_number'].value_counts()), '次考试')
print('根据考试名称，总共有', len(chengji['exam_numname'].value_counts()), '次考试')

# 考试按时间排序
print('\n********** 考试顺序 **********')


def f1(s):
    t1 = s.split(' ')
    t2 = t1[0].split('/')
    if len(t2[1]) == 1:
        t2[1] = '0' + t2[1]
    if len(t2[2]) == 1:
        t2[2] = '0' + t2[2]
    return t2[0]+'/'+t2[1]+'/'+t2[2]


t = chengji['exam_sdate'].apply(f1).rename('date')
chengji = pd.concat([chengji, t], axis=1)
exam_name = []
for i in chengji.sort_values(by='date')['exam_numname']:
    if i not in exam_name:
        exam_name.append(i)
exam_num = []
for i in chengji.sort_values(by='date')['exam_number']:
    if i not in exam_num:
        exam_num.append(i)
print(pd.concat([pd.Series(exam_num), pd.Series(exam_name)], axis=1))

# z-score t-score dengdi 的出现时间 2016/01/12
# 最近的三次考试没有以上三种成绩
print('\n********** 科目缺失的考试，主要都是最近的几次考试 **********')
print(chengji['exam_numname'][chengji['mes_sub_id'].isnull()==True].value_counts())

print('\n********** 考试类型 **********')
for i in [2, 3, 4, 5, 6, 7, 8, 9, 18, 19, 22]:
    print(i, exam_type['EXAM_KIND_NAME'][exam_type['EXAM_KIND_ID'] == i].iloc[0])

print('\n********** 2013-2014学年考试 13场 **********')
idx_13_14 = chengji['exam_number'][chengji['date'] >= '2013/08/01'][chengji['date'] < '2014/08/01'].value_counts().index
for i in idx_13_14:
    print(chengji['exam_numname'][chengji['exam_number'] == i].value_counts().index[0])

print('\n********** 2014-2015学年考试 15场 **********')
idx_14_15 = chengji['exam_number'][chengji['date'] >= '2014/08/01'][chengji['date'] < '2015/08/01'].value_counts().index
for i in idx_14_15:
    print(chengji['exam_numname'][chengji['exam_number'] == i].value_counts().index[0])

print('\n********** 2015-2016学年考试 16场 **********')
idx_15_16 = chengji['exam_number'][chengji['date'] >= '2015/08/01'][chengji['date'] < '2016/08/01'].value_counts().index
for i in idx_15_16:
    print(chengji['exam_numname'][chengji['exam_number'] == i].value_counts().index[0])

print('\n********** 2016-2017学年考试 15场 **********')
idx_16_17 = chengji['exam_number'][chengji['date'] >= '2016/08/01'][chengji['date'] < '2017/08/01'].value_counts().index
for i in idx_16_17:
    print(chengji['exam_numname'][chengji['exam_number'] == i].value_counts().index[0])

print('\n********** 2017-2018学年考试 20场 **********')
idx_17_18 = chengji['exam_number'][chengji['date'] >= '2017/08/01'][chengji['date'] < '2018/08/01'].value_counts().index
for i in idx_17_18:
    print(chengji['exam_numname'][chengji['exam_number'] == i].value_counts().index[0])

print('\n********** 2018-2019学年考试 7场 **********')
idx_18_19 = chengji['exam_number'][chengji['date'] >= '2018/08/01'][chengji['date'] < '2019/08/01'].value_counts().index
for i in idx_18_19:
    print(chengji['exam_numname'][chengji['exam_number'] == i].value_counts().index[0])


def f2(s):
    if ('高三' in s) | ('五校联考' in s) | ('十校联考' in s):
        return 2011
    else:
        return -1


# pd.concat([chengji, chengji['exam_numname'].apply(f2).rename('grade')], axis=1)
print(chengji[chengji['exam_numname'] == '2014年宁波市高三“十校联考”'])
