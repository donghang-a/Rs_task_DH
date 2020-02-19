import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression #逻辑回归

from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import cross_val_score
from sklearn import metrics
data = pd.read_csv('./train.csv')
data.drop(["EmployeeNumber",'Over18','user_id'],inplace=True,axis=1)
data["Attrition"] = (data["Attrition"]== "Yes").astype("int")


Y=data.Attrition
X=data.drop(["Attrition"],axis=1)
dvec=DictVectorizer(sparse=False)
X_data=dvec.fit_transform(X.to_dict(orient='record'))


LR=LogisticRegression(solver='liblinear', multi_class='auto')
LR=LR.fit(X_data, Y)

score = cross_val_score(LR,X_data,Y,cv=10).mean()#使用交叉验证
print(score)  #LR


x_test=pd.read_csv('./test.csv')
test_data=x_test.drop(["EmployeeNumber",'Over18','user_id'],inplace=False,axis=1)
dv_test=DictVectorizer(sparse=False)
test_data=dv_test.fit_transform(test_data.to_dict(orient='record'))



predict_lr_p=LR.predict_proba(test_data)
y_lr=pd.DataFrame(predict_lr_p[:,1],columns=['Attrition'])
y_lr=y_lr.set_index(x_test['user_id'])
#print(x_test['user_id'])
y_lr.to_csv('L1_action2_kaggle_final.csv')



