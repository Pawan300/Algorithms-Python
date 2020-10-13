def partition(arr,start,end):
    i=0
    pivot=arr[end]
    p=start
    for i in range(start,end):
        if(arr[i]<=pivot):
          arr[i],arr[p]=arr[p],arr[i]
          p+=1
    arr[p],arr[end]=arr[end],arr[p]
    return (p)
def quicksort(arr,start,end):
    if(start<end):
        r=partition(arr,start,end)
        quicksort(arr,start,r-1)
        quicksort(arr,r+1,end)
arr = [1,9,90,340,45,2, 5, 6,243, 7, 2 , 6]
print("Unsorted array is : ",arr)
quicksort(arr,0,len(arr)-1)
print(arr)