# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 23:16:45 2020

@author: nihal
"""

# LISTS
import numpy as np

x = [] # liste oluşturmak için köşeli parantezle tanımlamak gerekir.
print(type(x)) 

x = [1,2,3,4, 'n'] # listedeki her bir elaman arasında virgül koyulur. String datalar tırnak işareti içerisinde yazılır.
print(x)

x = np.linspace(0,10,11) # Farklı bir liste oluşturma yöntemidir.
print(x)                 #listenin ilk elemanı, son elemanı ve kaç aralık olması gerektiği yazılır.


x = np.arange(0,11,1) # listenin ilk elemanı son elemanından !!! bir fazlası !!! ve kaçar kaçar artması gerektiği yazılır.
print(x)

y = np.arange(4) # 0 dan başlayarak belirtilen aralığa kadar sıralar.
print(y)


# SLICING LISTS

x = [0,1,2,3,4,5,6,7,8,9]
print(x[0]) # köşeli parantez içerisinde belirtilen indisteki elemanı verir.

print(x[4:]) # 4.elemandan başlayarak liste elemanlarını verir.

# MANIPULATING LISTS

x = [1,2,3,4]
print(x)

x[3] = 4.8 #X  x'in 3üncü elemanınının yerine yeni bir eleman atar.
print(x)

x = x + [10, 11] # yeni bir eleman ekler.
print(x)

# LIST FUNCTION 

x = [0,1,2,3,4,5,6,7,8,9]
print(x)

x.append(0) # append komutu x e yeni bir eleman ekler. 
print(x)    #Sadece tek eleman ekliceğimiz koşullarda geçerlidir.

print(len(x)) # dizinin uzunluğunu verir.

x.extend([11,12,13]) # extend komutu x e yeni birden fazla eleman ekliceğimiz koşullarda kullanılır.
print(x) 

x.pop(1)
print(x) # pop komutu belirtilen elemanı siler. 

x.remove(0) # beliritilen sıradaki elemanı siler.,
print(x)    


x = [0,1,2,3,4,5,6,7,8,9]
del x[0] # belirtilen  elamanı siler. 
print(x) 


del x[:3] # belirtilen aralıktaki elemanları siler.
print(x)

del x[:] # bütün elemanları siler.
print(x) 

