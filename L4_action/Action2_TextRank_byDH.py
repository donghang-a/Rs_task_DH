#-*- encoding:utf-8 -*-
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import jieba

with open("news.txt", "r") as f:    #打开文件
    data = f.read()   #读取文件
    print(data)

tr4w = TextRank4Keyword()
tr4w.analyze(text=data, lower=True, window=3)
print('关键词：')
for item in tr4w.get_keywords(20, word_min_len=2):
    print(item.word, item.weight)

# 输出重要的句子
tr4s = TextRank4Sentence()
tr4s.analyze(text=data, lower=True, source = 'all_filters')
print('摘要：')
# 重要性较高的三个句子
for item in tr4s.get_key_sentences(num=3):
	# index是语句在文本中位置，weight表示权重
    print(item.index, item.weight, item.sentence)
