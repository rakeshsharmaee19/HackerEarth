res = 1
n=int(input())
l = map(int, input().split())
for i in l:
    res=(res*i)%((10**9)+7)
print(res)
