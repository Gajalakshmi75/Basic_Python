# -*- coding: utf-8 -*-
"""
Created on Wed May 11 20:37:37 2022

@author: Gaja Lakshmi
"""

n=int(input("enter the number of terms needed in fibonacci series:"))
f1,f2=0,1
if n==1:
    print(f1)
elif n==2:
    print(f1,' ',f1)
else:
    print(f1,f2,end=' ')
    for i in range(3,n+1):
        f3=f1+f2
        print(f3,end=' ')
        f1=f2
        f2=f3