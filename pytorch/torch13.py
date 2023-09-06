# 라이브러리 호출 및 데이터 준비
from sklearn.datasets import load_digits
digits = load_digits()

print("Image Data Shape", digits.data.shape)

print("Label Data Shape", digits.target.shape)


# digits 데이터셋의 시각화
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 4))
for index, (image, label) in enumerate(zip(digits.data[0:5], digits.target[0:5])):
    plt.subplot(1, 5, index + 1)
    plt.imshow(np.reshape(image, (8, 8)), cmap=plt.cm.gray)
    plt.title('Training : %i/n' % label, fontsize = 20)
# plt.show()


# 훈련과 테스트 데이터셋 분리 및 로지스틱 회귀 모델 생성
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(digits.data,
                                                    digits.target,
                                                    test_size=0.25,
                                                    random_state=0)
from sklearn.linear_model import LogisticRegression
logisticRegr = LogisticRegression()
logisticRegr.fit(x_train, y_train)


# 일부 데이터를 사용한 모델 예측
# print(logisticRegr.predict(x_test[0].reshape(1, -1)))
logisticRegr.predict(x_test[0].reshape(1, -1))
# print(logisticRegr.predict(x_test[0:10]))
logisticRegr.predict(x_test[0:10])


# 전체 데이터를 사용한 모델 얘측

# sklearn의 metrics를 이용한 코드
from sklearn import metrics
predictions = logisticRegr.predict(x_test)
print(metrics.accuracy_score(y_test, predictions))

# sklearn의 metrics를 이용하지 않은 코드
score = logisticRegr.score(x_test, y_test)
print(score)


import numpy as np
import seaborn as sns
from sklearn import metrics

cm = metrics.confusion_matrix(y_test, predictions)
plt.figure(figsize=(9, 9))
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square=True, cmap="Blues_r")
plt.ylabel("Actual label")
plt.xlabel("Predicted label")
all_sample_title = "Accurary Score : {0}".format(score)
plt.title(all_sample_title, size = 15)
plt.show()