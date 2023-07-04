import numpy as np
mat = []
for i in range(int(input())):
    mat.append(list(map(int, input().split())))
rotation = input()
r=0
for i in rotation:
    if i=='R':
        m = np.array(mat, int)
        new=np.rot90(m, k=-1, axes=(0,1))
        mat = new.tolist()
    else:
        m = np.array(mat, int)
        new=np.rot90(m, k=1, axes=(0,1))
        mat = new.tolist()
for i in mat:
    print(' '.join(str(j) for j in i))
