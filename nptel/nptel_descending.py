def descending(l):
  flag=True
  for i in range(1,len(l)):
    if(l[i]>l[i-1]):
      flag=False
      break
  return (flag)