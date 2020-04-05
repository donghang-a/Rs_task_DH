
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
使用behavior layer，interest extractor layer 以及 interest evolving layer从用户历史行为中挖掘用户与目标商品相关的兴趣及演变。
通过引入序列模型 AUGRU 模拟了用户兴趣进化的过程.在 Embedding layer 和 Concatenate layer 之间加入了生成兴趣的 Interest Extractor Layer 和模拟兴趣演化的 Interest Evolving layer。Interest Extractor Layer 使用了GRU的结构抽取了每一个时间片内用户的兴趣。Interest Extractor Layer，通过辅助loss，提升兴趣表达的准确性。Interest Evolution Layer，更准确的表达用户兴趣的动态变化性，在GRU基础上增加Attention机制，找到与target AD相关的interest。DIN中简单的使用外积完成的activation unit ，使用attention-based GRU网络，更好的挖掘序列数据中的兴趣及演化。



**5.DSIN关于Session的洞察是怎样的，如何对Session兴趣进行表达**  
将用户的点击行为按照时间排序，前后的时间间隔大于30min，算成另一个session。  
首先使用带有Bias Encoding（偏置编码）的Self-Attention（自我注意力）机制，提取用户的Session兴趣向量。然后利用Bi-LSTM 对用户的Session之间的交互进行建模 ，带有上下文信息的Session兴趣向量。最后利用Activation Unit（局部激活单元）自适应地学习各种会话兴趣对目标item的影响。


**6.如果你来设计淘宝定向广告，会有哪些future work（即下一个阶段的idea）**   
