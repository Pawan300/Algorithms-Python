# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 13:06:22 2018

@author: curaj
"""
import numpy as np
def calculate(f,a):
    f=f.replace("x",str(a))
    return(eval(f))
    
def bisection(f,a,b):
   if(calculate(f,a)*calculate(f,b)<0):
       m=(a+b)/2
       while((b-a)>0.01):
           if(calculate(f,a)*calculate(f,m)<0):
               b=m
           else:
               a=m
           m=(a+b)/2
       return(m)
   else:
       return("No roots")
     
def regular_falsi(f,a,b):
    if(calculate(f,a)*calculate(f,b)<0):
        c=(a*calculate(f,b)-b*calculate(f,a))/(calculate(f,b)-calculate(f,a))
        while((b-a)>=0.01 and  a!=c):
            if(calculate(f,a)*calculate(f,c)<=0):
                b=c
            else:
                a=c
            c=(a*calculate(f,b)-b*calculate(f,a))/(calculate(f,b)-calculate(f,a))
        return(c)
    else:
        return("No roots ")

def secant(f,a,b):
    while(abs(b-a)>0.000001):
        mid=b-(((a-b)*calculate(f,b))/(calculate(f,a)-calculate(f,b)))
        a=b
        b=mid
    return(b)

def derivative():
        p=np.poly1d([1,2,3,0,5,6])
        q=p.deriv()
        print(p)
        print(q)