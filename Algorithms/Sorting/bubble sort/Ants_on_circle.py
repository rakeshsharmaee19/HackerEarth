n, m, t = input().split()
pos_out = []
for i in range(int(m)):
    pos, dirt = input().split()
    if dirt == '1':
        ps = (int(t)+int(pos))%int(n)
        pos_out.append(ps if ps!=0 else int(n))
    else:
        ps = (-int(t)+int(pos))%int(n)
        pos_out.append(ps if ps!=0 else int(n))
a = sorted(pos_out)


# #using buble short
# for i in range(len(pos_out)-1):
#     for j in range(len(pos_out)-1-i):
#         if pos_out[j]>pos_out[j+1]:
#             pos_out[j],pos_out[j+1] = pos_out[j+1],pos_out[j]
print(' '.join(str(i) for i in a))
