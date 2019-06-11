# coding:utf-8

'''
#Author: chenhao
#date: June, 11 2019
'''

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm


###########################################################################################
# Part3: 采用ARIMA和ARMA进行时序预测，输入为1995年至2013年设备数量以及健身路径长度，预测2014年至2020年七年间的数据
###########################################################################################
# 导入数据
path = './'
data_origin = pd.read_csv(path + 'History.csv', encoding='gb2312')
data_pre = pd.read_csv(path + 'History_Pre.csv', encoding='gb2312')

# 用来正常显示中文标签
# plt.rcParams['font.sans-serif'] = ['FangSong']

# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# 画出设备数量和运动路径的长度
plt.title('Test-Score ARIMA')
plt.ylabel('Score')
plt.xlabel('Test')
x = range(len(data_origin['Year']))
y1 = data_origin['Score']
y2 = data_origin['Rank']
x1 = data_pre['Year']

plt.plot(x, y1, label='Score')
# plt.plot(x1, y2, label='Rank')
#plt.plot(x, y2, label='Path')
plt.xticks(x1, data_origin['Year'], rotation=45)
plt.show()

# 做出设备数量的自相关图
plot_acf(y1)
plt.show()

# 平稳性检测
print(u'原始序列的ADF检验结果为：', ADF(y1))
# 返回值依次为adf、pvalue、nobs、critical values、icbest、regresult、resstore
# adf:-0.0
# pvalue: 0.95853208606005602
# nobs: 8
# critical values: 10
# icbest: {'1%': -4.3315729999999997, '5%': -3.2329500000000002, '10%': -2.7486999999999999}
# resstore: -414.96637673426136

# 对数据进行差分
D_data = y1.diff(1).dropna()
D_data.columns = [u'数目差分']
D_data.plot()
plt.show()

# 做出设备数量差分的自相关图
plot_acf(D_data)
plt.show()

# 做出设备数量差分的偏自相关图
plot_pacf(D_data)
plt.show()

# 设备数量差分平稳性检测
print(u'差分序列的ADF检验结果为：', ADF(D_data))
# 返回值依次为adf、pvalue、nobs、critical values、icbest、regresult、resstore
# adf:-3.8202312222795336
# pvalue: 0.0027069749201551079
# nobs: 7
# critical values: 10
# icbest: {'1%': -4.3315729999999997, '5%': -3.2329500000000002, '10%': -2.7486999999999999}
# resstore: -424.34713555026133

# 白噪声检验，返回统计量和p值
print(u'差分序列的白噪声检验结果为：', acorr_ljungbox(D_data, lags=1))
# 统计量为4.52828986
# p值为0.03333892


# 定阶
# 一般阶数不超过length/10
D_data = y1.diff(1).dropna()
D_data.columns = [u'数目差分']
pmax = int(len(D_data)/10)
qmax = int(len(D_data)/10)

data_sub = data_origin['Score'].astype(float)
data_sub = pd.Series(data_sub)
data_sub.index = pd.Index(sm.tsa.datetools.dates_from_range('1', '24'))
print('data_sub:')
print(data_sub)

# 定义bic矩阵
bic_matrix = []
for p in range(pmax+1):
    tmp = []
    for q in range(qmax+1):
        tmp.append(ARIMA(data_sub, (p, 1, q)).fit().bic)

        # try:   #存在部分报错，所以用try来跳过报错
        #     tmp.append(ARIMA(data_sub, (p, 1, q)).fit().bic)
        # except:
        #     tmp.append(None)
    bic_matrix.append(tmp)

# 从中可以找出最小值
bic_matrix = pd.DataFrame(bic_matrix)
print(bic_matrix)
print(bic_matrix.stack())
'''
# 先用stack展平，然后用idxmin找出最小值位置
p, q = bic_matrix.stack().idxmin()
print(u'BIC最小的p值和q值为：%s、%s' %(p, q))

model = ARIMA(data_sub, (1, 1, 0)).fit(disp=0)
output = model.forecast(3)
print(output)
# 预测出来的结果为

'''