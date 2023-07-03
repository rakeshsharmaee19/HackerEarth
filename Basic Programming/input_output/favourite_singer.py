from collections import Counter
n = int(input())
ar = input().split()
count = Counter(ar)
mx = max(count.values())
print(list(count.values()).count(mx))
