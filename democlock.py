from time import clock
sum=0
start=clock()
for i in range(0,100000000):
    sum+=i
t=clock()-start
print(t,"     ",sum)