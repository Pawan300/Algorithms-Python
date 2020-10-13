# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 20:53:04 2018

@author: pawan_300
"""
from time import clock
num=eval(input("Enter the number upto you want to print prime number : "))
start=clock()
if(num>=2):
 c=0
 count=0
 for i in range(2,num+1):
    for j in range(2,i):
        if(i%j==0):
            c=1
            break
        else:
            c=0
    if(c==0):
     print(i," ")
     count=count+1 
 print("Total number of prime number under ",num," is : ",count)
else:  
 print("Please enter number greater than or equals to 1 !!!!!!!!!!!!!!!!")      
t=clock()-start
print (t)