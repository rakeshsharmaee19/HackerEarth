for i in range(int(input())):
    g,r = input().split()
    ot_dt = {1:0, 2:0}
    for j in range(int(input())):
        first, second = input().split()
        ot_dt[1] += int(first)
        ot_dt[2] += int(second)
    print(min((int(g)*ot_dt[1]+int(r)*ot_dt[2]),(int(r)*ot_dt[1]+int(g)*ot_dt[2])))
