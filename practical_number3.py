from itertools import combinations
num=int(input("Enter number : "))
nonfactor=[]
f=[]
def practical_number(num):
     j=2
     demo=[]
     flag=0
     while(j<=len(f)):
          temp=list(combinations(f,j))
          s=list(map(sum,temp))
          demo.extend(s)
          j=j+1
     for i in range(0,len(nonfactor)):
         if(nonfactor[i] not in demo):
             flag=1
             break
     if(flag==0):
         print(num,end=" ")
     
def factor(num):
    factors=[]  
    for i in range(1,num):   #for factors
        if(num%i==0):
            factors=factors+[i]
    return factors
for j in range(2,num):
    f=factor(j)
    nonfactor=[i for i in range(1,j)]
    nonfactor=set(nonfactor)-set(f)
    nonfactor=list(nonfactor)                #for non factors elements 
    practical_number(j)