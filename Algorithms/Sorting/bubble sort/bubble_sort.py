n = int(input())
ar = list(map(int, input().split()))
count=0
c =True
while c:
    c=False
    for j in range(n-1):
        if ar[j]>ar[j+1]:
            ar[j], ar[j+1] = ar[j+1],ar[j]
            c=True
    count+=1
print(count)
