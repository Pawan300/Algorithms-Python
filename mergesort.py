def merge(arr,start,middle,end):
    i=0
    j=0
    k=start
    nl=int(middle-start+1)
    nr=int(end-middle)
    l=[0]*nl
    r=[0]*nr
    for i in range(0,nl):
        l[i]=arr[i+start]
    for j in range(0,nr):
        r[j]=arr[j+middle+1]
   
    while i<nl and j<nr:
        if l[i]<=r[j]:
            arr[k]=l[i]
            i=i+1
        else:
            arr[k]=r[j]
            j=j+1
        k=k+1
    while(j<nr):
        arr[k]=r[j]
        j=j+1
        k=k+1
    while(i<nl):
        arr[k]=l[i]
        i=i+1
        k=k+1
            
def merge_sort(arr,start,end):
    if(start<end):
      middle=int((start+(end-1))/2)
      merge_sort(arr,start,middle)
      merge_sort(arr,middle+1,end)
      merge(arr,start,middle,end)
    
arr = [1,9,90,34,45,2, 5, 6,27, 7, 2 , 6]
n = len(arr)
print ("Given array is")
for i in range(n):
    print (arr[i],end=" ")
merge_sort(arr,0,n-1)
print("\nsorted array is : ")
print(arr)