jail=[]
for i in range(1,101):
    if(i==1):
        jail=[0]*100   #open 
    else:
        j=i
        k=i-1
        while(j<=100):
            if(jail[k]==0):
                jail[k]=1   #close
            else:
                jail[k]=0
            j=j+i
            k=k+i
print("These cell are locked  : ")
for i in range(0,100):
    if(jail[i]==1):
        print(i+1,end=" ")
print("\nThese cells are not locked : ")
for i in range(0,100):
    if(jail[i]==0):
        print(i+1,end=" ")