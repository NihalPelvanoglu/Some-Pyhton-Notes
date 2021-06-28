# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:43:42 2020

@author: nihal
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)
spread = np.random.rand(50) * 100 #○verinin genişliği

center = np.ones(25) * 50 #verinin medyanı

flier_high = np.random.rand(10) * 100 + 100 #verideki en yüksek değer

flier_low = np.random.rand(10) * -100 #verideki en düşük değer

data = np.concatenate((spread, center, flier_high, flier_low))

fig1, ax1 = plt.subplots()

ax1.set_title('Basic BoxPlot')

ax1.boxplot(data, vert=True, showfliers=True)

plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a=np.random.rand(10, 5)
print(a)

data = pd.DataFrame(a, columns=['A', 'B', 'C', 'D', 'E'])
print(data)

data.plot.box(grid='True') #
plt.show()



