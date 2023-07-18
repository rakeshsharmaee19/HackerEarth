for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    arr = sorted(ar)
    res = 'YES'
    while len(arr)>2:
        a = arr[-2]-(arr[-1]-arr[-2])
        b = arr[-1]-arr[-2]
        if a in set(arr[:-2]) and b in set(arr[:-2]):
            ar.remove(a)
            ar.remove(arr[-1])
            arr = sorted(ar)
        else:
            res='NO'
            break
    ar.sort(reverse=True)
    if res=='YES':
        print(res)
        print(' '.join(str(i) for i in ar))
    else:
        print('NO')
