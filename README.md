# chungnam_chatbot

충남인력개발원 챗봇과정에서 교육받는 동안 사용하는 레포지토리 입니다.

***
<details>
<summary><h2>23.09.04</h2></summary>

***
* torch1 ~ torch6
***
* python class
    * 생성자 (constructor)
        * class의 이름과 같은 이름으로 된 함수 class를 생성할때 실행되는 함수
    * 상속 (inheritance)
        * 부모 클래스의 내용을 자식 클래스가 물려받는 것
    * 오버라이딩 (overriding)
        * 부모 클래스의 메소드를 자식 클래스에서 재정의 하는 것
    * 스페셜 메소드 (special method)
        * 파이썬의 객체들이 동일하게 가지는 인터페이스
* 데이터
    * 스칼라 (scala)
        * 하나의 숫자를 의미
    * 벡터 (vector)
        * 벡터는 숫자(스칼라)의 배열
    * 행렬 (Matrix)
        * 2차원의 배열
    * 텐서 (tensor)
        * 3차원 또는 그 이상의 배열
* torch
* pandas
* torchvision

***
</details>

<details>
<summary><h2>23.09.05</h2></summary>

***
* torch7 ~ torch9
***
* pytorch code
    * 데이터셋 분포
    * 데이터셋 변환
    * 데이터셋 분리
    * 모델 클래스 객체 생성
    * CPU/GPU 사용 지정
    * 모델 학습
    * 모델 예측
    * 모델 정확도 확인
* 지도 학습
    * 분류와 회귀의 차이
        * 분류
            * 데이터 유형 : 이산형 데이터
            * 결과 : 훈련 데이터의 레이블 중 하나를 예측
            * 예시 : 학습 데이터를 A / B / C 그룹 중 하나로 매핑 ***ex) 스팸 메일 필터링***
        * 회귀
            * 데이터 유형 : 연속형 데이터
            * 결과 : 연속된 값을 예측
            * 예시 : 결괏값이 어떤 값이든 나올 수 있음 ***ex) 주가 분석 예측***
    * 분류 학습 모델
        * **`K - 최근접 이웃 (K-Nearest Neighbor)`**
            * 왜 사용할까?
                * 주어진 데이터에 대한 분류
            * 언제 사용하면 좋을까?
                * K - 최근접 이웃은 직관적이며 사용하기 쉽기 때문에 초보자가 사용하기 좋습니다.
                * 훈련 데이터를 충분히 확보할 수 있는 환경에서 사용하면 좋습니다.
* matplotlib
* sklearn
* seaborn

***
</details>

<details>
<summary><h2>23.09.06</h2></summary>

***
* torch9 ~ torch16
***

<details>
<summary><h3>지도 학습</h3></summary>

---

<details>
<summary><h3>서포트 벡터 머신 (Support Vector Machine, SVM)</h3></summary>

* 왜 사용할까?
    * 주어진 데이터에 대한 분류
* 언제 사용하면 좋을까?
    * 서포트 벡터 머신은 커널만 적절히 선택한다면정확도가 상당히 좋기 때문에 정확도를 요구하는 분류 문제를 다룰 때 사용하면 좋습니다.
    * 텍스트를 분류할 때도 많이 사용됩니다.
* 분류 지원
    * 서포트 벡터 머신은 **선형 분류**와 **비선형 분류**를 지원
    * 선형으로 분류될 수 없는 데이터들에 의해서 발생
* `서포트 벡터 머신`
    * 분류되지 않은 새로운 데이터가 나타나면 결정 결계를 기분으로 경계의 어느 쪽에 속하는지 분류하는 모델
* `서포트 벡터`
    * 결정 경계와 가까이 있는 데이터들을 의미
* `결정 경계`
    * 데이터를 분류하기 위한 기준선
    * 결정 경계는 데이터가 분류된 클래스에서 최대한 멀리 떨어져 있을 때 성능이 가장 좋다.
* `마진`
    * 결정 경계와 서포트 벡터 사이의 거리를 의미
    * `하드 마진`
        * 이상치를 허용하지 않음
    * `소프트 마진`
        * 어느 정도의 이상치들이 마진 안에 포함되는 것을 허용
* `커널 트릭`
    * 비선형 문제를 해결하는 가장 기본적인 방법은 저차원 데이터를 고차원으로 보내는 것인데, 이것은 많은 수학적 계산이 필요하기에 성능에 문제를 줄 수 있어, 그 문제를 해결하고자 도입한 것이 **커널 트릭**이다.
    * **선형모델을 휘한 커널**
        * `선형 커널`
            * 선형으로 분류 가능한 데이터에 적용
            * 선형 커널은 기본 커널 트릭이며, 커널 트릭을 사용하지 않겠다는 의미와 일맥상통함
            $$K(a, b) = a^T b$$
            $$(a, b : \text{입력 벡터})$$
    * **비선형을 위한 커널**
        * `다항식 커널`
            * 실제로는 특성을 추가하지 않지만, 다항식 특성을 많이 추가한 것과 같은 결과를 얻을 수 있는 방법
            * 실제로는 특성을 추가하지 않지만, 엄청난 수의 특성 조합이 생기는 것과 같은 효과를 얻기 때문에 고차원으로 데이터 매핑이 가능
            $$K(a, b) = (\gamma a^T \cdot b)^d$$
            $$a, b : \text{입력 벡터}$$
            $$\gamma : \text{감마}$$
            $$d : \text{차원, 이때 } \gamma d \text{는 하이퍼파라미터}$$

        * `가우시안 RBF 커널`
            * 입력 벡터를 차원이 무한한 고차원으로 매핑하는 것으로, 모든 차수에 모든 다항식을 고려
            * 다항식 커널은 차수에 한계가 있지만 가우시안 RBF는 차수에 제한 없이 무한한 확장이 가능
            $$K(a, b) = \exp\left(-\gamma \cdot \|a - b\|^2\right)$$
            $$(\text{이때 } \gamma \text{는 하이퍼파라미터)}$$
</details>

<details>
<summary><h3>결정 트리 (decision tree)</h3></summary>

* 왜 사용할까?
    * 주어진 데이터에 대한 분류
* 언제 사용하면 좋을까?
    * 결정 트리는 이상치가 많은 값으로 구성된 데이터셋을 다룰 대 사용하면 좋습니다.
    * 결정 과정이 시각적으로 표현되기 때문에 머신 러닝이 어떤 방식으로 의사 결정을 하는지 알고 싶을 때 유용합니다.
