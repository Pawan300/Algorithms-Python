import numpy as np
def swap(i,m):
    for j in range(0,5):
       augmat[m][j],augmat[i][j]=augmat[i][j],augmat[m][j]
def checkzero(m):
        for i in range(m+1,4):
            if(augmat[i][m]!=0):
                swap(i,m)
                break;
def checkinvertible(matrix):
    m=np.linalg.det(matrix)   ## for calculate determinant of matrix
    if(m==0):
        return (False)
    else:
        return (True)
def equation():
    x=[0]*4
    k=0
    temp=0
    for i in range(3,-1,-1):
          temp=0
          j=3
          while(j>0):
                  temp+=augmat[i][j]*x[j]
                  j=j-1
          x[i]=(augmat[i][4]-temp)/augmat[i][i]
 
    print(x)
def guass(m):
    if(augmat[m][m]==0):
         checkzero(m)
    temp=augmat[m][m]
    for i in range(m+1,4):
        if(augmat[i][m]==0):
            continue
        temp1=augmat[i][m]
        for j in range(0,5):
            augmat[i][j]=augmat[i][j]-temp1/temp*augmat[m][j]
    if(m<3):
        guass(m+1)
    else:
        equation()
x=[[0,1.0,3.0,10.0],[4.0,5.0,6.0,11.0],[7.0,8.0,9.0,12.0],[13.0,14.0,15.0,16.0]]
m=np.array(x)
y=[[1.0],[2.0],[3.0],[4.0]]
identity=np.array(y)
augmat=np.hstack((m,identity))
print(augmat)
if(checkinvertible(m)):
    guass(0)
else:
    print("This matrix is not invertible !!!!!!!!!!!!!")