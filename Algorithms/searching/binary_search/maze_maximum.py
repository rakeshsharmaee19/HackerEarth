n, m = input().split()
arr = []
for i in range(int(n)):
    arr.append(list(map(int, input().split())))
for i in range(int(n)):
    for j in range(int(m)):
        arr[0][j] = min(arr[0][j], arr[i][j])
        arr[i][0] = min(arr[i][0], arr[i][j])
a = max(arr[0])
b = arr[0][0]
for i in range(int(n)):
    b = max(b,arr[i][0])
print(min(a,b))
