import pandas as pd
import numpy as np

consumption = pd.read_csv('../../education_data/7_consumption.csv')

consumption['PerSex'] = consumption['PerSex'].apply(lambda x: np.NaN if str(x).isspace() else x)
consumption.dropna()


def func1(s):
    q = s.split(' ')
    return q[0]


def func2(s):
    q = s.rpartition('/')
    return q[0]


def func3(s):
    b = s.split(' ')
    q = b[0].split('/')
    n = len(q)
    for i in range(1, n):
        if len(q[i]) == 1:
            q[i] = '0'+q[i]
    t = q[0]+'/'+q[1]+'/'+q[2]+' '+b[1]
    return t


def func4(s):
    b = s.split(' ')
    q = b[1].split(':')
    t = b[0]+' '+q[0]
    return t


c = pd.Series(consumption['DealTime'].apply(func3))
a = pd.Series(c.apply(func1))
a.rename('DealDate', inplace=True)
b = pd.Series(a.apply(func2))
b.rename('DealMon', inplace=True)
d = consumption.drop('DealTime', axis=1)
e = pd.Series(c.apply(func4))
e.rename('DealHour', inplace=True)
temp = pd.concat([c, e, a, b, d], axis=1)
# print(temp)

# 消费时间异常
print('---消费时间异常---')
f = pd.Series(temp['DealHour'].apply(lambda x: x.split(' ')[1]))
for i in f.index:
    b = int(f[i])
    if b < 6 or b > 19:
        print(i, f[i], '时')

t1 = temp[['PerSex', 'DealDate', 'MonDeal', 'DealMon']]
csp_mon = t1.groupby(['PerSex', 'DealMon', 'DealDate']).sum()
print('\n-----按天统计男女消费情况-----')
print(csp_mon)

t2 = temp[['DealHour', 'DealDate', 'DealMon', 'PerSex', 'MonDeal']]
csp_hour = t2.groupby(['PerSex', 'DealMon', 'DealDate', 'DealHour']).sum()
print('\n-----按时间段（每小时）统计男女消费情况-----')
print(csp_hour)




