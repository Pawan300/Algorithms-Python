def transpose1(l):
 result = [[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]
 return (result)
def transpose2(l):
    t=[]
    for i in range(len(l[0])):
        demo=[]
        for j in range(len(l)):
               demo=demo+[l[j][i]]
        t=t+[demo]
    return (t)
print(transpose1([[16,31,99],[4,5,6]]))
print(transpose2([[16],[7],[8]]))
