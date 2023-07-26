for _ in range(int(input())):     
    n = int(input())     
    arr = list(map(int,input().split()))     
    a = [0]*n     
    for i in range(n):         
        a[arr[i]-1] = i + 1     
    print("inverse") if a == arr else print("not inverse")
