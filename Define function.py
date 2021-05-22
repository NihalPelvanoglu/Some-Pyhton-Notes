# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:04:09 2020

@author: nihal
"""
import numpy as np
import pandas as pd


def my_function():
  print("Hello from a function")
my_function()  
  
def my_function(n):
    print("Hello", n)
    print(n)
my_function(3)     
    
def my_function_with_args(name, university):
    print("Hello, my name is " + name + " from "+ university)
my_function_with_args("Nihal PELVANOĞLU", "YTÜ")



def sum_two_numbers(a, b):
    return a + b
print(sum_two_numbers(5,3))


def sum_of_squares(a, b):
 eval(input("Enter a and b:"))
 print(a**2 + b**2)
sum_of_squares(3, 5)



def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)




x = 15
def my_function(): 
    x=15 
    x = x + 5 
    print("The new value is now "+ str(x)) 
my_function() 
print(x)

def my_function(): 
    global x  # Xİ İÇERİ VE DIŞARI TAŞIYOR
    x = x + 5 
    print("The new value is now "+ str(x)) 
my_function() 
print(x)


def median(a,b,c):
    if a<b and b<c or a>b and b>c:
        return b
    if b<a and a<c or b>a and a>c:
        return a
    if c<a and b<c or a>c and b>c:
        return c

print(median(3,8,15))


def main():
    a=float(input("Enter a"))
    b=float(input("Enter b"))
    c=float(input("Enter c"))

    def median(a,b,c):
        if a<b and b<c or a>b and b>c:
            return b
        if b<a and a<c or b>a and a>c:
            return a
        if c<a and b<c or a>c and b>c:
            return c
    print(median(a,b,c))
    result=median(a,b,c)

main()


