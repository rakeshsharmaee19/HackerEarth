import collections
n, t = input().split()
d = {}
for i in range(int(n)):
    nm, s = input().split()
    if int(s) in d:
        d[int(s)].append(nm)
    else:
        d[int(s)]=[nm]
od = dict(sorted(d.items(), reverse=True))
c= 0
res = []
for i in od:
    od[i].sort()
    if len(od[i])+c<=int(t):
        res.extend(od[i])
        
        c+=len(od[i])
    else:
        res.extend(od[i][:(int(t)-c)])
        break
for i in res:
    print(i)
