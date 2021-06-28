# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:01:29 2020

@author: nihal
"""

import matplotlib.pyplot as plt

labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

explode = (0.1, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%')

plt.axis('equal')

plt.title('Programming Languages')

plt.legend(labels)

plt.show()
