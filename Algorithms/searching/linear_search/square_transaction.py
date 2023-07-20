import bisect
n = input()
total = 0
arr = []
for each in input().split():
    total+=int(each)
    arr.append(total)

for _ in range(int(input())):
    q = int(input())

    print(-1) if q>arr[len(arr)-1] else print(bisect.bisect_left(arr,q)+1)
            


# for _ in range(int(input())):
#     q = int(input())
#     itr = iter(arr)
#     ch = True
#     sm= 0
#     count = 0
#     while ch:
#         try:
#             sm+=next(itr)
#             count+=1
#             if sm>=q:
#                 ch=False
#         except:
#             count = -1
#             ch =False
#     print(count)
