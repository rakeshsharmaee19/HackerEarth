n = input()
arr = list(map(int, input().split()))
arr.sort()
if arr[-1]>=0:
    ar = [i for i in arr if i>=0]
    print(sum(ar), len(ar))
else:
    print(arr[-1], 1)
