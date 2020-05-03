# -*-coding:utf-8-*-

import pandas as pd
import numpy as np
from math import e
from scipy.stats import entropy
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 1000)


# 定义影响因素
# 成本型：地区生产总值GDP——G（亿元）、单位GDP耗电量——C（(kW·h)/元)、火力发电占比——S（%）、火力发电标准煤耗量H（g/(kW·h)）、发电量P（TW·h）、网损占比L（%）
# 效益型：自发电量占自用电量比例M（%）、历史碳排放量E_（万t）


N_region, N_factor = 5, 8  # 地区数、指标数
D = pd.read_excel(r'OriginalData.xlsx')
print('5个地区个指标值：')
print(D)


# 主观赋权法
cpr = pd.read_excel(r'OriginalData.xlsx', sheet_name='Comparison').loc[0, :].tolist()
print('7个重要度对比值：')
print(cpr)
roumat = np.ones((N_factor, N_factor))


# 定义计算判断矩阵元素ρ的函数
def calrou():
    [rows, cols] = roumat.shape
    for i in range(rows):
        for j in range(cols):
            if i < j:
                roumat[i, j] = np.prod(cpr[i: j])
            if i > j:
                roumat[i, j] = np.prod(cpr[j: i])
            if i == j:
                roumat[i, j] = 1


calrou()
print('判断矩阵ρ：')
print(roumat)

# 计算计算主观权重值过程中开n次根的那个中间值
Prod = [0] * N_factor  # [0, 0, 0, 0, 0, 0, 0, 0]
Rootmid = [0] * N_factor
def calmid():
    [rows, cols] = roumat.shape
    for i in range(cols):
        Prod[i] = np.prod(roumat[i, :])
        Rootmid[i] = pow(Prod[i], 1/N_factor)


calmid()

SumRoot = np.sum(Rootmid)
ws = [0] * N_factor  # 初始化8个指标的主观权重
for i in range(N_factor):
    ws[i] = Rootmid[i] / SumRoot
print('主观权重：')
print(ws)  # 每个指标的主观权重值


# 客观赋权法

# 效益型指标归一化函数
def normxy(df):
    dfnorm = df.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
    return dfnorm

# 成本型指标归一化函数
def normcb(df):
    dfnorm = df.apply(lambda x: (np.max(x) - x) / (np.max(x) - np.min(x)))
    return dfnorm


Dxy = D[['E_', 'M']]  # 取效益型指标所在列
Dcb = D.drop(['Region', 'E_', 'M'], axis=1)  # 取成本型指标所在列

Dxynorm = normxy(Dxy)
Dcbnorm = normcb(Dcb)

# 合并归一化后的指标
Dnorm = pd.concat([Dxynorm.iloc[:, 0], Dcbnorm.iloc[:, 0], Dcbnorm.iloc[:, 1], Dcbnorm.iloc[:, 2], Dcbnorm.iloc[:, 3], Dxynorm.iloc[:, 1], Dcbnorm.iloc[:, 4], Dcbnorm.iloc[:, 5]], axis=1)
print('归一化后的原始数据r：')
print(Dnorm)

# 标准化成Dnorm_，对应文中公式9下方的yij
DnormSum = Dnorm.sum(axis=0)
Dnorm_ = Dnorm.div(DnormSum, axis='columns')
print('归一化后的原始数据y：')
print(Dnorm_)


# 求信息熵
Dnorm_L = [0] * N_factor
E_en = [0] * N_factor
for i in range(N_factor):
    Dnorm_L[i] = Dnorm_.iloc[:, i].values.tolist()
print('Dnorm_L：')
print(Dnorm_L)
for i in range(N_factor):
    E_en[i] = entropy(Dnorm_L[i], base=e) / np.log(N_region)  # 即公式9的dj

print('E_en：')
print(E_en)

E_enSum = np.sum(E_en)  # dk求和
E_en2 = [x*2 for x in E_en]
mid2 = E_enSum + 1 - E_en2


# 计算客观权重wo
wo = mid2 / np.sum(mid2)
print('客观权重：')
print(wo)


# 自定义偏好系数δ
δ = 0.5
# 求综合权重
wsL = [x*δ for x in ws]
# print(wsL)
woL = [x*(1-δ) for x in wo]
# print(woL)
wcom = np.sum([wsL, woL], axis=0)
print('综合权重：')
print(wcom)
