import numpy as np
n = input()
arr = list(map(int, input().split()))

for _ in range(int(input())):
    q = int(input())
    itr = iter(arr)
    ch = True
    sm= 0
    count = 0
    while ch:
        try:
            sm+=next(itr)
            count+=1
            if sm>=q:
                ch=False
        except:
            count = -1
            ch =False
    print(count)
            
