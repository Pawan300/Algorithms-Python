import re
import numpy as np
def create_matrix(st1,st2):
    lcs=np.zeros((len(st1)+1,len(st2)+1))
    for i in range(len(st1)+1):
        for j in range(len(st2)+1):
            if(i==0 or j==0):
                continue
            elif(st1[i-1]==st2[j-1]):
                lcs[i][j]=lcs[i-1][j-1]+1
            else:
                lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
    return(lcs)
def backtrack(mat,s1,s2):
    s=""
    i=len(s1)
    j=len(s2)
    while(i>0 and j>0):
            if(s1[i-1]==s2[j-1]):
                s+=s1[i-1]
                i=i-1
                j=j-1
            else:
                if(mat[i-1][j]>mat[i][j-1]):
                    i=i-1
                else:
                    j=j-1
    return(s)

def lcs(st1, st2):
    s =""
    st1=re.sub(" ",'',st1)
    st2=re.sub(" ",'',st2)
    mat=create_matrix(st1,st2)
    s=backtrack(mat,st1,st2)
    return s[::-1]

