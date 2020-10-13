from itertools import combinations
a=[]
f=[]
def p_number(num):
     j=2
     demo=[]
     flag=0
     while(j<=len(f)):
          temp=list(combinations(f,j))
          s=list(map(sum,temp))
          demo.extend(s)
          j=j+1
     for i in range(0,len(a)):
         if(a[i] not in demo):
             flag=1
             break
     if(flag==0):
         print(num,end=" ")
     
def factor(num):
    f=[]  
    for i in range(1,num):   #for factors
        if(num%i==0):
            f=f+[i]
    return f
num=int(input("Enter number upto you want to print practical number  : "))
for j in range(2,num):
    f=factor(j)
    a=[i for i in range(1,j)]
    a=set(a)-set(f)
    a=list(a)                #for non factors elements 
    p_number(j)