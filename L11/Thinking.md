
## L11 Thinking
**1.电商定向广告和搜索广告有怎样的区别，算法模型是否有差别**       
定向广告 用户没有很明显的意图（主动的Query查询）,用户来到淘宝之前，自己也没有特别明确的目标（利用以往的历史行为进行item推荐）
      
**2.定向广告都有哪些常见的使用模型，包括Attention机制模型**     
LR模型（线性模型） ,MLR模型（非线性模型）,  DNN模型（深度学习）
Deep Interest Network模型，Deep Interest Evolution Network模型，Deep Session Interest Network模型
  

**3.DIN中的Attention机制思想和原理是怎样的**        
Attention思想：在对用户兴趣的表示上引入了attention机制，即对用户的每个兴趣表示赋予不同的权值，这个权值是由用户的兴趣和待估算的广告进行匹配计算得到的.在pooling的时候，与 candidate Ad 相关的商品权重大一些，与candidate Ad 不相关的商品权重小一些。       
原理：在对用户行为的embedding计算上引入了attention network ，把用户历史行为特征进行embedding操作，视为对用户兴趣的表示，之后通过Attention Unit，对每个兴趣表示赋予不同的权值。

**4.DIEN相比于DIN有哪些创新**          
通过引入序列模型 AUGRU 模拟了用户兴趣进化的过程.在 Embedding layer 和 Concatenate layer 之间加入了生成兴趣的 Interest Extractor Layer 和模拟兴趣演化的 Interest Evolving layer。Interest Extractor Layer 使用了GRU的结构抽取了每一个时间片内用户的兴趣。Interest Evolving layer 利用序列模型 AUGRU 的结构将不同时间的用户兴趣串联起来，形成兴趣进化的链条。最终把当前时刻的“兴趣向量”输入上层的多层全连接网络，与其他特征一起进行最终的 CTR 预估。




**5.DSIN关于Session的洞察是怎样的，如何对Session兴趣进行表达**      


**6.如果你来设计淘宝定向广告，会有哪些future work（即下一个阶段的idea）**   