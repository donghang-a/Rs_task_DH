# 使用networkX计算节点的pagerank
import networkx as nx
import matplotlib.pyplot as plt

# 创建有向图
G = nx.DiGraph()   
# 设置有向图的边集合
edges = [("A", "B"), ("A", "F"), ("A", "E"), ("A", "D"), ("B", "C"), ("C", "E"), ("D", "A"), ("D", "C"), \
         ("D", "E"), ("E", "C"), ("E", "B"), ("F", "D")]
# 在有向图G中添加边集合
for edge in edges:
    G.add_edge(edge[0], edge[1])

# 有向图可视化
#circular_layout：在一个圆环上均匀分布节点

#shell_layout：节点都在同心圆上

layout = nx.circular_layout(G)
nx.draw(G, pos=layout, with_labels=True, hold=False)
plt.show()

# 计算简化模型的PR值
pr = nx.pagerank(G, alpha=1)
print("简化模型的PR值：\n", pr)

# 计算随机模型的PR值
pr = nx.pagerank(G, alpha=0.8)
print("随机模型的PR值：\n", pr)