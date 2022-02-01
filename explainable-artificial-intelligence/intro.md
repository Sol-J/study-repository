---
description: Fairness, Accountability, and Transparency of Algorithms
---

# Intro

#### **XAI(eXplainable Artificial Intelligence, 설명 가능한 인공지능)란 ?**

* XAI는 인공지능 모델이 특정 결론을 내리기까지 어떤 근거로 의사결정을 내렸는지를 알 수 있게 '설명 가능성'을 추가하는 것이다.&#x20;

#### XAI 등장 배경&#x20;

* XAI는 2004년도에 반 렌트(Michel van Lent)와 피셔(William Fisher), 만쿠소(Michael Mancuso) 세 사람이 제시한 용어로, 이들은 인공지능 시스템이 갈수록 복잡해지는 반면에 그것들의 자기 설명 기능에는 발전이 없었다는 것을 지적하였다.&#x20;
* 인공지능 기술이 계속해서 발전할 수록 기계가 학습하는 feature1)의 양이 사람이 해석 불가능할 만큼 많아지게 된다.&#x20;
* 따라서 인공지능에 설명 능력을 부여하여 기계와 인간의 상호작용에 합리성을 확보할 필요가 있다.&#x20;
* XAI 연구는 그동안 여러 시도가 있었으나, 인터넷과 GPS를 개발한 미국의 DARPA(고등연구계획국)에 의해 2016년에 본격적으로 시작되었다.

#### 모델의 Accuracy와 Interpretability 간의Trade-off&#x20;

* 모델의 interpretability가 높을 수록 모델 구조가 단순하기 때문에 accuracy는 낮을 수 밖에 없게 된다. 즉 accuracy와 interpretability 간의 trade-off가 존재한다. 이때 높은 accuracy가 요구되는 경우, interpretability가 낮은 모델을 사용하게 되고 모델 자체만으로는 예측 결과에 대한 해석이 어렵기 때문에 XAI가 필요하게 된다.

![Figure 1. The trade-off between interpretability and accuracy of some relevant ML models.](<../.gitbook/assets/스크린샷 2022-02-01 오후 3.43.59.png>)

> Morocho-Cayamcela, M. E., Lee, H., & Lim, W. (2019). Machine learning for 5G/B5G mobile and wireless communications: Potential, limitations, and future directions. _IEEE Access_, 7, 137184-137206.

*   High Interpretable Model

    Logistic Regression의 경우 각 features(x1, x2, x3...)가 y에 어느정도 기여했는지 회귀 계수 을 통해 확인할 수 있기 때문에 예측값에 대한 해석이 가능하다. 또한 Decision Tree는 모델 내부 구조를 보면 어떤 feature가 어떤 값을 가졌을 때 특정 범주로 분류되었는지 확인할 수 있기 때문에 예측값에 대한 해석이 가능하다.
*   High Accurate Model&#x20;

    Neural Networks를 활용한 모델은 예측 결과의 정확도는 높을 수 있지만 모델이 어떤 과정을 통해 도출한 결과인지 파악하기 어렵다. 모델의 내부를 들여다보아도 수 많은 파라미터로 구성되어 있어 사람이 이해하는 데에 어려움이 있다. &#x20;
