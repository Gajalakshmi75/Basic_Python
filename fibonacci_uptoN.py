# -*- coding: utf-8 -*-
"""
Created on Wed May 11 20:17:08 2022

@author: Gaja Lakshmi
"""

#program display fibonacci numbers up to N
n=int(input("enter the number:"))
f1=0
f2=1
print(f1,end=' ')
print(f2,end=' ')
f3=f1+f2
while(f3<=n):
    print(f3,end=' ')
    f1=f2
    f2=f3
    f3=f1+f2