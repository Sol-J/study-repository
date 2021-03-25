---
description: 'Word2vec (2013), GloVe (2014), FastText (2016)'
---

# Word embeddings

 '자연어' 라는 것은 말 그대로 문자로 이루어져 있고, 컴퓨터는 이를 처리할 수 없기 때문에 이를 수학적인 표현으로 변환해주는 과정이 필요하다. 또한 단어를 표현하는 방법에 따라서 자연어 처리의 성능은 크게 달라질 수 있기 때문에 이와 관련된 다양한 연구들이 등장 하였다. 

 Word embedding은 단어들의 분포를 공간 상의 벡터로 표현함으로써, 사람의 언어를 컴퓨터가 처리할 수 있게끔 하는 수학적인 모델이다. 여기에 대한 예시를 30초의 짧은 영상으로 보여주는 링크를 함께 첨부한다. [https://youtu.be/fzXwGQeVNI4](https://youtu.be/fzXwGQeVNI4)

 이러한 임베딩 개념으로 인해 자연어처리 분야는 획기적인 발전을 이루었는데, 여기에 관한 3가지 방법론을 소개한다.   

 먼저 2013년에 등장 **Word2vec\(w2v\)** 이다. Word2vec는 훈련 방법에 따라서  Continuous Bag of Words \(CBOW\) 와 Skip-gram 방식으로 나뉜다. CBOW는 맥락으로부터 타겟을 예측하기 위한 모델이고, 반대로 Skip-gram은 타겟으로부터 맥락을 예측하기 위한 모델이다. 

 아래의 그림과 같이 CBOW에서는 'you'와 goodbye'라는 맥락을 토대로 빈칸에 'say'가 들어갈 것을 예측한다. Skip-gram은 'say'라는 타켓 하나로 'you'와 'goodbye'를 예측해야한다. 이러한 점에서 CBOW 보다  skip-gram이 더 어려운 문제에 도전한다고 볼 수 있고, 그만큼 skip-gram에서 훈련된 모델은 단어의 분포를 표현하는 데에 있어서 더 좋은 퍼포먼스를 보일 수 있다. 

![Source: https://github.com/WegraLee/deep-learning-from-scratch-2](../.gitbook/assets/2021-03-12-2.54.59.png)

 하지만 이러한 Word2vec 모델은 사용자가 지정한 window 내에서만 학습이 이루어지기 때문에, 코퍼스 전체의 co-occurrence는 반영되기 어렵다는 한계를 지적하면서 2014년에 **Global Vectors for Word Representation \(GloVe\)**가 등장하였다.  전체 코퍼스로부터 동시등장비율\(co-occurrence ratio\)을 계산하여 예측하기 때문에, 코퍼스 전체의 통계 정보를 좀 더 잘 반영한다고 볼 수 있다. 

 그러나 지금까지의 임베딩에 관한 방법론에서 아직 해결되지 못한 문제들이 남아있다. 이전의 Word2vec 모델은 단어 단위로 vocabulary를 구성하여 학습하기 때문에, 만약 사전에 없는 새로운 단어\(Out of Vocabulary, OOV\)가 등장 하면 데이터 전체를 다시 학습해야 한다는 한계가 있었다.  

 이러한 문제를 해결하기 위해 **FastText**가 등장하게 된다. 이는 페이스북이 2016년 발표한 방법론으로, Word2Vec의 확장형이라고 볼 수 있다. 가장 큰 차이점은 Word2Vec은 단어를 쪼갤 수 없는 단위라고 생각했다면, FastText에서는 하나의 단어 안에도 내부 단어\(subword\)가 존재한다고 간주한다.   

 이해를 위하여 예시를 [https://bit.ly/3t5TdGW](https://bit.ly/3t5TdGW) 에서 가져왔다. birthplace\(출생지\)란 단어를 학습하지 않은 상태라고 해보자. 만약 이전에 학습에서 n-gram으로써 birth와 place를 학습한 적이 있다면 birthplace의 임베딩 벡터 값을 만들 수 있다. 즉 birth와 place라는 subword를 통해 모르는 단어\(OOV\)에 대해서도 벡터 표현이 가능하고, 다른 단어와의 유사도 계산도 할 수 있게 되는 것이다.  



