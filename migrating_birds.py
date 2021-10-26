def migratoryBirds(arr):
    lt=[]
    for x in range(5):
        lt.insert(x,0)
        for y in arr:
            if(y==(x+1)):
                lt[x]=lt[x]+1

    return lt.index(max(lt))+1