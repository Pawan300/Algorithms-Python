from itertools import combinations
import math
f=[]  #FACOTRS ELEMENTS
a=[]  #NON FACTORS ELEMENT
j=2
perm=[]
flag1=0
def factor(num):
    f=[]  
    for i in range(1,num):   #for factors
        if(num%i==0):
            f=f+[i]
    return f
num=int(input("Enter number : "))
f=factor(num)
a=[i for i in range(1,num)]
a=set(a)-set(f)         
a=list(a)      #for non factors
flag=[0]*len(a)
while(j<=len(f)):
   t=list(combinations(f,j))
   perm.append(t)
   j=j+1
for i in range(0,len(a)):
   for demo in range(2,len(f)+1):
        length=int(math.factorial(len(f))/((math.factorial(demo))*math.factorial(len(f)-demo)))
        for it  in range(0,len(perm)):
          d=perm[it]         
          for x in d:
              sum=0
              for y in x:
                  sum+=y
              if(sum==a[i]):
                  flag[i]=1
                  break
for j in range(0,len(a)):
    if(flag[j]==0):
        flag1=1
        print("This number is not a practical number ")
        break;
if(flag1==0):
    print("This number is a practical number ")
