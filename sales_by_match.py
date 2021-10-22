#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ls=[]
    count=0
    for x in range(n):
        if(ar[x] in ls):
            
            continue
        else:
           cnt= ar.count(ar[x])
           
           count=count+int(cnt/2)
           ls.append(ar[x])
           
    return count
           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
