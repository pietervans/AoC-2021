import numpy as np

with open('data/lines.txt') as f:
    lines = f.readlines()

x1, y1 = [], []
x2, y2 = [], []
for i in range(len(lines)):
    points = lines[i].split(' -> ')
    nx1, ny1 = points[0].split(',')
    nx2, ny2 = points[1][:-1].split(',')
    x1.append(int(nx1))
    y1.append(int(ny1))
    x2.append(int(nx2))
    y2.append(int(ny2))

M = max(max(x1), max(x2))+1
N = max(max(y1), max(y2))+1
A = np.zeros((M,N), dtype=int)

for i in range(len(x1)):
    nx1, ny1 = x1[i], y1[i]
    nx2, ny2 = x2[i], y2[i]
    if nx1 == nx2:
        A[nx1, min(ny1,ny2):(max(ny1,ny2)+1)] = A[nx1, min(ny1,ny2):(max(ny1,ny2)+1)] + 1
    elif ny1 == ny2:
        A[min(nx1,nx2):(max(nx1,nx2)+1), ny1] = A[min(nx1,nx2):(max(nx1,nx2)+1), ny1] + 1
    else:
        if (nx1<nx2 and ny1<ny2) or (nx1>nx2 and ny1>ny2):
            sx1, Y = min(nx1, nx2), min(ny1, ny2)
            lx2 = max(nx1, nx2)
            for ind in range(sx1, lx2+1):
                A[ind, Y] = A[ind, Y]+1
                Y += 1
        else:
            Y = ny1
            if nx1 > nx2:
                nx1, nx2 = nx2, nx1
                Y = ny2
            for ind in range(nx1, nx2+1):
                A[ind, Y] = A[ind, Y]+1
                Y -= 1


nb = np.sum(A>1)
print(nb)