* `결정 트리`
    * 데이터를 분휴하거나 결괏값을 예측하는 분석 방법
    * 트리 구조로 되어있기에 결정 트리라고 한다.
    * 결정트리는 데이터를 1차로 분류한 후 각 영역의 순도는 증가하고, 불순도와 불확실성은 감소하는 방향으로 학습을 진행한다.
* `정보 획득`
    * 순도가 증가하고 불확실성이 감소하는 것
* 순도 계산 방법
    * `엔트로피`
        * 확률 변수의 불확실성을 수치로 나타낸 것
        * 엔트로피가 높을수록 불확실성이 높다는 의미
        $$\text{Entropy}(A) = -\sum_{k=1}^{m} P_k \cdot \log_2(P_k)$$
        $$P_k = A : \text{영역에 속하는 데이터 가운데 }k\text{ 범주에 속하는 데이터 비율}$$
    * `지니 계수`
        * 불순도를 측정하는 지표로, 데이터의 통계적 분산 정도를 정량화해서 표현한 값
        * 지니 계수는 원소 n개 중에서 임의로 두개를 추출했을 때, 추출된 두 개가 서로 다른 그룹에 속해 있을 확률을 의미
        $$Gini(S) = 1 - \sum_{i=1}^{c} p_i^2$$
        $$S : \text{이미 발생한 사건의 모음}$$
        $$c : \text{사건 개수}$$
</details>

<details>
<summary><h3>회귀</h3></summary>

* `회귀`
    * 변수가 두 개 주어졌을 때 한 변수에서 다른 변수를 예측하거나 두 변수의 관계를 규명하는데 사용하는 방법
* 변수 유형
    * `독립 변수 (예측 변수)`
        * 영향을 미칠 것으로 예상되는 변수
    * `종속 변수 (기준 변수)`
        * 영향을 받을 것으로 예상되는 변수
    * 변수의 설정
        * 두 변수 간 관계에서 독립 변수와 종속 변수의 설정은 `논리적인 타당성`이 있어야 함  


<details>
<summary><h3>로지스틱 회귀</h3></summary>

* 왜 사용할까?
    * 주어진 데이터에 대한 분류
* 언제 사용하면 좋을까?
    * 로지스틱 회귀 분석은 주어진 데이터에 대한 확신이 없거나(예를 들어 분류 결과에 대해 확신이 없을 때) 향후 주기적으로 훈련 데이터셋을 수집하여 모델을 훈련시킬 수 있는 환경에서 사용하면 유용합니다.
* `로지스틱 회귀`
    * 분석하고자 하는 대상들이 두 집단 혹은 그 이상의 집단으로 나누어진 경우, 개별 관측치들이 어느 집단으로 분류될 수 있는지 분석하고 이를 예측하는 모형을 개발하는 데 사용되는 통계 기법입니다.  
<br>
<div align="center">

| 구분           | 일반적인 회귀 분석 | 로지스틱 회귀 분석 |
| -------------- | ------------------ | ------------------ |
| 종속 변수      | 연속형 변수        | 이산형 변수        |
| 모형 탐색 방법 | 최소제곱법         | 최대우도법         |
| 모형 검정      | F-테스트, t-테스트 | $X^2$ 테스트       |

</div>

* `분석 철차`
    * 각 집단에 속하는 확률의 추정치를 예측
        * 추정치는 이진 분류의 경우 집단 1에 속하는 확률 $P(Y=1)$로 구함
    * 분류 기준 값(cut-off)을 설정한 후 특정 범주로 분류함
        * $P(Y=1) \geq 0.5$ -> 집단 1로 분류
        * $P(Y=1) < 0.5$ -> 집단 0로 분류
</details>

<details>
<summary><h3>선형 회귀</h3></summary>

* 왜 사용할까?
    * 주어진 데이터에 대한 분류
* 언제 사용하면 좋을까?
    * 선형 회귀는 주어진 데이터에서 독립 변수(x)와 종속 변수(y)가 선형 관계를 가질 때 사용하면 유용합니다.
    * 복잡한 연산 과정이 없기 때문에 컴퓨팅 성능이 낮은 환경(CPU/GPU 혹은 메모리 성능이 좋지 않을 때)에서 사용하면 좋습니다.
* `선형 회귀`
    * 종속 변수와 독립 변수 사이의 관계를 설정하는데 사용됨
    * 독립 변수 x를 사용하여 종속 변수 y을 움직임을 예측하고 설명하는데 사용됨
        * 독립 변수 x는 하나일 수도 있고, x1, x2, x3처럼 여러 개일 수도 있다.
    * `단순 선형 회귀`
        * 하나의 x 값으로 y 값을 설명할 수 있다면 단순 선형 회귀라고 한다.
    * `다중 선형 회귀`
        * x 값이 여러 개라면 다중 선형 회귀라고 한다.
</details>
</details>
</details>

---

<details>
<summary><h3>비지도 학습</h3></summary>

---

* 비지도 학습
    * 비지도 학습은 레이블이 필요하지 않으며 정답이 없는 상태에서 훈련시키는 방식이다.
    * 비지도 학습에는 `군집`과 `차원 축소`가 있다.
* `군집`
    * 각 데이터의 유사성(거리)를 측정한 후 유사성이 높은(거리가 짧은) 데이터끼리 집단으로 분류하는 것
* `차원 축소`
    * 차원을 나타내는 특성을 줄여서 데이터를 줄이는 방식

<br>
<div align="center">

| 구분          | 군집                                                | 차원 축소                           |
| ------------- | --------------------------------------------------- | ----------------------------------- |
| 목표          | 데이터 그룹화                                       | 데이터 간소화                       |
| 주요 알고리즘 | K-평균 군집화(K-Means)                              | 주성분 분석(PCA)                    |
| 예시          | 사용자의 관심사에 따라<br>그룹화 하여 마케팅에 활용 | - 데이터 압축<br>- 중요한 속성 도출 |

</div>

---

<details>
<summary><h3>K-평균 군집화</h3></summary>

* 왜 사용할까?
    * 주어진 데이터에 대한 군집화
* 언제 사용하면 좋을까?
    * 주어진 데이터셋을 이용하여 몇 개의 클러스터를 구성할지 사전에 알 수 있을 때 사용하면 유용하다.
* `K-평균 군집화`
    * 데이터를 입력받아 소수의 그룹으로 묶는 알고리즘
