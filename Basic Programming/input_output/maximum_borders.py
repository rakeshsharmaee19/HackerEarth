import numpy
 
for t in range(int(input())):
    list1= []
    n, m = map(int, input().split())
    res= []
    for i in range(n):
        a=[]
        a[:0] = input()
        list1.append(a)
        count = 1
        for j in range(m-1):
            if a[j]=='#' and a[j+1]=='#':
                count+=1
            else:
                res.append(count)
                count=1
    list2 = numpy.transpose(list1)
    for i in range(m):
        count = 1
        for j in range(n-1):
            if list2[i][j]=='#' and list2[i][j+1]=='#':
                count+=1
            else:
                res.append(count)
                count=1
    print(max(res))
