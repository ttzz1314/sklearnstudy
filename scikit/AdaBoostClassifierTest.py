#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_gaussian_quantiles

# 生成2维正态分布，生成的数据按分位数分为两类，500个样本,2个样本特征，协方差系数为2
X1, y1 = make_gaussian_quantiles(cov=2.0,n_samples=500, n_features=2,n_classes=2, random_state=1)
# 生成2维正态分布，生成的数据按分位数分为两类，400个样本,2个样本特征均值都为3，协方差系数为2
X2, y2 = make_gaussian_quantiles(mean=(3, 3), cov=1.5,n_samples=400, n_features=2, n_classes=2, random_state=1)
#讲两组数据合成一组数据
X = np.concatenate((X1, X2))
y = np.concatenate((y1, - y2 + 1))

plt.scatter(X[:, 0], X[:, 1], marker='o', c=y)
bdt = GradientBoostingClassifier(GradientBoostingClassifier(max_depth=2, min_samples_split=20, min_samples_leaf=5),
                         max_features='sqrt',loss='deviance',
                         n_estimators=200, learning_rate=0.8)
bdt.fit(X, y)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

Z = bdt.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
cs = plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
plt.scatter(X[:, 0], X[:, 1], marker='o', c=y)
plt.show()

print("Score:", bdt.score(X,y))
#也就是说拟合训练集数据的分数还不错。当然分数高并不一定好，因为可能过拟合。现在我们将最大弱分离器
# 个数从200增加到300。再来看看拟合分数。

bdt = GradientBoostingClassifier(DecisionTreeClassifier(max_depth=2, min_samples_split=20, min_samples_leaf=5),
                         max_features='sqrt',loss='deviance',
                         n_estimators=300, learning_rate=0.8)
bdt.fit(X, y)
print("Score:", bdt.score(X,y))

#这印证了我们前面讲的，弱分离器个数越多，则拟合程度越好，当然也越容易过拟合。现在我们降低步长，
# 将步长从上面的0.8减少到0.5，再来看看拟合分数。
bdt = GradientBoostingClassifier(DecisionTreeClassifier(max_depth=2, min_samples_split=20, min_samples_leaf=5),
                         max_features='sqrt',loss='deviance',
                         n_estimators=300, learning_rate=0.5)
bdt.fit(X, y)
print("Score:", bdt.score(X,y))

#可见在同样的弱分类器的个数情况下，如果减少步长，拟合效果会下降。最后我们看看当弱分类器个
# 数为700，步长为0.7时候的情况：
bdt = GradientBoostingClassifier(DecisionTreeClassifier(max_depth=2, min_samples_split=20, min_samples_leaf=5),
                         max_features='sqrt',loss='deviance',
                         n_estimators=700, learning_rate=0.7)
bdt.fit(X, y)
print("Score:", bdt.score(X,y))

#此时的拟合分数和我们最初的300弱分类器，0.8步长的拟合程度相当。也就是说，在我们这个例子中，
# 如果步长从0.8降到0.7，则弱分类器个数要从300增加到700才能达到类似的拟合效果。