* `학습 과정`
    * `중심점 선택`
        * 랜덤하게 초기 중심점을 선택
    * `클러스터 할당`
        * K개의 중심점과 각각의 개별 데이터 간의 거리를 측정한 후, 가장 가까운 중심점을 기준으로 데이터를 할당, 이 과정을 통해 클러스터가 구성
        * 클러스터링은 데이터를 하나 혹은 둘 이상의 덩어리로 묶는 과정
        * 클러스터는 덩어리 자체를 의미
    * `새로운 중심점 선택`
        * 클러스터마다 새로운 줌심점을 계산
    * `범위 확인`
        * 선택된 중심점에 더 이상의 변화가 없다면 진행을 멈춤
        * 만약 계속 변화가 있다면 클러스터 할당 후 새로운 중심점을 선택하는 과정을 반복
* `거리 제곱의 합`
    * $x, y$ 두 데이터의 차를 구해서 제곱한 값을 모두 더한 후 유사성을 측정하는데 사용됨
    * 가장 가까운 클러스터 중심까지 거리를 제곱한 값에 합을 구할 때 사용
    $$
    \text{SSD} = \sum_{i=1}^{n} (x_i - y_i)^2
    $$
    $$
    \left\{
    \begin{aligned}
    &n : \text{데이터 집합 내 데이터 포인트(요소)의 수를 나타냄} \\
    &x_i : \text{하나의 데이터 집합에서 i번째 요소 값을 나타냄} \\
    &y_i : \text{다른 데이터 집합에서 i번째 요소 값을 나타냄}
    \end{aligned}
    \right\}
    $$
    * $K$가 증가하면 거리 제곱의 합은 0이 되는 경향이 있음
        * $K$를 최댓값 $n$(여기에서 $n$은 샘플 수)으로 설정하면 각 샘플이 자체 클러스터를 형성하여 거리 제곱 합이 0과 같아지기 때문
</details>

<details>
<summary><h3>밀도 기반 군집 분석 (DBSCAN)</h3></summary>

* 왜 사용할까?
    * 주어진 데어터에 대한 군집화
* 언제 사용하면 좋을까?
    * K-평균 군집화와는 다르게 사전에 클러스터의 숫자를 알지 못할 때 사용하면 유용하다.
    * 주어진 데이터에 이상치가 많이 포함되었을 때 사용하면 좋다.
* `밀도 기반 군집 분석 (DBSCAN)`
    * 일정 밀도 이상을 가진 데이터를 기준으로 군집을 형성하는 방법
    * 노이즈에 영향을 받지 않고, K-평균 군집화에 비해 연산량은 많지만  K-평균 군집화가 잘 처리하지 못하는 오목하거나 볼록한 부분을 처리하는데 유용함
* 밀도 기반 군집 절차
    * `앱실론 내 점 개수 확인 및 중심점 결정` 
    * `군집 확장`
    * `1 ~ 2단계 반복`
    * `노이즈 정의`
</details>

<details>
<summary><h3>주성분 분석 (PCA)</h3></summary>

* 왜 사용할까?
    * 주어진 데이터의 간소화
* 언제 사용하면 좋을까?
    * 현재 데이터의 특성(변수)이 너무 많을 경우에는 데이터를 하나의 플롯(plot)에 시각화해서 살펴보는 것이 어렵다.
    * 특성 p개를 두세 개 정도로 압축해서 테이터를 시각화하여 살펴보고 싶을 때 유용한 알고리즘이다.
* `PCA (Principal Component Analysis)`
    * 고차원 데이터를 저차원(차원 축소) 데이터로 축소시키는 알고리즘
* 차원 축소 방법
    * `데이터들의 분포 특성을 잘 설명하는 벡터를 두 개 선택`
    * `벡터 두 개를 위한 적정한 가중치를 찾을 때까지 학습을 진행`
</details> 
</details>

<br>

* pandas
    * DataFrame
</details>

<details>
<summary><h2>23.09.07</h2></summary>

***
* torch17 ~ torch19
***
* **`딥러닝`**
    * 퍼셉트론
        * 인공 신경망에서 이용하는 구조(입력층, 출력층, 가중치로 구성된 구조)로 이루어진 선형 분류기
        * 다수의 신호(흐름이 있는)를 입력으로 받아 하나의 신호를 출력, 이 신호를 입력으로 받아 '흐른다/안 흐른다(1 or 0)'는 정보를 앞으로 전달하는 원리이다.
    <br>
    <div align="center">

    | 구분                                | 구성 요소                           | 설명                                                                                                            |
    | ----------------------------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------- |
    | 층                                  | 입력층 (input layer)                | 데이터를 받아들이는 층                                                                                          |
    | 층                                  | 은닉층 (hidden layer)               | 모든 입력 노드부터 입력 값을 받아 가중합을 계산하고,<br>이 값을 활성화 함수에 적용하여 출력층에 전달하는 층     |
    | 층                                  | 출력층 (output layer)               | 신경망의 최종 결괏값이 포함된 층                                                                                |
    | 가중치 (weight)                     | 가중치 (weight)                     | 노드와 노드 간 연결 강도                                                                                        |
    | 바이어스 (bias)                     | 바이어스 (bias)                     | 가중합에 더해 주는 상수로, 하나의 뉴런에서<br>활성화 함수를 거쳐 최종적으로 출력되는 값을<br>조절하는 역할을 함 |
    | 가중합 (weighted sum)<br>/ 전달함수 | 가중합 (weighted sum)<br>/ 전달함수 | 가중치와 신호의 곱을 합한 것                                                                                    |
    | 함수                                | 활성화 함수 (activation function)   | 신호를 입력받아 이를 적절히 처리하여 출력해 주는 함수                                                           |
    | 함수                                | 손실 함수 (loss function)           | 가중치 학습을 위해 출력 함수의 결과와 실제 값 간의 오차를 측정하는 함수                                         |

    </div>   

</details>

***

<details>
<summary><h2>23.09.11</h2></summary>

***
* torch19 ~ torch20
***
* **`전이 학습`**
    * `사전 훈련된 모델의 파라미터 학습 유무 지정`
        * 합성곱층을 사용하되 파라미터에 대해서는 학습을 하지 않도록 고정

        ```python
        def set_parameter_requires_grad(model, feature_extracting = True):
        if feature_extracting:
            for param in model.parameters():
                param.requires_grad = False

        set_parameter_requires_grad(resnet18)
        ```
        * 역전파 중 파라미터들에 대한 변화를 계산할 필요가 없음
        * 모델에 일부를 정하고 나머지를 학습하고자 할 때 requires_grad = False로 설정
            * 모델의 일부는 합성곱층(convolutional layer)가 풀링(pooling)층을 의미
