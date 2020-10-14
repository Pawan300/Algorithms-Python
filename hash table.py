def seperate_chaining(l,m):
    result=[" "]*(m)
    for i in range(m):
        result[i]=[]
    for i in l:
           result[(i%m)].append(i)
    return(result)
def search_sc(l,m,ele):
    n=ele % m
    if(ele in l[n]):
        return("element found in script : ",n)
    else:
        return("element not found ")
def remove_sc(l,ele):
    m=ele%len(l)
    l[m].remove(ele)
    return(l)

           
def linear_probing(l):
    result=[None]*(len(l))
    for i in l:
        flag=True
        m=i%len(l)
        while(flag):
             if(result[m]==None):
                 result[m]=i
                 flag=False
             elif(m<len(l)-1):
                 m=m+1
             else:
                 m=0
    return(result)
def quadratic_probing(l):
    result=[None]*(len(l))
    for i in l:
        m=i%len(l)
        t=m
        flag=True
        j=1
        while(flag):
            if(result[t]==None):
                result[t]=i
                flag=False
            else:
                m=m+j**2
                t=m%len(l)
                j=j+1
                if(j>20):
                    return("Quadratic probing is not possible!!!!!!!!!!!!")
    return(result)
def double_hasing(l):
    result=[None]*len(l)
    for i in l:
        m=i%len(l)
        flag=True
        j=1
        while(flag):
            if(result[m]==None):
                result[m]=i
                flag=False
            else:
                t=i%5+1
                m=(m+j*t)%len(l)
                j=j+1
                if(j>20):
                    return(result)
    return(result)
def search_dh(l,ele):
    m=ele%len(l)
    flag=True
    j=1
    while(flag):
        if(l[m]==ele):
           return(m+1)
        else:
            t=i%5+1
            m=(m+j*t)%len(l)
            j=j+1
            if(j>20):
                return("not found")
def delete_dh(l,pos):
    t.remove(t[pos-1])
    return(t)   