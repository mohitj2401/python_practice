arr = [5, 4, 4, 2, 2, 8]
lt = []
count = 0
min_val = min(arr)
while (min_val != 0):
    length = len(arr)
    for x in range(length):
        arr[x] = arr[x]-min_val
        if(arr[x] > 0):
            count = count + 1
    for x in range(arr.count(0)):
        arr.remove(0)
    if count != 0:
        lt.append(count)
    if (len(arr) > 0):
        min_val = min(arr)
    else:
        break
    count = 0

return (lt.insert(0, len(arr)))
