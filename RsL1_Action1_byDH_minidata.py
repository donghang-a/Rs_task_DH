from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits

import matplotlib.pyplot as plt

from sklearn import tree

# 加载数据
digits = load_digits()
data = digits.data

# 分割数据，将25%的数据作为测试集，其余作为训练集
train_x, test_x, train_y, test_y = train_test_split(data, digits.target, test_size=0.25, random_state=33)

# 采用Z-Score规范化
ss = preprocessing.StandardScaler()
#print('before zs\n',train_x[0])
train_ss_x = ss.fit_transform(train_x)
test_ss_x = ss.transform(test_x)
#print('after zs\n',train_ss_x[0])


clf=tree.DecisionTreeClassifier()
clf=clf.fit(train_ss_x, train_y)

predict_y_clf=clf.predict(test_ss_x)
print('分类树准确率: %0.4lf' % accuracy_score(predict_y_clf, test_y))

rgs=tree.DecisionTreeRegressor()
rgs=rgs.fit(train_ss_x, train_y)

predict_y_rgs=rgs.predict(test_ss_x)
print('回归树准确率: %0.4lf' % accuracy_score(predict_y_rgs, test_y))