* `텐서 함수 비교`
    <div align="center">

    | 구분                    | 메모리        | 계산 그래프 상주 유무       |
    | ----------------------- | ------------- | --------------------------- |
    | tensor.clone()          | 새롭게 할당   | 계산 그래프에 계속 상주     |
    | tensor.datach()         | 공유해서 사용 | 계산 그래프에 상주하지 않음 |
    | tensor.clone().detach() | 새롭게 할당   | 계산 그래프에 상주하지 않음 |

    </div>

* `add_subplot`
    * matplotlib 라이브러니에 있는 함수중 하나로 한 화면에 여러 개의 이미지를 담기 위해 사용
</details>

<details>
<summary><h2>23.09.12</h2></summary>

***
* torch21 ~ torch22
***

* **`os.path.join`**
    * 경로(패스)명 조작에 관한 처리를 모아둔 모듈로써 구현되어 있는 함수의 하나
    * 인수에 전달된 2개의 문자열을 결합하여, 1개의 경로로 할 수 있음
* **`transform class`**
    * 이미지의 데이터셋을 전처리 해주는 클래스
    ```py
    class ImageTransform():
        def __init__(self, resize, mean, std):
            self.data_transfrom = {
                "train" : transforms.Compose([
                    transforms.RandomResizedCrop(resize, scale=(0.5, 1.0)),
                    transforms.RandomHorizontalFlip(),
                    transforms.ToTensor(),
                    transforms.Normalize(mean, std)
                ]),
                "val" : transforms.Compose([
                    transforms.Resize(256),
                    transforms.CenterCrop(resize),
                    transforms.ToTensor(),
                    transforms.Normalize(mean, std)
                ])
            }
        
        def __call__(self, img, phase):
            return self.data_transfrom[phase](img)
    ```

* **`tqdm`**
    * 어떤 작업을 수행중 일 때 어디까지 실행되었고 얼마나 남았는지 등의 진행률을 확인할 때 사용
    * 반복문에서 프로세스바를 통해 진행률과 남은 시간을 알려주는 라이브러리 함수
* **`torch.summary`**
    * 텐서플로에 `model.summary()`와 같이 모델의 구조도 요약을 확인하는 기능을 구현한 라이브러리
    * 모델의 구조도에 대한 `요약`, `파라미터의 개수`, `메모리` 등 확인 가능

* **`합성곱 신경망`**
    * **`LeNet-5`**
        * 합성곱 신경망이라는 개념을 최초로 얀 르쿤이 개발한 구조
        * 합성곱과 다운 샘플링(혹은 풀링)을 반복적으로 거치면서 마지막에 완전연결층에서 분류를 수행

</details>

<details>
<summary><h2>23.09.13</h2></summary>

***
* flaskbook/apps/minimalapp
***

* **`파이썬 웹 프레임워크`**
    * **`장고 (django)`**
      * 특징
        * 파이썬 웹 프레임워크 중에서도 가장 유명함
        * 중규모 이상 웹을 구축시에 자주 사용
        * 개발에 필요한 많은 기능이 구현되어 있어 풀스택 프레임워크로 불림
        * Django REST Framework(DRF)를 추가 설치함으로서 웹 앱뿐만 아닌 REST API를 간단히 만들 수 있음
    * **`플라스크 (flask)`**
      * 특징
        * 마이크로 웹 프레임워크이다.
        * 데이터베이스 기능이 포함되어 있지 않는 등 최소한의 기능만 제공
        * 최소한의 규약만 있어 앱 구성 자유롭게 결정 가능
        * 데이터베이스 기능 등 확장 기능을 많이 지원
    * **`보틀 (bottle)`**
      * 특징
        * 웹 앱을 만들기 위한 프레임워크 중에는 가장 단순함
        * bottle.py라는 하나의 파일로만 구성되어있음
        * 파이썬 표준 라이브러리 이외에 의존 관계 없음
        * 마이크로 웹 프레임워크 중 하나로 플라스크보다 단순하고 빠르고 가벼움
    * **`FastAPI`**
      * 특징
        * 비동기 처리가 용이하도록 만들어진 파이썬 웹 프레임워크
        * 요청을 처리하는 속도 매우 빠름
    
    <br>
    <div align="center">

    | 프레임워크 | 공식 사이트                | 라이선스    | 초기 개발자                           | 최초 릴리스 | 템플릿 엔진                  | O/R 매퍼           |
    | ---------- | -------------------------- | ----------- | ------------------------------------- | ----------- | ---------------------------- | ------------------ |
    | 장고       | www.djangoproject.com      | BSD License | Adrian<br>Holovaty,<br>Simon Willison | 2005년      | Django<br>Template           | Django<br>O/R 매퍼 |
    | 플라스크   | palletsproject.com/p/flask | BSD License | Armin<br>Ronacher                     | 2010년      | Jinja2                       | 없음               |
    | 보틀       | bottlepy.org/docs/dev      | MIT License | Marcel<br>HEllkamp                    | 2009년      | Simple<br>Template<br>Engine | 없음               |
    | FastAPI    | fastapi.tiangolo.com       | MIT License | Sebastian<br>Ramirez                  | 2018년      | Jinja2                       | 없음               |
    </div>

* `데이터베이스 초기화 및 마이그레이션`
  * **`flask db init`**
    * 데이터베이스를 초기화하는 명령
    ```
    (venv) $ flask db init
    ```
    * 명령을 실행한 폴더 바로 아래 migraions 디렉터리가 생성됨
    * **`tip`**
      * migrations 디렉터리의 위치를 바꾸고 싶다면 -d 옵션을 통해 디렉터리를 지정
      ```
      (venv) $ flask db init -d apps/migrations
      ```
  * **`flask db migrate`**
    * 데이터베이스의 마이그레이션 파일을 생성하는 명령
    ```
    (venv) $ flask db migrate
    ```
    * 모델 정의를 바탕으로 migrations/versions 아래에 파이썬 파일로 데이터 베이스에 적용하기 전 정보가 생성됨
  * **`flask db upgrade`**
    * 마이그레이션 정보를 실제로 데이터베이스에 반영하기 위한 명령
    ```
    (venv) $ flask db upgrade
    ```
    * users 테이블이 생성됨
    
<br>
  
* python-dotenv
  * 환경 변수를 .env 파일로부터 읽어 들임
* email-validator
  * 이메일 주소 형식을 체크
* flask-debugtoolbar
  * 플라스크 앱 개발 보조 도구
* flask-mail
  * 이메일 송신
</details>

<details>
<summary><h2>23.09.14</h2></summary>

***
* flaskbook/apps/crud
***

