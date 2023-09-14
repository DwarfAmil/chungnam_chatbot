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
<blockquote style="color: inherit">
<details>
<summary><h3>지도 학습</h3></summary>

<blockquote style="color: inherit">
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
            $$
            \begin{aligned}
            &(a, b : \text{입력 벡터})
            \end{aligned}
            $$
    * **비선형을 위한 커널**
        * `다항식 커널`
            * 실제로는 특성을 추가하지 않지만, 다항식 특성을 많이 추가한 것과 같은 결과를 얻을 수 있는 방법
            * 실제로는 특성을 추가하지 않지만, 엄청난 수의 특성 조합이 생기는 것과 같은 효과를 얻기 때문에 고차원으로 데이터 매핑이 가능
            $$K(a, b) = (\gamma a^T \cdot b)^d$$
            $$
            \left\{
            \begin{aligned}
            &a, b : \text{입력 벡터} \\
            &\gamma : \text{감마} \\
            &d : \text{차원, 이때 } \gamma, d \text{는 하이퍼파라미터}
            \end{aligned}
            \right\}
            $$


        * `가우시안 RBF 커널`
            * 입력 벡터를 차원이 무한한 고차원으로 매핑하는 것으로, 모든 차수에 모든 다항식을 고려
            * 다항식 커널은 차수에 한계가 있지만 가우시안 RBF는 차수에 제한 없이 무한한 확장이 가능
            $$K(a, b) = \exp\left(-\gamma \cdot \|a - b\|^2\right)$$
            $$
            \begin{aligned}
            &(\text{이때 } \gamma \text{는 하이퍼파라미터)}
            \end{aligned}
            $$
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
        $$
        \begin{aligned}
        &P_k = A : \text{영역에 속하는 데이터 가운데 }k\text{ 범주에 속하는 데이터 비율}
        \end{aligned}
        $$
    * `지니 계수`
        * 불순도를 측정하는 지표로, 데이터의 통계적 분산 정도를 정량화해서 표현한 값
        * 지니 계수는 원소 n개 중에서 임의로 두개를 추출했을 때, 추출된 두 개가 서로 다른 그룹에 속해 있을 확률을 의미
        $$Gini(S) = 1 - \sum_{i=1}^{c} p_i^2$$
        $$
        \begin{aligned}
        &S : \text{이미 발생한 사건의 모음} \\
        &c : \text{사건 개수}
        \end{aligned}
        $$
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

<blockquote style="color: inherit">
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

| 구분 | 일반적인 회귀 분석 | 로지스틱 회귀 분석 |
|----------|----------|----------|
| 종속 변수 | 연속형 변수 | 이산형 변수 |
| 모형 탐색 방법 | 최소제곱법 | 최대우도법 |
| 모형 검정 | F-테스트, t-테스트 | $X^2$ 테스트 |

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
</blockquote>
</details>
</blockquote>
                    
</details>
</blockquote>

<blockquote style="color: inherit">
<details>
<summary><h3>비지도 학습</h3></summary>

* 비지도 학습
    * 비지도 학습은 레이블이 필요하지 않으며 정답이 없는 상태에서 훈련시키는 방식이다.
    * 비지도 학습에는 `군집`과 `차원 축소`가 있다.
* `군집`
    * 각 데이터의 유사성(거리)를 측정한 후 유사성이 높은(거리가 짧은) 데이터끼리 집단으로 분류하는 것
* `차원 축소`
    * 차원을 나타내는 특성을 줄여서 데이터를 줄이는 방식

<br>
<div align="center">

| 구분 | 군집 | 차원 축소 |
|----------|----------|----------|
| 목표 | 데이터 그룹화 | 데이터 간소화 |
| 주요 알고리즘 | K-평균 군집화(K-Means) | 주성분 분석(PCA) |
| 예시 | 사용자의 관심사에 따라<br>그룹화 하여 마케팅에 활용 | - 데이터 압축<br>- 중요한 속성 도출 |

</div>

