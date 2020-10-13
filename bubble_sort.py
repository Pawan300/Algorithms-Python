# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n=[5,87,98,1,1,1,0,78,98,56,9 ,987,87,3,2,1,1]
for i in range(0,len(n)):
    for j in range(0,len(n)-1):
        if n[j]>n[j+1] :
            n[j],n[j+1]=n[j+1],n[j]
        

print("now sorted array is :",n)      