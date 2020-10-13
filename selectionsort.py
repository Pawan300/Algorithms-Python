#selection sort 
l=[56,34,2,7,89,0,4,56,23,14]

for i in range(0,len(l)):
    t=l[i]
    for j in range(i+1,len(l)):
        if(t>l[j]):
            t,l[j]=l[j],t
    l[i]=t
print(l)