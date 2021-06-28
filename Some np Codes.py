# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
pop = [15.068, 5.504, 4.321, 2.995, 2.426]
print(max(pop))
print(min(pop))
print(sum(pop))
print(round(1.68, 0))
help(round) #yuvarlama 1 ve 0 yazarsak virgülden sonraki basamağa göre yuvarlar.
pop_incr = sorted(pop) # küçükten büyüğe sıralar.
print(pop_incr)
help(sorted)

pop_decr = sorted(pop, reverse = True) # terse çevirerek büyükten küçüğe sıralar.
print(pop_decr)
help(len)
print(len(pop))
print(sum(pop))
print(sum(pop)/len(pop))
import numpy as np
help(np.prod)
print(np.prod(pop)) #çarpım 
x = np.linspace(2,25,47)
print(x)
print(sum(x))
x = np.arange(2,26,0.5) # alt sınır dahil üst sınır dahil değil
print(x)
np.random.seed(100) # standart normal dağılımdan yapay rassal sayılar çeker.#yapay rassal sayılar seed e göre belirli üretilir.
x = np.random.randn(10) # kaç sayı üreticeğini gösterir.
print(x)
print(np.floor(x)) # alt sayıya yuvarlar.
print(np.ceil(x)) # üst sayıya yuvarlar.
print(np.exp(x)) # sayıları e üzei olarak yazdırır.
print(np.log(x)) # logartimasını alır.
print(np.abs(x)) # mutlak değer alır.
print(np.sign(x)) # işaret fonksiyonudur. negative -1 pozitif +1
crowded = ['istanbul', 15.068, ' ankara', 5.504, 'izmir', 4.321, 'bursa', 2.995, 'antalya', 2.426]
print(crowded)
print(crowded.index('istanbul'))
print(crowded.index(2.995))
score = [3, 3, 1, 1, 0, 3, 1, 1, 0, 3]
print(score.count(3)) # kaç 3 var 
score_text = ['w', 'w', 'D', 'D', 'L', 'W', 'D', 'D', 'L', 'W']
print(score_text)
text = 'pyhton is SO cool'
print(text.lower()) # hepsini küçük harf yapar.
print(text.upper()) # hepsini büyük harf yapar.
