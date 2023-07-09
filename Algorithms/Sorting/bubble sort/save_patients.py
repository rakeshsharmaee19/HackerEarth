n = int(input())
vac = list(map(int, input().split()))
pas = list(map(int, input().split()))
v = sorted(vac)
p = sorted(pas)
c = "Yes"
for i in range(n):
    if v[i]<=p[i]:
        c ="No"
        break
print(c)

