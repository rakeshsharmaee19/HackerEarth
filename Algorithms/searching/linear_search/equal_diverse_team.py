for _ in range(int(input())):
    n, k = input().split()
    arr = list(map(int, input().split()))
    a = set(arr)
    if len(a)==int(k)*2:
        print('YES')
    elif len(a)>int(k)*2:
        print('NO')
    else:
        res = {1:0, 2:0}
        for i in a:
            if arr.count(i)>1:
                res[2] +=1
            else:
                res[1] += 1
        ch = 'NO'
        both_team_len = res[1]
        if res[1]+(res[2]*2)>=int(k)*2:
            ch ='YES'
        print(ch)
