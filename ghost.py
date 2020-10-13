# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:52:22 2018

@author: pawan_300
"""

def ghost(n,l):
    d={}
    for i in range(n):
       key=d.keys()
       if(l[i] in key):
           d[l[i]]=d[l[i]]+1 
       else:        
           d.update({l[i]:1})
       m=max(d.values())
       a=[]
       for i in key:
           if(d[i]==m):
               a.append(i)
       de=max(a)
       print(de," ",d[de])