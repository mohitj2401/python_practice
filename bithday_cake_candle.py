def birthdayCakeCandles(candles):
    count=0
    m=max(candles)
    for x in candles:
        if(x==m):
            count=count+1
    return count
