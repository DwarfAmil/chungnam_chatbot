# 라이브러리 호출
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA


# 데이터 불러오기
x = pd.read_csv('pytorch/data/credit_card.csv')
x = x.drop('CUST_ID', axis=1)
x.fillna(method='ffill', inplace=True)
print(x.head())


# 데이터 전처리 및 데이터를 2차원으로 차원 축소
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_nomalized = normalize(x_scaled)
x_nomalized = pd.DataFrame(x_nomalized)

pca = PCA(n_components=2)
x_principal = pca.fit_transform(x_nomalized)
x_principal = pd.DataFrame(x_principal)
x_principal.columns = ['P1', 'P2']
print(x_principal.head())


# DBSCAN 모델 생성 및 결과의 시각화
db_default = DBSCAN(eps=0.0375, min_samples=3).fit(x_principal)
labels = db_default.labels_

# colours = {}
# colours[0] = 'y'
# colours[1] = 'g'
# colours[2] = 'b'
# colours[-1] = 'k'
colours = {0 : 'y', 1 : 'g', 2 : 'b', -1 : 'k'}

cvec = [colours[label] for label in labels]

r = plt.scatter(x_principal['P1'], x_principal['P2'], color='y')
g = plt.scatter(x_principal['P1'], x_principal['P2'], color='g')
b = plt.scatter(x_principal['P1'], x_principal['P2'], color='b')
k = plt.scatter(x_principal['P1'], x_principal['P2'], color='k')

plt.figure(figsize=(9, 9))
plt.scatter(x_principal['P1'], x_principal['P2'], c=cvec)

plt.legend((r, g, b, k), ('Label 0', 'Label 1', 'Label 2', 'Label -1'))
plt.show()


# 모델 튜닝
db = DBSCAN(eps=0.0375, min_samples=50).fit(x_principal)
labels1 = db.labels_

colours1 = {0 : 'r', 1 : 'g', 2 : 'b', 3 : 'c', 4 : 'm', 5 : 'y', -1 : 'k'}

cvec = [colours1[label] for label in labels1]
colors1 = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
# colors1 = list("rgbcymk")

scatter_li = []
for c in colors1:
    scatter_li.append(plt.scatter(x_principal['P1'],
                                  x_principal['P2'],
                                  marker='o',
                                  color=c))
# r = plt.scatter(
#     x_principal['P1'], x_principal['P2'], marker='o', color=colors1[0])
# g = plt.scatter(
#     x_principal['P1'], x_principal['P2'], marker='o', color=colors1[1])
# b = plt.scatter(
#     x_principal['P1'], x_principal['P2'], marker='o', color=colors1[2])
# c = plt.scatter(
#     x_principal['P1'], x_principal['P2'], marker='o', color=colors1[3])
# m = plt.scatter(
#     x_principal['P1'], x_principal['P2'], marker='o', color=colors1[4])
# y = plt.scatter(
#     x_principal['P1'], x_principal['P2'], marker='o', color=colors1[5])
# k = plt.scatter(
#     x_principal['P1'], x_principal['P2'], marker='o', color=colors1[-1])

plt.figure(figsize=(9, 9))
plt.scatter(x_principal['P1'], x_principal['P2'], c=cvec)
plt.legend([sc for sc in scatter_li],
           ('Label 0', 'Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5', 'Label -1'),
           scatterpoints=1,
           loc='upper left',
           ncol=3,
           fontsize=8)
# plt.legend((r, g, b, c, m, y, k),
#            ('Label 0', 'Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5', 'Label -1'),
#            scatterpoints=1,
#            loc='upper left',
#            ncol=3,
#            fontsize=8)
plt.show()


# min_samples를 50에서 100으로 변경
db = DBSCAN(eps=0.0375, min_samples=100).fit(x_principal)
labels2 = db.labels_

colours2 = {0 : 'r', 1 : 'g', 2 : 'b', 3 : 'c', 4 : 'm', 5 : 'y', -1 : 'k'}

cvec = [colours2[label] for label in labels2]
colors2 = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
# colors2 = list("rgbcymk")

scatter_li1 = []
for c in colors2:
    scatter_li1.append(plt.scatter(x_principal['P1'],
                                  x_principal['P2'],
                                  marker='o',
                                  color=c))

# r = plt.scatter(
#     x_principal['P1'], x_principal['P2'], marker='o', color=colors2[0])
# g = plt.scatter(
#     x_principal['P1'], x_principal['P2'], marker='o', color=colors2[1])
# b = plt.scatter(
#     x_principal['P1'], x_principal['P2'], marker='o', color=colors2[2])
# c = plt.scatter(
#     x_principal['P1'], x_principal['P2'], marker='o', color=colors2[3])
# m = plt.scatter(
#     x_principal['P1'], x_principal['P2'], marker='o', color=colors2[4])
# y = plt.scatter(
#     x_principal['P1'], x_principal['P2'], marker='o', color=colors2[5])
# k = plt.scatter(
#     x_principal['P1'], x_principal['P2'], marker='o', color=colors2[-1])

plt.figure(figsize=(9, 9))
plt.scatter(x_principal['P1'], x_principal['P2'], c=cvec)
plt.legend([sc for sc in scatter_li1],
           ('Label 0', 'Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5', 'Label -1'),
           scatterpoints=1,
           loc='upper left',
           ncol=3,
           fontsize=8)
# plt.legend((r, g, b, c, m, y, k),
#            ('Label 0', 'Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5', 'Label -1'),
#            scatterpoints=1,
#            loc='upper left',
#            ncol=3,
#            fontsize=8)
plt.show()