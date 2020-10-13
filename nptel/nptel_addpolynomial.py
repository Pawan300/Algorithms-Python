def addpoly(p1,p2):
    r=[]
    t=[]
    for i in p1:
        flag=True
        for j in p2:
            if(i[1]==j[1]):
                r.append((i[0]+j[0],i[1]))
                flag=False
        if(flag):
            r.append((i[0],i[1]))
    for i in p2:
        j=0
        flag=True
        while(j<len(r)):
            if(i[1]==r[j][1]):
                flag=False
            j=j+1
        if(flag):
            r.append((i[0],i[1]))
    for i in r:
        if(i[0]!=0):
            t.append(i)
    return (t)
def multipoly(p1,p2):
    r=[]
    t=[]
    for i in p1:
        for j in p2:
            r.append((i[0]*j[0],i[1]+j[1]))
    for i in range(0,len(r)):
        for j in range(i+1,len(r)):
            if(r[i][1]==r[j][1]):
                r[j]=(r[i][0]+r[j][0],r[i][1])
                r[i]=(0,-1)
    for i in r:
        if(i[0]!=0):
           t.append(i)
    return(t)
print(multipoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)]))