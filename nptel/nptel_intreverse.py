import math
def intreverse(num):
  x=num
  count=0
  while(x>0):
      x=int(x/10)
      count=count+1 
  y=0
  count=count-1
  while(num>1):
    x=int(num%10)
    num=num/10
    y=y+x*math.pow(10,count)
    count=count-1
  print(int(y))
intreverse(368)