<blockquote style="color: inherit">
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
</blockquote>

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

    | 구분 | 구성 요소 | 설명 |
    |----------|----------|----------|
    | 층 | 입력층 (input layer) | 데이터를 받아들이는 층 |
    | 층 | 은닉층 (hidden layer) | 모든 입력 노드부터 입력 값을 받아 가중합을 계산하고,<br>이 값을 활성화 함수에 적용하여 출력층에 전달하는 층 |
    | 층 | 출력층 (output layer) | 신경망의 최종 결괏값이 포함된 층 |
    | 가중치 (weight) | 가중치 (weight) | 노드와 노드 간 연결 강도 |
    | 바이어스 (bias) | 바이어스 (bias) | 가중합에 더해 주는 상수로, 하나의 뉴런에서<br>활성화 함수를 거쳐 최종적으로 출력되는 값을<br>조절하는 역할을 함 |
    | 가중합 (weighted sum)<br>/ 전달함수 | 가중합 (weighted sum)<br>/ 전달함수 | 가중치와 신호의 곱을 합한 것 |
    | 함수 | 활성화 함수 (activation function) | 신호를 입력받아 이를 적절히 처리하여 출력해 주는 함수 |
    | 함수 | 손실 함수 (loss function) | 가중치 학습을 위해 출력 함수의 결과와 실제 값 간의 오차를 측정하는 함수 |

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

    | 구분 | 메모리 | 계산 그래프 상주 유무 |
    |----------|----------|----------|
    | tensor.clone() | 새롭게 할당 | 계산 그래프에 계속 상주 |
    | tensor.datach() | 공유해서 사용 | 계산 그래프에 상주하지 않음 |
    | tensor.clone().detach() | 새롭게 할당 | 계산 그래프에 상주하지 않음 |

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

* 파이썬 웹 프레임워크
    * 장고
      * 특징
        * 파이썬 웹 프레임워크 중에서도 가장 유명함
        * 중규모 이상 웹을 구축시에 자주 사용
        * 개발에 필요한 많은 기능이 구현되어 있어 풀스택 프레임워크로 불림
        * Django REST Framework(DRF)를 추가 설치함으로서 웹 앱뿐만 아닌 REST API를 간단히 만들 수 있음
    * 플라스크
      * 특징
        * 마이크로 웹 프레임워크이다.
        * 데이터베이스 기능이 포함되어 있지 않는 등 최소한의 기능만 제공
        * 최소한의 규약만 있어 앱 구성 자유롭게 결정 가능
        * 데이터베이스 기능 등 확장 기능을 많이 지원
    * 보틀
      * 특징
        * 웹 앱을 만들기 위한 프레임워크 중에는 가장 단순함
        * bottle.py라는 하나의 파일로만 구성되어있음
        * 파이썬 표준 라이브러리 이외에 의존 관계 없음
        * 마이크로 웹 프레임워크 중 하나로 플라스크보다 단순하고 빠르고 가벼움
    * FastAPI
      * 특징
        * 비동기 처리가 용이하도록 만들어진 파이썬 웹 프레임워크
        * 요청을 처리하는 속도 매우 빠름
    
    <br>
    <div align="center">

    | 프레임워크 | 공식 사이트 | 라이선스 | 초기 개발자 | 최초 릴리스 | 템플릿 엔진 | O/R 매퍼 |
    |----------|----------|----------|----------|----------|----------|----------|
    | 장고 | www.djangoproject.com | BSD License | Adrian<br>Holovaty,<br>Simon Willison | 2005년 | Django<br>Template | Django<br>O/R 매퍼 |
    | 플라스크 | palletsproject.com/p/flask | BSD License | Armin<br>Ronacher | 2010년 | Jinja2 | 없음 |
    | 보틀 | bottlepy.org/docs/dev | MIT License | Marcel<br>HEllkamp | 2009년 | Simple<br>Template<br>Engine | 없음 |
    | FastAPI | fastapi.tiangolo.com | MIT License | Sebastian<br>Ramirez | 2018년 | Jinja2 | 없음 |
    </div>
  
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
* flaskbook/apps
***

* flask-sqlalchemy
  * 플라스크에서 SQLAlchemy를 이용하는 확장
* flask-migrate
  * 데이터베이스를 마이그레이트하는 확장
    * migrate - 옮기다 / 이동하다
* flask-wtf
  * 플라스크에서 유효성 검증이나 CSRF에 대처하기 위한 폼을 작성하는 확장

  <br>
  
  * 유효성 검증
    * 구체적인 의도를 가진 사용(목적)을 위하여 특정 요구사항이 충족되었다는 객관적인 증거를 제공하고 실험에 의해 확인하는 과정
  * CSRF (Cross Site Request Forgery)
    * 웹 어플리케이션 취약점 중 하나로 인터넷 사용자(희생자)가 자신의 의지와는 무관하게 공격자가 의도한 행위(수정, 삭제, 등록 등)를 특정 웹사이트에 요청하게 만드는 공격
</details>