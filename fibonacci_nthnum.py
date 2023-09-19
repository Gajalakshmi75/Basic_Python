# -*- coding: utf-8 -*-
"""
Created on Wed May 11 20:04:03 2022

@author: Gaja Lakshmi
"""

#prograam to find nth fibonacci number
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter the number:"))
print("nTh fibonacci number is:",fib(n))