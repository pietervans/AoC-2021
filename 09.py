
with open('data/height.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = '9' + lines[i].strip() + '9'

extra = '9'*len(lines[0])
lines = [extra] + lines + [extra]

M = len(lines)
N = len(lines[0])


low_points = []
for i in range(1, M-1):
    for j in range(1, N-1):
        if int(lines[i][j]) < int(lines[i-1][j]) and \
            int(lines[i][j]) < int(lines[i][j-1]) and \
            int(lines[i][j]) < int(lines[i][j+1]) and \
            int(lines[i][j]) < int(lines[i+1][j]):
            low_points.append((i,j))

def find_size(i, j):
    bin = [(i,j)]
    explored = []
    while len(bin) > 0:
        i, j = bin.pop()
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if int(lines[i+di][j+dj]) != 9 \
                and (i+di, j+dj) not in explored \
                and (i+di, j+dj) not in bin:
                bin.append((i+di, j+dj))
        explored.append((i,j))
    return len(explored)

sizes = []
for lp in low_points:
    i, j = lp
    size = find_size(i, j)
    sizes.append(size)

l3 = sorted(sizes)[-3:]
print(l3[0]*l3[1]*l3[2])