* flask-sqlalchemy
  * 플라스크에서 SQLAlchemy를 이용하는 확장
* flask-migrate
  * 데이터베이스를 마이그레이트하는 확장
    * migrate - 옮기다 / 이동하다
* flask-wtf
  * 플라스크에서 `유효성 검증`이나 `CSRF`에 대처하기 위한 폼을 작성하는 확장

  <br>
  
  * **`유효성 검증`**
    * 구체적인 의도를 가진 사용(목적)을 위하여 특정 요구사항이 충족되었다는 객관적인 증거를 제공하고 실험에 의해 확인하는 과정
  * **`CSRF (Cross Site Request Forgery)`**
    * 웹 어플리케이션 취약점 중 하나로 인터넷 사용자(희생자)가 자신의 의지와는 무관하게 공격자가 의도한 행위(수정, 삭제, 등록 등)를 특정 웹사이트에 요청하게 만드는 공격
</details>

***
<details>
<summary><h2>23.09.18</h2></summary>

***
* flaskbook/apps/auth | flaskbook/apps/detector | flaskbook/app/static
***

* **`flask-login`**
   * Flask 프레임워크로 개발한 웹 어플리케이션의 로그인 기능을 쉽게 구현할 수 있도록 도와주는 라이브러리 
   * **`UserMixin`**
    <div align="center">
    
    | 프로퍼티/메서드  | 설명                                                                                    |
    | ---------------- | --------------------------------------------------------------------------------------- |
    | is_authenticated | 로그인 시는 true를 반환하고 미로그인시는 false를 반환하는 함수                          |
    | is_active        | 사용자 계정이 활성 상태일 때는 true를 반환하고 비활성 상태일 때는 false를 반환하는 함수 |
    | is_anonymous     | 로그인 사용자는 false를 반환하고 익명 사용자는 true를 반환하는 함수                     |
    | get_id           | 로그인 사용자의 유니크 ID를 취득하는 프로퍼티                                           |
    </div>

    * **`@login_required`**
      * 데코레이터를 붙이면 해당의 엔드포인트는 로그인하지 않으면 접근 불가 
    
    <br>

* **`SQLAlchemy`**
  * **`릴레이션십`**
  
    <div align="center">

    | 옵션명   | 설명                                                                                                                                |
    | -------- | ----------------------------------------------------------------------------------------------------------------------------------- |
    | backref  | 다른 모델에 대해서 양방향으로 릴레이션함                                                                                            |
    | lazy     | 관련한 객체를 지연하여 취득하는 옵션<br>디폰트는 select이며 다른 옵션에는 immediate, joined, subquery,<br>noload, dynamic 등이 있음 |
    | order_by | 정렬할 컬럼을 지정함                                                                                                                |
    </div>

</details>

<details>
<summary><h2>23.09.19</h2></summary>

***
* flaskbook/apps | flaskbook/apps/detector
***

* detector/index.html
```html
<div class="dt-image-username">{{ user_image.User.username }}</div>
<div class="dt-image-username">{{ user_image.UserImage.user_image_name }}</div>
```
위와 같이 데이터베이스 안에 있는 정보를 불러오려면 불러올 정보 앞에 클래스 이름을 붙어야 함

</details>

<details>
<summary><h2>23.09.20</h2></summary>

***
* torch23 ~ torch26
***

* **`시계열 분석`**
  * 독립 변수를 사용하여 종속 변수를 예측하는 일반적인 머신 러닝에서 시간을 독립 변수로 사용함
* **`ARIMA 모델 (AutoRegressive Integrated Moving Average)`**
  * 자기 회귀와 이동 평균을 둘 다 고려하는 모형
  * ARMA와 달리 과거 데이터의 선형 관계뿐만 아니라 추세까지 고려한 모델
  * `절차`
    * ARIMA() 함수 호출하여 사용, ARIMA(p, d, q) 함수에서 쓰는 파라미터는 다음과 같음
      * p: 자기 회귀 차수
      * d: 차분 차수
      * q: 이동 평균 차수
    * fit() 메서드 호출 모델에 데이터 적용 및 훈련
    * predict() 메서트 호출 미래 추세 및 동향 예측
<details>
<summary><h3>순환 신경망 (RNN | Recurrent Neural Network)</h3></summary>

* 시간적으로 연속성이 있는 데이터를 처리하려고 고안된 인공 신경망
  * RNN의 `Recurrent(반복되는)`는 이전 은닉층이 현재 은닉층의 입력이 되면서 `반복되는 순환 구조를 갖는다`는 의미
  * 기존 네트워크와의 차이점은 `기억(memory)`을 갖는다는 것이다.


* `RNN의 셀 유형`
  * `nn.RNNCell`
    *  SimpleRNN 계층에 대응되는 RNN 셀
  * `nn.GRUCell`
    * GRU 계층에 대응되는 GRU 셀
  * `nn.LSTMCell`
    * LSTM 계층에 대응되는 LSTM 셀


* `RNN 계산`
  * `은닉층 계산`
    * 계산을 위해 $x_t$와 $h_t-1$이 필요  
    즉, (이전 은닉측 * 은닉층 -> 은닉층 가중치 + 입력층 -> 은닉층 가중치 * (현재) 입력값)으로 계산 할 수 있으며,
    RNN에서 은닉층은 일반적으로 `하이퍼볼릭 탄젠트 활성화 함수`를 사용  


$$h_t = tanh(W_{hh} \cdot h_{t-1} + W_{hx} \cdot x_t)$$


  * `출력층 계산`
    * 심층 신경망과 계산 방법이 동일  
    즉, (은닉층 -> 출력층 가중치 * 현재 은닉층)에 `소프트맥스 함수`를 적용  


$$ŷₜ = softmax(W_{oh}h_t)$$


  * `오차 (E)`
    * 심층 신경망에서 전방향 학습과 달리 각 단계($t$)마다 오차를 측정  
    즉, 각 단계마다 실제 값($y_t$)과 예측 값($ŷₜ$)으로 오차(평균 제곱 오차 적용)를 이용하여 측정
  * `역전파`
    * `BPTT(BackPropagation Through Time)`를 이용하여 모든 단계마다 처음부터 끝까지 역전파함
      * 오차는 각 단계($t$)마다 오차를 측정하고 이전 단계로 전달, 이것을 `BPTT`라고 함 
    * 즉, 구한 오차를 이용하여 $W_{{x}h}, W_{{h}h}, W_{{h}y}$ 및 바이어스(bias)를 업데이트함  
    이때 BPTT는 오차가 멀리 전파될 때(왼쪽으로 전파) 계산량이 많아지고 `전파되는 양이 점차 적어지는 문제점(기울기 소멸 문제)`이 발생함  
    * 기울기 소멸 문제를 보안하기 위해 오차를 몇 단계까지만 전파시키는 `생략된-BPTT(truncated BPTT)`를 사용할 수도 있고, 근본적으로는 LSTM 및 GRU를 많이 사용
        계산량을 줄이기 위해 현재 단계에서 일정 시점까지만(보통 5단계 이전까지만) 오류를 역전파함, 이것을 `생략된-BPTT`라고 함
        
