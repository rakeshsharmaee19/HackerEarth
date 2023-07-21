n = int(input())
s = 0
c_o = list(map(int,input().split()))
p_o = list(map(int,input().split()))

while p_o:
    while(c_o[0] != p_o[0]):
        c_o = c_o[1:]+c_o[:1]
        s = s + 1
    p_o.pop(0)
    c_o.pop(0)
    s = s+1
print(s)
