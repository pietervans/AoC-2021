import numpy as np

with open('data/paper.txt') as f:
    lines = f.readlines()

dots = []
folds = []
sec = False
for line in lines:
    line = line.strip()
    if line == '':
        sec = True
    elif sec:
        folds.append(line[11:].split('='))
    else:
        dots.append(line.split(','))

x = [int(dot[0]) for dot in dots]
y = [int(dot[1]) for dot in dots]

Nx = max(x)+1
Ny = max(y)+1

mat = np.zeros((Ny, Nx), dtype=np.bool_)

for j, i in zip(x, y):
    mat[i, j] = True

def fold(mat, ind, along_y):
    if along_y:
        submat = np.flip(mat[ind+1:, :], axis=0)
        mat = mat[0:ind, :]
        mat[-np.size(submat,0):, :] += submat
    else:
        submat = np.flip(mat[:, ind+1:], axis=1)
        mat = mat[:, 0:ind]
        mat[:, -np.size(submat,1):] += submat
    return mat

for f in folds:
    mat = fold(mat, int(f[1]), f[0]=='y')

for row in mat:
    for e in row:
        print('⬛' if e else '  ', end='')
    print()
