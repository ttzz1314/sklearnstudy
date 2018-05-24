#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

d = {'col1': ['a','a','a','b','b','c'], 'col2': [2,2,2,2,2,1],'col3':['c','c','c','d','d','e']}
df = pd.DataFrame(data=d)
newdf = pd.melt(df,id_vars=['col2'])
print(df)
print(newdf)


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


t1 = np.arange(0, 5, 0.1)
t2 = np.arange(0, 5, 0.02)

plt.figure(12)
plt.subplot(221)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'r--')

plt.subplot(222)
plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')

plt.subplot(212)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

plt.show()

plt.show()