</details>
</details>

<details>
<summary><h2>23.09.22</h2></summary>

***
* torch26 ~ torch31
***

* **`LSTM`**
  * `순전파`
    * 기울기 소멸 문제를 해결하기 위해 망각, 입력, 출력 게이트라는 새로운 요소를 은닉층의 각 뉴런의 추가함
    * `망각 게이트`
      * 과거 정보를 어느 정도 기억할지 결정
      * 과거 정보와 현재 데이터를 입력받아 시그모이드를 취한 후 그 값을 과거 정보에 곱함
      * 시그모이드의 출력이 0이면 과거 정보를 버리고, 1이면 과거 정보는 온전히 보존
      $$f_t = σ(W_f * [h_{t-1}, x_t])$$
      $$c_t = f_t \cdot c_{t-1}$$
    * `입력 게이트`
      * 과거 정보와 현재 데이터를 입력받아 시그모이드와 하이퍼볼릭 탄젠트 함수를 기반으로 현재 정보에 대한 보존량을 결정
      * 현재 메모리에 새로운 정보를 반영할지 결정하는 역할을 함
      $$i_t = σ(W_i * [h_{t-1}, x_t])$$
      $$\tilde{c}_t = tanh(w_c[h_{t-1}, x_t])$$
      $$c_t = c_{t-1} + i_t * \tilde{c}_t$$
    * `셀`
      * 각 단계에 대한 은닉 노드(hidden node)를 메모리 셀이라 함
      * `총합(sum)`을 사용하여 셀 값을 반영, 이것으로 기울기 소면 문제 해결
      * `셀 업데이트`
        * 망각 게이트와 입력 게이트의 이전 단계 셀 정보를 계산, 현재 단계의 셀 상태를 업데이트
      $$i_t = σ(W_i * [h_{t-1}, x_t])$$
      $$c_t = c_{t-1} + i_t * \tilde{c}_t$$
    * `출력 게이트`
      * 과거 정보와 형재 데이터를 사용하여 뉴런의 출력을 결정
      * 이전 은닉 상태(hidden state)와 $t$번째 입력을 고려해서 다음 은닉 상태를 계산, 그리고 LSTM에서는 이 은닉 상태가 그 시점에서의 출력이 됨
      $$o_t = σ(W_o · [h_{t-1}, x_t])$$
      $$h_t = o_t * tanh(c_{t-1})$$
  * `역전파`
    * LSTM은 셀을 통해 역전파를 수행하기 때문에 `중단없는 기울기(uninterrupted gradient flow)`라고도 함
    * 최종 오차는 모든 노드에 전파, 이때 셀을 통해 중단 없이 전파
* **`GRU`**
  * LSTM에서 사용하는 망각 게이트와 입력 게이트를 하나로 합친 것
  * 별도의 업데이트 게이트로 구성
  * `망각 게이트`
    * 과거 정보를 적당히 초기화 시키려는 목적으로 시그모이드 함수를 출력으로 이옹, (0, 1) 값을 이전 은닉층에 곱함
    * 이전 시점의 은닉층 값에 현시점에 정보에 대한 가중치를 곱한 것
    $$r_t = σ(W_r * [h_{t-1},x_t])$$
  * `업데이트 게이트`
    * 과거와 현재 정보의 최신화 비율을 결정하는 역할
    * 시그모이드로 출력된 결과($z_t$)는 현시점의 정보량을 결정하고 1에서 뺀 값($1-z_t$)을 직전 시점의 은닉층 정보와 곱함
    $$z_t = σ(W_z * [h_{t-1},x_t])$$
  * `후보군`
    * 현시점의 정보에 대한 후보군을 계산
    * 과거 은닉층의 정보를 그대로 이용하지 않고 망각 게이트의 결과를 이용하여 후보군을 계산
    $$\tilde{h}_t = tanh(W * [r_t \* h_{t-1}, x_t])$$
  * `은닉층 계산`
    * 마지막으로 업데이트 게이트 결과와 후보군 결과를 결합하여 현시점의 은닉층을 계산
    * 시그모이드 함수의 결과는 현시점에서 결과에 대한 정보량을 결정, 1-시그모이드 함수의 결과는 과거의 정보량을 결정함
    $$h_t = (1 - z_t) * h_{t-1} + z_t * \tilde{h}_t$$
* **`양방향 RNN / 양방향 LSTM`**
  * 하나의 출력 값을 예측하는 데 메모리 셀 두 개를 사용
  * 첫 번째 메모리 셀은 이전 시점의 은닉 상태(forward state)를 전달받아 현재의 은닉 상태를 계산
  * 두 번째 메모리 셀은 다음 시점의 은닉 상태(backward state)를 전달받아 현재의 은닉 상태를 계산
  * 값 두 개를 모두 출력층에서 출력 값을 예측하는 데 사용

</details>

***

<details>
<summary><h2>23.09.25</h2></summary>

***
* torch31 ~ torch34
***

* **`성능 최적화`**
  * **`조기 종료를 이용한 성능 최적화`**
    * 조기 종료(early stopping)는 `뉴럴 네트워크가 과적합을 회피`하는 규제 기법
    * 훈련 데이터와 별도로 검증 데이터를 준비, 매 에포크마다 `검증 데이터에 대한 오차(validation loss)`를 측정하여 모델의 종료 시점 제어
    * 과적합이 발생하기 전까지 `학습에 대한 오차(training loss)`와 `검증에 대한 오차` `모두 감소`하지만, 과적합이 발생하면 `훈련 데이터셋에 대한 오차는 감소`하는 반면 `검증 데이터셋에 대한 오차는 증가`, 따라서 조기 종료는 `검증 데이터셋에 대한 오차가 증가하는 시점에서 학습을 종료`하도록 조정


