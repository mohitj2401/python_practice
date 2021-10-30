
def getTotalX(a, b):
    # Write your code here
    total = 0
    for i in range(max(a), min(b)+1):
        if all(i % j == 0 for j in a) and all(j % i == 0 for j in b):
            total += 1
    return total


a = [2, 4]
b = [16, 32, 96]
print(getTotalX(a, b))
