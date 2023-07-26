for _ in range(int(input())):
    a,b = input().split()
    res= int(a[::-1])+int(b[::-1])
    print(int(str(res)[::-1]))
