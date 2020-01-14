from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits

import matplotlib.pyplot as plt

from sklearn import tree
import numpy as np
import datetime
data = np.load('mnist.npz') #从本地读取数据集
# 加载数据

train_x, train_y, test_x, test_y  = data['x_train'], data['y_train'], data['x_test'], data['y_test']
train_x = train_x.reshape(train_x.shape[0], train_x.shape[1]*train_x.shape[2])
test_x = test_x.reshape(test_x.shape[0], test_x.shape[1]*test_x.shape[2])




# 采用Z-Score规范化
ss = preprocessing.StandardScaler()

train_ss_x = ss.fit_transform(train_x)
test_ss_x = ss.transform(test_x)


starttime = datetime.datetime.now()
clf=tree.DecisionTreeClassifier()
clf=clf.fit(train_x, train_y)

predict_y_clf=clf.predict(test_x)

endtime = datetime.datetime.now()
duringtime = endtime - starttime
print('分类树准确率: %0.4lf' % accuracy_score(predict_y_clf, test_y))
print('分类树耗时\n',duringtime)

starttime = datetime.datetime.now()
rgs=tree.DecisionTreeRegressor()
rgs=rgs.fit(train_x, train_y)

predict_y_rgs=rgs.predict(test_x)

endtime = datetime.datetime.now()
duringtime = endtime - starttime
print('回归树耗时\n',duringtime)

print('回归树准确率: %0.4lf' % accuracy_score(predict_y_rgs, test_y))
