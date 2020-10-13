sum=0
for i in range(100,999):
    sum=0
    for j in range(1,i-1):
        if (i%j==0):
            sum=sum+j
    if(sum==i):
        print(i)