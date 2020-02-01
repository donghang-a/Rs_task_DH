import pandas as pd
import numpy as np


# 数据加载
data = pd.read_csv('./Market_Basket_Optimisation.csv')
print('原数据\n',data.head())
# data 原数据第一行数据变成了列名，需要修正
mbdata=pd.DataFrame(np.array(data.columns).reshape(1,len(data.columns)),columns=range(len(data.columns)))
data.columns=range(len(data.columns))
mbdata=mbdata.append(data,ignore_index=True)
print('修正数据\n',mbdata.head())


# 整合成mlxtend 识别的数据格式
mldata=mbdata.stack()
mldata=mldata.reset_index()
mldata=mldata.drop(['level_1'],axis=1)
mldata.columns=['Transaction','Item']
hot_encoded_df=mldata.groupby(['Transaction','Item'])['Item'].count().unstack().reset_index().fillna(0).set_index('Transaction')
print('one-hotdata\n',hot_encoded_df.head())



# 采用efficient_apriori工具包
def rule1():
	from efficient_apriori import apriori

	transactions = []
	for i in range(len(mbdata)):
		set1 = set(mbdata.iloc[i].dropna())
		transactions.append(set1)
	itemsets, rules = apriori(transactions, min_support=0.04, min_confidence=0.2)


	print('频繁项集：\n', itemsets)
	print('关联规则：\n', rules)





def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
# 采用mlxtend.frequent_patterns工具包
def rule2():
	pd.options.display.max_columns = 100
	from mlxtend.frequent_patterns import apriori
	from mlxtend.frequent_patterns import association_rules
	hot_encoded_data = hot_encoded_df.applymap(encode_units)
	frequent_itemsets = apriori(hot_encoded_data, min_support=0.04, use_colnames=True)
	rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
	print("频繁项集：\n", frequent_itemsets)
	print("关联规则：\n", rules[(rules['lift'] >= 1) & (rules['confidence'] >= 0.2)])


rule1()
print('-'*100)
rule2()
