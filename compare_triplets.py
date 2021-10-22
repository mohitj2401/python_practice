def compareTriplets(a, b):
    ac=0
    bob=0
    for x in range(0,3):
        if(a[x]>b[x]):
            ac=ac+1
        if(a[x]==b[x]):
            continue
        if(a[x]<b[x]):
            bob=bob+1
            
    a=[ac,bob]
    return a
