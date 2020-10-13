date=[]
d1=[]
d=[]
t={}
l1=[]
month={"01":"Januaury",
           "02":"Febuary",
           "03":"March",
           "04":"April",
           "05":"May",
           "06":"June",
           "07":"July",
           "08":"August",
           "09":"September",
           "10":"October",
           "11":"November",
           "12":"December"
           }
print("\tRULES : \n1.DAY (1-31) \n2.MONTH(1-12) ")
for i in range(0,20):
    d=input("Enter date :  ")   #For enter date 
    date=date+[d]
    
date_distinct=set(date)
d1=list(date_distinct)
print("distinct dates are : ")  #For distinct date
print(date_distinct)

for j in range(0,len(d1)):
    d=d1[j].split("/")         #For print date with month name
    if((d[1] in month)&(int(d[0]) in range(1,31))):
        print(d[0],month[d[1]],d[2],end=" : ")
        temp=input("Enter temperature for date : ")
        l1=l1+[temp]
    else:
        l1=l1+["error"]
t=dict(zip(d1,l1))
print(t)
