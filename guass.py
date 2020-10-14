import numpy as np
from scipy import linalg
def test(A,b,sol):
    sol=np.reshape(sol,(4,1))
    er=linalg.norm(A.dot(sol)-b)
    return(er)
def swap(i,m,matrix):
    for j in range(0,5):
       matrix[m,j],matrix[i,j]=matrix[i,j],matrix[m,j]  
     
def checkzero(m):
        for i in range(m+1,4):
            if(augmat[i][m]!=0):
                swap(i,m,augmat)
                break;
def checkinvertible(matrix):
    m=np.linalg.det(matrix)   ## for calculate determinant of matrix
    if(m==0):
        return (False)
    else:
        return (True)
def equation(m):
    x=[0]*m
    for i in range(m-1,-1,-1):
       j=m-1
       temp=0
       while(j>0):
           temp+=augmat[i][j]*x[j]
           j=j-1
       x[i]=(augmat[i][m]-temp)/augmat[i][i]
    return x
def pivot(j):
    d={}
    for i in range(4):
        row_max=max(abs(augmat_pivot[i]))
        if (row_max==0):
            sys.exit("Not invertible!!!!!!!! ")
        nrm=abs(augmat_pivot[i,j])/row_max
        d.update({nrm:i})
    return (d[max(d.keys())])

def row_operation(m,matrix):
    temp=matrix[m,m]
    for i in range(m+1,4):
        if(matrix[i,m]==0):
            continue
        temp1=matrix[i,m]
        for j in range(0,5):
            matrix[i,j]=matrix[i,j]-temp1/temp*matrix[m,j]
def guass_pivot(m):
    y=[]
    temp=pivot(m)
    swap(m,temp,augmat_pivot)
    row_operation(m,augmat_pivot)
    if(m<3):
        y=guass_pivot(m+1)
        return(y)
    else:
        y=equation(4)
        return (y)
def guass(m):
    y=[]
    if(augmat[m][m]==0):
         checkzero(m)
    temp=augmat[m][m]
    for i in range(0,5):
        augmat[m][i]=augmat[m][i]/temp
    for i in range(m+1,4):
        if(augmat[i][m]==0):
            continue
        temp1=augmat[i][m]
        for j in range(0,5):
            augmat[i][j]=augmat[i][j]-temp1*augmat[m][j]
    if(m<3):
       y= guass(m+1)
       return y
    else:
        y=equation(4)
        return y
x=[[0,1,3,10.0],[4.0,5.0,6.0,11.0],[7.0,8.0,9.0,12.0],[1.0,14.0,15.0,16.0]]
m=np.array(x)
y=[[1.0],[2.0],[3.0],[4.0]]
identity=np.array(y)
augmat=np.hstack((m,identity))
augmat_pivot=np.hstack((m,identity))
if(checkinvertible(m)):
    alpha=guass(0)
    beta=guass_pivot(0)
    print(alpha)
    print(beta)
else:
    print("This matrix is not invertible !!!!!!!!!!!!!")
print(test(m,identity,alpha))