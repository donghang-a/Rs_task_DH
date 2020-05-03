
## L14 Thinking
**1.什么是Graph Embedding，都有哪些算法模型**                   
把由节点和边组成的图关系数据（非欧几里得数据）中的节点降维成Embedding向量表达的方法就是Graph Embedding          
主要算法模型有：    
factorization methods （图因式分解机）  
random walk techniques（随机游走）如DeepWalk和Node2Vec      
deep learning（深度学习）如GCN

**2.如何使用Graph Embedding在推荐系统，比如NetFlix 电影推荐，请说明简要的思路**             
电影之间是有关联的比如相同的题材类型主题，相同的导演编剧演员，这样电影和电影之间可以构成图关系数据。然后可以进行Graph Embedding，得出每个电影的向量表达，然后可以得出电影之间的相似度。同样用户之间也是有关系的，相同的职业，相似的年龄，相同的出生地工作地，相同的受教育程度和经历等等也可以构成图关系数据。然后也进行Graph Embedding，得出每个用户的向量表达，这样就得出了每个用户之间的相似程度。假设用户A给电影X打了高分，那么我们可以用X的embedding找出和电影X最相似的电影，推荐给用户A。同时我们也可以找出和用户A最相似的用户，把电影X推荐给他。

**3.在交通流量预测中，如何使用Graph Embedding，请说明简要的思路**   
将路口作为节点。路口和路口间的路径作为边，如果是单行道，就是一条有向边，如果是双行道，就是两条有向边。可以用历史观测车流量大小作为边的权重。然后对每个路口进行Graph Embedding。

**4.在文本分类中，如何使用Graph Embedding，请说明简要的思路**   
可以对文本和文本进行相似度计算，文本作为节点，相似度作为权重的一条边。这样就生成图关系数据。然后进行Graph Embedding得出每个文本的embedding向量表达。然后再用这些embedding表达做聚类。
