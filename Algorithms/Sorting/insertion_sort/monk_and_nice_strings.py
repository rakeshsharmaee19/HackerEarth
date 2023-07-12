ar = []
for i in range(int(input())):
    ar.append(input())
res=[0,]
for i in range(1,len(ar)):
    count= 0
    for j in range(i-1,-1,-1):
        if ar[j]<ar[i]:
            count+=1
    res.append(count)
for i in res:
    print(i)
