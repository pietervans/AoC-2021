import numpy as np

with open('data/octo.txt') as f:
    lines = f.readlines()

matrix = np.empty((12,12))
for i in range(10):
    row = np.empty((12))
    for j in range(10):
        row[j+1] = int(lines[i][j])
    matrix[i+1] = row
matrix[0] = -np.inf
matrix[11] = -np.inf
matrix[:,0] = -np.inf
matrix[:,11] = -np.inf

flashes = 0
step = 1
# for k in range(100):
while True:
    matrix += 1
    pos = np.where(matrix>9)
    while np.size(pos[0]) > 0:
        rows = pos[0]
        cols = pos[1]
        flashes += np.size(rows)
        for i in range(np.size(rows)):
            u = rows[i]
            v = cols[i]
            matrix[u,v] = np.nan
            for du in [-1, 0, 1]:
                for dv in [-1, 0, 1]:
                    matrix[u+du,v+dv] += 1
        pos = np.where(matrix>9)
    if np.sum(np.isnan(matrix)) == 100:
        print(f'Step {step}')
        break
    matrix[np.isnan(matrix)] = 0
    step += 1

# print(flashes)
