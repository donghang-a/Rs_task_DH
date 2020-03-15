## L8 Thinking
**1.在CTR点击率预估中，使用GBDT+LR的原理是什么？**          
GBDT是一种多个弱分类器的树模型算法。先将部分训练集通过GBDT多个弱分类器梯度下降法进行迭代，得到最终叶子节点上选择代表的位置。以这个位置输出类似one-hot编码的位置向量，这个向量就成了原始数据的新特征。利用已经训练好的GBDT模型将剩余的训练集进行分类，得出训练集的新特征，将新特征传入LR模型，训练LR模型。


**2.Wide & Deep的模型结构是怎样的，为什么能通过具备记忆和泛化能力（memorization and generalization）**          
Wide & Deep 就是LR线性模型和DNN深度学习模型。LR模型有着较好的记忆能力，发掘特征之间的相关性。DNN深度模型有较好的泛化推理能力，能发掘特征隐含的深层次的相关性。Wide & Deep就是将LR和DNN连个模型的结果融合，做成一个端到端的模型。


**3.在CTR预估中，使用FM与DNN结合的方式，有哪些结合的方式，代表模型有哪些？**        
一种是并行结构，FM和DNN分开计算，代表模型是DeepFM           
另一种是串行架构，将FM的结果作为DNN的输入，然后训练DNN模型，代表模型为NFM模型。

**4.Surprise工具中的baseline算法原理是怎样的？BaselineOnly和KNNBaseline有什么区别？**       
baseline算法原理：用户对商品的评分等于平均分加上特定用户对整体的偏差加上该商品对整体的偏差。使用ALS进行优化。BaselineOnly就是用上述原理，并且使用ALS算法计算用户对整体的偏差和该物品对整体的偏差，从而进行评分预测。KNNBaseline还是用协同过滤的方法，考虑到用户打分的偏差，偏差计算时使用baseline，在KNNWithMeans基础上，用baseline替代均值

**5.GBDT和随机森林都是基于树的算法，它们有什么区别？**    
GBDT是多个弱分类器，一个树在另一个树的基础上迭代，相当于串行。而随机森林是并行，通过自助采样的方法生成众多并行式的分类器，多个决策树，采用多数投票机制输出。

**6.基于邻域的协同过滤都有哪些算法，请简述原理**        
KNNBasic，KNNWithMeans，KNNWithZScore，KNNBaseline等。  
KNNBasic就是基本的协同过滤，用户u和用户v的相似度乘以用户v对物品i的打分，除以用户u,v相似度累加，就是用户u对商品i打分的预估值。   
KNNWithMeans，考虑到用户v的个性化部分， 用户v对物品i的打分减去用户v的平均打分。然后进行协同过滤。   
KNNWithZScore，把用户v的打分做一个Zscore规范化，衡量偏离均值多少个标准差。







