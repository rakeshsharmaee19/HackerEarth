t = int(input())
for k in range(t):
    n = input()
    matchT = 0
    for i in n:
        if int(i) in (0, 9, 6):
            matchT+=6
        elif int(i) == 1:
            matchT+=2
        elif int(i) == 7:
            matchT+=3
        elif int(i) == 4:
            matchT+=4
        elif int(i) in (2,3,5):
            matchT += 5
        else:
            matchT += 7
    num = ''
    while matchT>0:
        if matchT%2==0:
            num+='1'
            matchT-=2
        else:
            num+='7'
            matchT-=3
    print(num)
