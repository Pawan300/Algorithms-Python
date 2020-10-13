arr=[44,56,32,2,3,6,66,88,9,66,54,77,3,2,33,2,4]
def swap(i,j):
    arr[i],arr[j]=arr[j],arr[i]
def heapify(i,end):
    l=2*i+1
    r=2*i+2
    max=i
    if(l<end and arr[l]>arr[i]):
        max=l
    if(r<end and arr[max]<arr[r]):
        max=r
    if(max!=i):
        swap(max,i)
        heapify(max,end)
def heapsort(arr):
    end=len(arr)
    start=end//2-1
    for i in range(start,-1,-1):
        heapify(i,end)
    for j in range(end-1,0,-1):
        swap(j,0)
        heapify(0,j)
heapsort(arr)
print(arr)