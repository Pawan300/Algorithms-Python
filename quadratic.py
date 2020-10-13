flag=0
def demo(j):
    for i in range(0,32):
        for k in range(0,32):
            if((i**2+k**2)==j):
                return j
    return 0
for i in range(100,999):
    r=demo(i)
    if(r==i):
        for j in range(i+1,i+3):
            r1=demo(j)
            if(r1==0):
                flag=1
                break
            else:
                flag=0
    if(flag==0):
        print(i,i+1,i+2)
    else:
        continue