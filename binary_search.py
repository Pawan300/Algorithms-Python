def binary_srch(arr,num):
 start=0
 end=len(arr)-1
 while(start<=end):
     mid=int((start+end)/2)
     if num==arr[mid]:
         return mid
     elif num<=arr[mid]:
         end=mid-1
     else:
         start=mid+1
 return (-1)
arr = [1, 2, 2, 5, 6, 6, 7, 9, 45, 90, 243, 340]
num=5
n=binary_srch(arr,num)
if(n!=-1):
    print(n+1)
else:
    print("not found")