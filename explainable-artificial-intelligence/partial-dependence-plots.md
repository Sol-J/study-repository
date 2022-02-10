# Partial Dependence Plots

부분 의존성 플롯은 개별 피처가 목표 변수에 어떻게 작용하는지 알아볼 수 있는 도구로, 특정 범위 내에서 관심 있는 피처의 값을 변화시켜 목표 변수의 값을 계산하고 그린다. 따라서 부분 의존성 플롯을 사용하면 피처의 값이 변할 때 모델에 미치는 영향을 가시적으로 이해할 수 있다.\
이 또한 학습한 모델과 데이터만 있으면 그래프를 뽑아주는 방법이기 때문에, 어느 모델이든(Model-agnostic) 학습시킨 후(Post-hoc)에 적용할 수 있다. 부분 의존성 플롯이 그려지는 원리는 다음과 같다.

![](<../.gitbook/assets/스크린샷 2022-02-11 오전 1.40.36.png>)

{% embed url="https://colab.research.google.com/drive/1JLX5lKbPVCRYSp45GCYs9WbeQ-YXWOkK?usp=sharing" %}
퍼뮤테이션 피처 중요도 & 부분 의존성 플롯 예제 &#x20;
{% endembed %}