* **`자연어 처리`**
  * 우리가 일상생활에서 사용하는 `언어 의미를 분석`하여 `컴퓨터가 처리`할 수 있도록 하는 과정
  * 인간 언어에 대한 이해도 필요하며, 언어 종류가 다르고 그 형태가 다양하기 때문에 처리가 매우 어렵다.
    * 영어는 명확한 띄어쓰기가 있지만, 중국어는 띄어쓰기가 없기에 단어 단위의 임베딩이 어려움
    
  * **`자연어 처리 용어`**
    * `말뭉치 (corpus(코퍼스))`
      * 자연어 처리에서 `모델을 학습시키기 위한 데이터`
      * 자연어 연구를 위해 `특정한 목적에서 표본을 추출한 집합`
    * `토큰 (token)`
      * 자연어 처리를 위한 문서는 작은 단위로 나누어야 하는데, 이때 `문서를 나누는 단위`가 토큰
      * 문자열을 토큰으로 나누는 작업을 `토큰 생성(tokenizing)`이라고 하며, 문자열을 토큰으로 분리하는 함수를 `토큰 생성 함수`라고 함
    * `토큰화 (tokenization)`
      * 텍스트를 문장이나 단어로 분리하는 것
      * 토큰화 단계를 마치면 텍스트가 `단어 단위로 분리`됨
    * `불용어 (stop words)`
      * 문장 내에서 많이 등장하는 단어
      * `분석과 관계없으며, 자주 등장하는 빈도` 때문에 `성능에 영향을 미치므로` 사전에 제거
        * 불용어 예로 `a`, `the`, `she`, `he` 등이 있음
    * `어간 추출 (stemming)`
      * 단어를 기본 형태로 만드는 작업
        * 예를 들어 `consign`, `consigned`, `consigning`, `consignment`가 있을 경우 기본 단어인 `consign`으로 통일하는 것
    * `품사 태깅 (part-of-speech tagging)`
      * 주어진 문장에서 품사를 식별하기 위해서 붙여 주는 태그(식별 정보)를 의미
  * **`자연어 처리 과정`**
    * 인간 언어인 `자연어가 입력 텍스트`로 들어옴
      * 인간 언어가 다양하듯 처리 방식이 조금씩 다르며, 현재는 영어에 대한 처리 방법들이 잘 알려짐
    * 입력된 `텍스트에 대한 전처리` 과정
    * 전처리가 끝난 `단어들을 임베딩`
      * 단어를 벡터로 변환하는 것
    * 컴퓨터가 이해 가능한 데이터가 완성되었기에 `모델/모형(ex)결정트리)`을 이용하여 데이터에 대한 분류 및 예측 수행
      * 데이터 유형에 따라 분류와 예측에 대한 결과가 달라짐

</details>


<details>
<summary><h2>23.09.26</h2></summary>

***
* torch34 ~ torch37
***

</details>

<details>
<summary><h2>23.09.27</h2></summary>

***
* torch37 ~ torch39
***

* **`seq2seq (sequence to sequence)`**
  * 입력 시퀀스(input sequence)에 대한 출력 시퀀스(output sequence)를 만들기 위한 모델
  * 품사 판별과 같은 시퀀스 레이블링과의 차이
    * 시퀀스 레이블링이란 입력 단어가 $x_1, x_2 ..., x_n$이라면 출력은$y_1, y_2 ..., y_n$이 도는 형태. 즉, 입력과 출력에 대한 문자열(sequence)가 같음
    * seq2seq는 판별보다 번역에 초점을 둔 모델, 번역은 입력 시퀀스의 $x_{1:n}$과 의미가 동일한 출력 시퀀스 $y_{1:m}$을 만드는 것이며, $x_i, y_i$간의 관계는 중요치 않음
  * `인코더와 디코더 네트워크` 사용
  * `입력 문장이 긴 시퀀스일 경우 정확한 처리 어려움` (인코더에서 사용하는 RNN(LSTM, GRU)의 `마지막 은닉 상태만 디코더로 전달`되기 때문)  


* **`어텐션 메커니즘 (attention mechanism)`**
  * 입력 문장의 모든 단어를 동일한 가중치로 취급하지 않고, 출력 문장에서 `특정위치에 대응하는 입력 단어들에 더 많은 가중치를 부여`하여 `입력과 출력의 길이가 다른 모델이 더욱 정확하고 유연하게 작동`할 수 있도록 함
  * `등장 이유`
    * 하나의 고정된 크기의 벡터에 모든 정보를 담다 보니 정보의 손실 발생
    * RNN에서 발생할 수 있는 기울기 소멸(vanishing gradient) 문제 발생  


* **`버트 (BERT)`**
  * 기존의 단방향 자연어 처리 모델들의 단점을 보완한 양방향 자연어 처리 모델
  * 검색 문장의 단어를 입력된 순서대로 하나씩 처리하는 것이 아닌 트랜스포머를 이용하여 구현  


* **`한국어 임베딩`**
  * `영어 임베딩과 다르지 않음`. 즉, 자연어 처리를 위한 임베딩 방법을 알고있다면 `언어와 상관없이 단어/문장에 대한 임베딩`을 진행하며, `모델을 생성하고 훈련`시킨 후 `예측 및 분류 수행` 가능
  * 대표적인 한국어 임베딩 모델
    * `다국어 버트 모델`
    * `KoBert`

</details>

***

<details>
<summary><h2>23.10.04</h2></summary>

***
* torch40 ~ torch42 | numpy01 ~ numpy10
***

* **`클러스터링 (clustering)`**
  * 어떤 데이터들이 주어졌을 때 특성이 비슷한 데이터끼리 묶어 주는 머신 러닝 기법
  * 머신 러닝 알고리즘에 딥러닝을 적용한다면 성능이 더 향상될 수 있음  


