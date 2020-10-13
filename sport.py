import random
x=[1,2,3,4,6]
y=['S','P','O','R','T']
run=[0]*10
out=0
outtype=["Run out","Bowled","L.B.W","Caught out","Caught & Bowled","Stumps","Hitwicket"]
i=0
while(i<3):
   out=0
   while(out==0):
        num=input("Enter from keywords S,P,O,R,T : ")
        num=num.upper()
        if(num not in y):
            continue
        ball=random.randint(0,4)
        print(ball)
        if(y[ball]==num):
            out=1
            if(num=="P" or num=="R"):
                print(outtype[0])
            elif(num=="T"):
                temp=random.choice(outtype)
                if(temp != outtype[0]):
                  print(temp)
            else:
                print(random.choice(outtype))
            print("YOUR SCORE IS : ",run[i])
            i=i+1
        else:
            run[i]+=x[y.index(num)]
            print("SCORE :",run[i])   
sum=0
for i in run:
    sum+=i
print("Score of team is : ",sum)
print("Score card is : ",run)