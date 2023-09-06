# 라이브러리 호출
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


# weather.csv 불러오기
dataset = pd.read_csv("pytorch/data/weather.csv")


# 데이터 간 관계를 시각화로 표현
# dataset.plot(x='MinTemp', y='MaxTemp', style='o')
# plt.title('MinTemp vs MaxTemp')
# plt.xlabel('MinTemp')
# plt.ylabel('MaxTemp')
# plt.show()


# 데이터를 독립 변수와 종속 변수로 분리하고 선형 회귀 모델 생성
x = dataset['MinTemp'].values.reshape(-1, 1)
y = dataset['MaxTemp'].values.reshape(-1, 1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
regressor = LinearRegression()
regressor.fit(x_train, y_train)


# 회귀 모델에 대한 예측
y_pred = regressor.predict(x_test)
df = pd.DataFrame({'Actual' : y_test.flatten(), 'Predicted' : y_pred.flatten()})
print(df)


# 테스트 데이터셋을 사용한 회귀선 표현
# 그래프를 그리면 그 시점에서 코드가 멈추기 때문에 주석 처리
# plt.scatter(x_test, y_test, color='green')
# plt.plot(x_test, y_pred, color='blue', linewidth=2)
# plt.show()


# 선형 회귀 모델 평가
print(f"평균제곱법 : {metrics.mean_squared_error(y_test, y_pred)}")
print(f"루트 평균제곱법 : {np.sqrt(metrics.mean_squared_error(y_test, y_pred))}")