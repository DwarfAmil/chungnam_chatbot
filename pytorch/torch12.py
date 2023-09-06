# 라이브러리 호출 및 데이터 준비
import pandas as pd
df = pd.read_csv("pytorch/data/titanic/train.csv", index_col="PassengerId")
print(df.head())

# 데이터 전처리
df = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Survived']]
df['Sex'] = df['Sex'].map({'male' : 0, 'female' : 1})
df = df.dropna()
X = df.drop('Survived', axis=1)
y = df['Survived']


# 훈련과 테스트 데이터셋으로 분리
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


# 결정 트리 모델 생성
from sklearn import tree
model = tree.DecisionTreeClassifier()


# 모델 훈련
model.fit(X_train, y_train)


# 모델 예측
y_predict = model.predict(X_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_predict)


# 혼동 행렬을 이용한 성능 측정
from sklearn.metrics import confusion_matrix
print(pd.DataFrame(
    confusion_matrix(y_test, y_predict),
    columns=['Predicted Not Survival', 'Predicted Survival'],
    index=['Ture Not Survival', 'True Survival']
))