* **`클러스터링 알고리즘`**
  * `K-평균 군집화`
    * `알고리즘 원리`
      * 클러스터 중심인 중심점을 구하기 위해 `임의의 점 K를 선택`
      * 각 중심에 대한 거리를 계산, 각 데이터를 `가장 가까운 클러스터에 할당`
      * 할당된 데이터 평균을 계산, 새로운 `클러스터 중심을 결정`
      * 클러스터 할당이 `변경되지 않을 때까지 위의 과정을 반복`
    * 클러스터 개수를 좀 더 편리하게 결정할 수 있는 방법은 `클러스터 개수와 WCSS 간 관계를 그래프로 표현`한 후, `WCSS 변경이 평평하게 하락하는 구간을 선택`하는 것  
  * `가우시안 혼합 모델 (Gaussian Mixture Model, GMM)`
    * 이름 그대로 가우시안 분포(gaussian distribution)가 여러 개 혼합된 클러스터링 알고리즘
    * 현실에 있는 복잡한 형태의 확률 분포를 가우시안 분포 K개를 혼합하여 표현하자는 것이 가우시안 혼합 분포(gaussian mixture distribution)임
    * K는 하이퍼파라미터
  * `자기 조직화 지도 (Self-Organizing Map, SOM)`
    * `신경 생리학적 시스템을 모델링`한 것으로 `입력 패턴에 대해 정확한 정답을 주지 않고 스스로 학습을 하여 클러스터링`하는 알고리즘
    * `자기 조직화 지도의 학습 단계`
      * `초기화 (initialization)`
        * 모든 연결 가중치는 `작은 임의의 값으로 초기화`
      * `경쟁 (competition)`
        * 경쟁 학습을 이용하여 `입력층과 경쟁층을 연결`
        * `연결 강도 벡터가 입력 벡터와 얼마나 가까운지 계산`하여 `가장 가까운 뉴런이 승리`하는 `승자 독점(winner take all)`방식을 사용
        * 연결 강도 벡터와 입력 벡터가 가장 가까운 뉴런으로 계산되면 그 뉴런의 `이웃 뉴런들도 학습`을 하게되는데, `이때 모든 뉴런이 나닌 제한된 이웃 뉴련들만 학습`
      * `협력 (cooperation)`
        * `승자 뉴런은 네트워크에서 가장 좋은 공간 위치를 차지`하게 되며, 함께 `학습할 이웃 크기를 정의`
      * `적응 (adaptation)`
        * `승리한 뉴런`의 `가중치와 이웃 뉴런을 업데이트`
      * 최종적으로 `원하는 횟수`만큼 `경쟁과 협력을 반복`


* `WCSS (Within Cluster Sum of Squares)`
  * 올바른 클러스터 개수를 알아내는 이상적인 방법은 WCSS를 계산하는 것
  * WCSS는 모든 클러스터에 `각 데이터가 중심까지의 거리를 제곱하여 합을 계산`하는 것

</details>

<details>
<summary><h2>23.10.05</h2></summary>

***
* torch43 ~ torch44 | pandas01 ~ pandas08
***

* **`강화 학습 (reinforcement learning)`**
  * 머신 러닝/딥러닝의 한 종류로, 어떤 환경에서 어떤 행동을 했을 때 그것이 `잘된 행동인지 잘못된 행동인지를 판단`하고 `보상(또는 벌칙)을 주는 과정을 반복해서 스스로 학습`하게 하는 분야
  * 어떤 환경에서 어떤 행동을 하는지 알기 위해 `환경(environment)`과 `에이전트(agent)`라는 구성 요소를 사용
  * `환경`
    * 에이전트가 다양한 행동을 해 보고, `그에 따른 결과를 관측할 수 있는 시뮬레이터`
  * `에이전트`
    * 환경에서 `행동하는 주체`가 됨
  * **ex)** 게임에서는 게임기가 환경, 게임을 하는 사람이 에이전트  
  

* `마르코프 프로세스 (Markov Process, MP)`
  * `어떤 상태가 일정한 간격으로 변하고`, `다음 상태`는 `현재 상태에만 의존하는 확률적 상태 변화`를 의미
  * `현재 상태에 대해서만 다음 상태가 결정` 되며, `현재 상태까지의 과정`을 `전혀 고려할 필요가 없음`
  * 위와 같이 `변화 상태들이 체인처럼 엮여` 있다고 하여 `마르코프 체인(Markov chain)`이라고도 함  


* `마르코프 보상 프로세스 (Markov Reward Process, MRP)`
  * 마르코프 프로세스에서 `각 생태마다 좋고 나쁨(reward)`이 추가된 확률 모델
  * 상태 $a$에서 $a'$로 이동하였을 때 `이동 결과가 좋고 나쁨에 대해 보상(혹은 벌칙)`을 주는 것


* `마르코프 결정 과정 (Markov Decision Process, MDP)`
  * 기존 마르코프 보상 과정에서 `행동이 추가`된 확률 모델
  * 목표는 정의된 문제에 대해 `각 상태마다 전체적인 보상을 최대화하는 행동이 무엇인지 결정`하는 것
  * `MDP에서 가치 함수`
    * `상태-가치 함수 (state-value function)`
      * 에이전트가 놓인 상태 가치를 함수로 표현한 상태
    * `행동-가치 함수 (action-value function)`
      * 에이전트의 행동에 대한 가치를 함수로 표현한 상태


* `벨만 방정식 (Bellman equation)`
  * `상태-가치 함수`와 `행동-가치 함수`의 `관계를 나타내는 방정식`


* `벨만 기대 방정식 (Bellman expectation equation)`
  * 가치 함수 $v_\pi(s)$는 단순히 `어떤 상황에서 미래의 보상을 포함한 가치`를 나타냄<br>다음 상태로 이동하려면 `어떤 정책(policy)에 따라 행동`해야 하는데, 이때 `정책을 고려한 다음 상태로의 이동`


* `벨만 최적 방정식 (Bellman optimality equation)`
  * `강화 학습에서 추구하고자 하는 목표`는 최적의 가치 함수 값을 찾는 것이 아닌 `최대의 보상을 얻는 정책을 찾는 것`<br>즉, `최대의 보상을 얻기 위한 정책`을 찾기 위해 `가치 함수 값이 가장 큰 값`을 찾음<br>또한, 강화 학습에서 어떤 목표를 이루었을 때 `최적(optimal)`의 상태, 즉` 어떤 목적이 달정된 상태`라고 함
  * 위와 같은 `최적화된 정책을 따르는 벨만 방정식`을 `벨만 최적 방정식(Bellman optimality equation)`이라 함
  * `최적의 가치 함수`
    * 최대의 보상을 갖는 가치 함수
    * `상태-가치 함수`는 `어떤 상태가 더 많은 보상을 받을 수 있는지` 알려 주며, `행동-가치 함수`는 `어떤 상태에서 어떤 행동을 취해야 더 많은 보상을 받을 수 있는지` 알려줌
  * `최적의 상태-가치 함수`
    * 최적의 상태-가치 함수$(v_*(s))$는 `주어진 모든 정책에 대한 상태-가치 함수의 최댓값`
  * `최적의 행동-가치 함수`
    * 최적의 행동-가치 함수$(q_*(s,a))$는 `주어진 모든 정책에 대해 행동-가치 함수의 최댓값`

</details>

***

<details>
<summary><h2>23.10.10</h2></summary>

***
* torch45 ~ torch47
***

* **`생성 모델`**
  * `오토인코더`
  * `GAN`

</details>