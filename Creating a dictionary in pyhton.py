# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:49:22 2020

@author: nihal
"""
English = ["Pen", "Table", "Wallet", "Bottle", "Book", "Guitar", "Selfie Stick"]
print(English)

Turkish = ["Kalem", "Masa", "Cüzdan", "Şişe", "Kitap", "Gitar", "Özçekim Çubuğu"]
print(Turkish)

Price = [5, 150, 45, 15, 30, 400, 20]
print(Price)

eng_to_tur = {"Pen":"Kalem", "Table":"Masa", "Wallet":"Cüzdan", "Bottle":"Şişe", "Book":"Kitap", "Guitar":"Gitar" }
print(eng_to_tur) # kırlangıçla birlikte sözlük oluşturulur.

eng_to_tur = dict(zip(English, Turkish))
print(eng_to_tur) # verilen iki listeyi birleştirip sözlük oluştur.

print(eng_to_tur.keys()) # bütün verileri verir.
print(eng_to_tur.values()) # bütün değerleri verir.

eng_to_tur["Selfie Stick"] = "Özçekim Çubuğu" # yeni bir sözlük eklemek için basit bir atama yapılır.
eng_to_tur["Rear Gear"] = "Geri Vites"
print(eng_to_tur)

del eng_to_tur["Rear Gear"] # istenilen veriyi siler.
print(eng_to_tur)

eng_to_tur = { 'Pen': { 
            'Turkish':'Kalem', 
            'Price':5 
          },
           'Table': { 
           'Turkish':'Masa', 
           'Price':150}} # içe içe sözlük atar. 



