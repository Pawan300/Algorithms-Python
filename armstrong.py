n=int(input('enter a number'))
a=list(str(n))
print(a)
sum=0
for x in a:
    x=int(x)
    if(len(a)==3):
        sum+=x**3
    else:
        print("invalid number")
if(sum==n):
    print("armstrong number")
else:
    print("no")