import pandas as pd
import numpy as np
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image

from lxml import etree
from nltk.tokenize import word_tokenize


# 数据加载
data = pd.read_csv('./Market_Basket_Optimisation.csv')

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



def create_word_cloud(f):
	print('根据词频，开始生成词云!')
	#f = remove_stop_words(f)
	cut_text = word_tokenize(f)
	#print(cut_text)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		max_words=100,
		width=2000,
		height=1200,
    )
	wordcloud = wc.generate(cut_text)
	# 写词云图片
	wordcloud.to_file("Market_Basket_wordcloud.jpg")
	# 显示词云文件
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()

all_word=" ".join(mldata['Item'])
create_word_cloud(all_word)

#画条形图看购买前10多的商品

print('总共有%d种商品' %len(mldata['Item'].unique()))
item_count=mldata['Item'].value_counts()
plt.figure(figsize=(20,11))
sns.set(font_scale=0.8)
sns.barplot(item_count.values[:10],item_count.index[:10],)

plt.show()

