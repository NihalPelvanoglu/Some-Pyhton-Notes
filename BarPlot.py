# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:38:35 2020

@author: nihal
"""

import matplotlib.pyplot as plt
names = ['Sayı 1', 'Sayı 2', 'Sayı 3']
values = [10, 20, 150]
plt.subplot(141) # sütunun genişiliği büyüklüğü .
plt.bar(names, values)

plt.subplot(142)
plt.scatter(names, values) 

plt.subplot(143)
plt.plot(names, values)

plt.subplot(144)
plt.plot(names, values, 'g^')


plt.show()

