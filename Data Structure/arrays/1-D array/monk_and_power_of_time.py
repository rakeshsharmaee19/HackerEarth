n = int(input())
s = 0
co = list(map(int,input().split()))
po = list(map(int,input().split()))

while p_o:
    while(co[0] != po[0]):
        co = co[1:]+co[:1]
        s = s + 1
    po.pop(0)
    co.pop(0)
    s = s+1
print(s)
