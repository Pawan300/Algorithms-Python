def valley(l):
    x=min(l)
    flagd=True
    flagi=True
    countd=1
    counti=1
    for i in range(0,len(l)) : 
        if(x==l[i]): 
            y=i
    for temp in range(y,0,-1):
        if(l[temp]>=l[temp-1]):
            flagd=False
            break
        countd=countd+1
    for temp in range(y,len(l)-1):
        if(l[temp]>=l[temp+1]):
            flagi=False
            break
        counti=counti+1
    if(counti<2 or countd<2):
        flagd=False
        flagi=False
    return (flagd and flagi)
print(valley([17,1,2,3,4,5]))