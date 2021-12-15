import numpy as np

with open('data/path.txt') as f:
    lines = f.readlines()

mat = []
for line in lines:
    line = line.strip()
    row = []
    for c in line:
        row.append(int(c))
    mat.append(row)

M = len(mat)
N = len(mat[0])
mat0 = np.array(mat)
mat = np.array(mat)
for k in range(1, 5):
    mat = np.hstack((mat, np.mod(mat0+k-1, 9) + 1))
mat0 = mat
for k in range(1, 5):
    mat = np.vstack((mat, np.mod(mat0+k-1, 9) + 1))

M = len(mat)
N = len(mat[0])

parents = [[(-1,-1)]*N for _ in range(M)]
costs = [[float('inf')]*N for _ in range(M)] # Costs to get here
costs[0][0] = 0
bin = [(0,0)]

while len(bin) > 0:
    cmin = float('inf')
    for i in range(len(bin)):
        pos = bin[i]
        if costs[pos[0]][pos[1]] + M-1-pos[0] + N-1-pos[1] < cmin:
            cmin = costs[pos[0]][pos[1]] + M-1-pos[0] + N-1-pos[1]
            ci = i

    pos = bin.pop(ci)
    if pos == (M-1, N-1):
        print('Reached end!')
        break
    for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
        if pos[0]+di >= 0 and pos[0]+di < M and pos[1]+dj >= 0 and pos[1]+dj < N:
            if costs[pos[0]][pos[1]] + mat[pos[0]+di, pos[1]+dj] < costs[pos[0]+di][pos[1]+dj]:
                parents[pos[0]+di][pos[1]+dj] = pos
                costs[pos[0]+di][pos[1]+dj] = costs[pos[0]][pos[1]] + mat[pos[0]+di, pos[1]+dj]
                bin.append((pos[0]+di, pos[1]+dj))

# path = [(M-1,N-1)]
# pos = path[-1]
# while pos != (0,0):
#     pos = parents[pos[0]][pos[1]]
#     path.insert(0, pos)

print(costs[M-1][N-1])
