#-*- coding:utf-8 -*-

'''
# Author: chenhao
# Date: March. 10
# Description: Data-process for Education visualization competition
'''

##############################################################################
#Part1：统计学校范围内学生的基本情况
##############################################################################

import pandas as pd

# 导入数据集
data_origin = pd.read_csv('../../education_data/2_student_info.csv')
# print(data_origin)

##############################################################################
# 性别

# 统计学生性别的缺失值
num_null = len(data_origin['bf_sex'][pd.isnull(data_origin['bf_sex'])])
print(num_null)
# 缺失值数量为0

# 统计学生的总人数
num_all = len(data_origin['bf_sex'])
print(num_all)
# 总人数为1765

# 统计男女生的人数
data_origin['bf_sex'] = data_origin['bf_sex'].map({'男': 1, '女': 0})
num_male = sum(data_origin['bf_sex'])
num_female = num_all - num_male
print(num_male, num_female)
# 男性人数为943人，女性人数为822人

##############################################################################
# 民族

# 统计学生民族数据的缺失值
nation_null = len(data_origin['bf_nation'][pd.isnull(data_origin['bf_nation'])])
print(nation_null)
# 缺失值数量为0

# 了解一共有几种民族
# 直接使用Excel进行统计得到：汉族1750人，少数民族15人（回族2人，满族4人，苗族3人，畲族1人，土家族3人，朝鲜族2人）
# 该部分建议使用饼状图反映，点击可展示具体少数民族人数

##############################################################################
# 出生地分布

# Step1：统计缺失值并剔除
NativePlace_null = len(data_origin['bf_NativePlace'][pd.isnull(data_origin['bf_NativePlace'])])
print(NativePlace_null)
# 出生地缺失的数据有125人

# 将学生出生地缺失的行删除
data_NativePlace = data_origin.drop(data_origin[data_origin['bf_NativePlace'].isnull()].index)
print(data_NativePlace.shape[0])
# 剩下的行数为1640行

# 将学生出生地中错误数据进行删除，如汉、汉族、中国
data_NativePlace = data_NativePlace.drop(data_NativePlace[data_NativePlace['bf_NativePlace'] == '汉族'].index)
data_NativePlace = data_NativePlace.drop(data_NativePlace[data_NativePlace['bf_NativePlace'] == '汉'].index)
print(data_NativePlace.shape[0])
# 剩下的行数为1610行

# Step2:删除构建主要省级城市
# 构建主要的省级城市  34个
Province = ["北京", "上海", "天津", "重庆", "河北", "山西", "辽宁", "吉林", "河南", "江苏", "浙江", "安徽", "福建",
            "江西", "山东", "湖北", "湖南", "广东", "海南", "四川", "贵州", "云南", "陕西", "甘肃", "青海", "黑龙江",
            "内蒙古", "广西", "西藏", "宁夏", "新疆", "台湾", "香港", "澳门"]

# 通过循环来统计数目
num_city = [0]*34
for i in range(0, 34):
    data_NativePlace_new = data_NativePlace.drop(data_NativePlace[data_NativePlace['bf_NativePlace'].str.contains(Province[i])].index)
    num_city[i] = data_NativePlace.shape[0] - data_NativePlace_new.shape[0]
    print("城市", Province[i], "的数量为", num_city[i])

# 通过循环来去除主要省市
for j in range(0, 34):
    data_NativePlace = data_NativePlace.drop(data_NativePlace[data_NativePlace['bf_NativePlace'].str.contains(Province[j])].index)
# print(data_NativePlace)

# 删除只有中国的行
data_NativePlace = data_NativePlace.drop(data_NativePlace[data_NativePlace['bf_NativePlace'] == '中国'].index)

print(data_NativePlace.shape[0])
# 处理浙江的城市

Zhejiang = ["宁波", "慈溪", "岱山", "东阳", "奉化", "富阳", "海曙", "杭州", "黄岩", "嘉善", "嘉兴", "建德", "江北", "乐清",
            "宁海", "浦江", "衢州", "三门", "上虞", "绍兴", "嵊州", "台州", "桐庐", "温州", "咸祥", "象山", "新昌", "义乌",
            "鄞州", "余姚", "浙甬", "舟山", "诸暨", "丽水"]

sum_zhejiang = 0
num_zhejiang = [0]*(len(Zhejiang))
for i in range(0, len(Zhejiang)):
    data_NativePlace_new = data_NativePlace.drop(data_NativePlace[data_NativePlace['bf_NativePlace'].str.contains(Zhejiang[i])].index)
    num_zhejiang[i] = data_NativePlace.shape[0] - data_NativePlace_new.shape[0]
    data_NativePlace = data_NativePlace.drop(data_NativePlace[data_NativePlace['bf_NativePlace'].str.contains(Zhejiang[i])].index)
print(num_zhejiang)

for i in range(0, len(Zhejiang)):
    sum_zhejiang += num_zhejiang[i]

num_city[10] = num_city[10] + sum_zhejiang
print("属于浙江的其他的城市有", sum_zhejiang, "个")
print("属于浙江省一共有", num_city[10], "名学生")

# 修改其他的省市
# 打印剩余的
print(data_NativePlace)

# 将其他的并入
# 安徽合肥、皖
num_city[11] = num_city[11] + 2
# 江西吉安
num_city[13] = num_city[13] + 1
# 辽宁鞍山
num_city[6] = num_city[6] + 1

# 打印各个省市的分布情况
for i in range(0, len(Province)):
    print("来自", Province[i], "的有", num_city[i], "位学生")

# 打印各个省市有人的分布情况
for i in range(0, len(Province)):
    if num_city[i] != 0:
        print("来自", Province[i], "的有", num_city[i], "位学生")

##############################################################################
# 学生政治面貌统计

# 统计学生政治面貌的缺失值
num_policy_null = len(data_origin['bf_policy'][pd.isnull(data_origin['bf_policy'])])
print(num_policy_null)
# 缺失值数量为0

# 统计学校内学生的政治面貌，分为：共青团员，少先队员，一般

policy = ["共产党党员", "共青团员", "少先队员", "一般", "民主党派"]
num_policy = [0]*5

for i in range(5):
    data_policy_new = data_origin.drop(data_origin[data_origin['bf_policy'].str.contains(policy[i])].index)
    num_policy[i] = data_origin.shape[0] - data_policy_new.shape[0]
print(num_policy)

# 共产党党员1人，共青团员1662人，少先队员23人，一般为78人，民主党派1人

