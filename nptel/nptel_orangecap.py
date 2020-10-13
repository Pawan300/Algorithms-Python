def orangecap(d):
    max=0
    name=""
    t={}
    for i in d.keys():
        for j in d[i].keys():
            if j in t.keys():
                t[j]+=d[i][j]
            else:
                t.update({j:d[i][j]})
    for i in t:
            if(t[i]>max):
                max=t[i]
                name=i
    return (name,max)
print(orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}))