# Solution 1
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

#Solution 2
import copy
n = int(input())
mat = []
res_mat = copy.deepcopy(mat)

for i in range(n):
    mat.append(list(map(int, input().split())))
rotation = input()
res_mat = copy.deepcopy(mat)

for i in rotation:
    if i=='R':
        for j in range(n):
            for k in range(n):
                res_mat[k][n-j-1] = mat[j][k]
    else:
        for j in range(n):
            for k in range(n):
                res_mat[n-k-1][j] = mat[j][k]
    mat = res_mat
    res_mat=copy.deepcopy(mat)

for i in mat:
    print(' '.join(str(j) for j in i))
