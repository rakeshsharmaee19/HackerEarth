for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    res = {2:[], 1:[], 4:[]}
    for i in arr:
        if i&1==0:
            if i%4 == 0:
                res[4].append(i)
                res[2].append(i)
            else:
                res[2].append(i)
        else:
            res[1].append(i)
            
    while len(res[2])<n and res[4]:
        nm = res[1].pop()
        mmf = res[4].pop()
        res[2].append(nm*2)
        res[2].remove(mmf)
        if (mmf>>2)%4==0:
            res[2].append(mmf>>2)
            res[4].append(mmf>>2)
        else:
            res[2].append(mmf>>2)
    if len(res[2])>=n:
        print('YES')
    else:
        print('NO')
