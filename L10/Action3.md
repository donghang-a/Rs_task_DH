## L10 Action3

P2P租车也是一个双向选择的过程。顾客租车时一般会有明确的目的租车用途，比如越野车或是商务车等等。当顾客query明确的车型或用途时，那么以车型信息为主综合位置价格颜色关键字描述等要素优化推荐list的排序。同时为了避免车主拒绝，将要求高的车主，可能在list中的排序降低。采用Learnig to rank来做，将问题转换为pairwise regression问题，将预定的listing作为正样本，拒绝的作为负样本。               
可能的embedding策略，对于车主和他的车，把每个用户在一小段时间内连续点击浏览过的车Session看做一个句子，每辆车当做word，训练出车的embedding，同时根据车的自身属性，类型排量颜色车龄品牌等等进一步优化。这样我们就有了每辆车的embedding映射到另一个空间的信息，而相似的车在这个空间中距离更近。embedding之后，既可以用来相似推荐，也可以在query中排序呈现。



