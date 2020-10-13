def isprime(n):
  flag=True
  i=2
  while(i<=n/2):
    if(n%i==0):
      flag=False
      break
    i=i+1
  return (flag)
def sumprimes(l):
  sum=0
  for i in l:
    if(i>0):
        if(isprime(i)):
          sum=sum+i
  return (sum)
print(sumprimes([-3,-5,3,5]))