# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 23:36:26 2020

@author: nihal
"""

import numpy as np

a = np.array([1, 2, 3]) # matris oluşturur.   
                 
A = np.array([[1, 2, 3], [3, 4, 5]], dtype = complex)  
print(A) # dtype = veriyi istediğimiz hale getirir.

from numpy import array # bir paketten tek fonksiyon çekmye yarar.

a = np.random.randint(1,5,(2,5)) # random olarak 1 den 5 e kadar atadığı verileri 2 ye 5lik matris yapar.

x= np.zeros((2, 3)) # 2 satırlı 3 sütünlü sıfır matris verir. ! iki parantezle kullanılır.
                    # önce satır, sonra sütun
                    
print('A = ', A) # matrise isim verir.


B = np.arange(12).reshape(2, 6) # reshape kaça kaçlık oluşturcağını belirtir. matrisi nasıl şekilledirceğimizi belirttik.

print(np.append(a,10)) # matrisin sonuna eleman ekler.

a = np.array([1, 2, 3])
print(np.insert(a, 2, 5)) # 2. kısım eklenmek istenilen indis yeri, 3. kısım eklenmek istenilen verir.

a = np.array([1, 2, 3])
print(np.delete(a,2)) # belirtilen indisteki veriyi siler.


b = a+[5, 6, 7] # iki materisi topladı.
print(b)

b = a*[5, 6, 7] # iki materisi çarptı.
print(b)

c = np.dot(a,b) # iki matrisi çarpar.
print(c)

a = np.repeat(5,3) # ilk sayıdan kaç tekrar olcak.
print(a)

a = np.repeat(a, 4, axis=1) #satır yönünde her bir elemanı kaçar tane yazdırcağını gösterir.
print(a)

print(np.repeat(a, 4, axis=0)) #sütun yönünde elemanı kaçar tane yazdırcağını gösterir.

a = np.repeat(a, [1,3], axis=0) # ilk indis birinci satırı, ikinci indis ikinci satırı kaç kere tekrar ettirceğini gösterir.
print(a)

a = np.repeat(a, [2, 3], axis=1) # birinci sütündan 2 tane, 2. sütündan 3 tane
print(a)

N = np.identity(3) # 3 e 3 lük birim matris oluşturur.
print(N)

n=np.sin(N) # sayıların sinüsüyle yeni matris oluşturur.
np.logh(10) # logaritma verir.

A = np.array([[1, 0, 2], [2, -1, 3], [4, 1, 8]])
inverse = np.linalg.inv(A) # tersini verir.
print(inverse) 

A = np.array([[2, 4, 0], [1, 3, 2]])
print(A.transpose()) # transpozunu verir.
print(A.T)





