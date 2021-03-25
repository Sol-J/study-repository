---
description: Transformer (2017)
---

# Attention

 이어서 등장할 Transformer에 대해 이해하려면, **Sequence to Sequence \(Seq2Seq\)**을 알고있어야 한다. Seq2Seq는 2014년에 기계번역을 위해 등장한 모델로, '인코더-디코더' 라고도 불린다.  

 이전에 자연어처리에서 시퀀스의 흐름을 조정하기 위해 사용한 RNN은 출력이 바로 이전의 입력만 고려하기 때문에 정확도에 한계가 있었다. 즉 전체 문장을고려하지 않고 다음 단어를 생성해내기 때문이다. 따라서 이를 해결하기 위해 Seq2Seq가 등장하였다. Seq2Seq는 아래 그림과 같이 두개의 LSTM으로 구성된 모델이다. 인코더는 입력으로 들어온 sequential data를 압축해서 context vector로 표현해주고, 디코더는 압축된 context vector를 새로운 sequential data로 변환해준다. 

![Source: https://wikidocs.net/24996](../.gitbook/assets/1.png)

 이러한 Seq2Seq는 전체 input을 살펴본 다음, context vector에 정보를 압축해서 전달하기 때문에 전체적인 맥락을 파악하는 데에 있어서 효과적이었다. 하지만 결국 입력 문장이 너무 길어지면 시퀀스를 압축하는 과정에서 정보가 소실되고, 효율적으로 학습을 하지 못한다는 RNN 기반 모델의 고질적인 한계에 부딪히게 된다. 

 이와 같은 현상을 개선하기 위해 2017년에 RNN 없이 설계한 자연어처리 모델인 **Transformer**가 등장하게 된다. 기존에 자연어처리에서 시퀀스의 흐름을 조정하던 RNN 없이 설계 되었음에도 불구하고 RNN 보다 우수한 성능을 보인다는 것이 특징적이다. 대신 Transformer는 오직 어텐션\(Attention\)만을 사용하여 인코더-디코더를 구현하였다. 

![Source: &#xAD6C;&#xAE00; &#xB17C;&#xBB38; Attention is All You Need \(2017\)](../.gitbook/assets/2021-03-12-5.05.12.png)

 위 그림과 같이 인코더가 기존의 RNN으로 구성되는 게 아니라 CNN으로 병렬적으로 구성되었다. 디코더 관점에서 어텐션을 바라보는게 아니라, 인코더에서 셀프 어텐션한다. 셀프 어텐션이라는 것은 문장에서 중요한 단어들에 집중하여 각 단어의 정보를 업데이트하는 것이다.

\(작성중\)







