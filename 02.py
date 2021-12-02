
with open('data/instructions.txt') as f:
    lines = f.readlines()

dir = []
amount = []
for line in lines:
    a, b = line.split(' ')
    dir.append(a)
    amount.append(int(b))

hor = 0
ver = 0
aim = 0
for i in range(len(dir)):

    if dir[i] == 'forward':
        hor += amount[i]
        ver += amount[i]*aim
    elif dir[i] == 'down':
        aim += amount[i]
    else:
        aim -= amount[i]

print(hor*ver)
