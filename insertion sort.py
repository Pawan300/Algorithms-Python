# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 12:38:05 2018

@author: pawan_300
"""
l=[]
def insertion(l,temp):
    for i in range(1,temp):
        lamda=l[i]
        j=i-1
        while((j>=0)&(lamda<l[j])):
            l[j+1]=l[j]
            j=j-1
        l[j+1]=lamda
    print(l)       

temp=int(input("Enter number of digit : "))
for i in range(0,temp):
    t=int(input("Enter numbers: "))
    l.append(t)
print("Unsorted list is : ",l)
insertion(l,temp)
