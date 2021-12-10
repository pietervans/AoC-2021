
with open('data/syntax.txt') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

open  = ['(', '[', '{', '<']
close = [')', ']', '}', '>']

corrupted = []
for j in range(len(lines)):
    line = lines[j]
    expected = []
    for c in line:
        if c in open:
            i = open.index(c)
            expected.append(close[i])
        else:
            exp = expected.pop()
            if exp != c:
                corrupted.append(j)


lines = [lines[i] for i in range(len(lines)) if i not in corrupted]
scores = []
for j in range(len(lines)):
    line = lines[j]
    expected = []
    for c in line:
        if c in open:
            i = open.index(c)
            expected.append(close[i])
        else:
            exp = expected.pop()
            assert exp == c
    
    score = 0
    while len(expected) > 0:
        c = expected.pop()
        i = close.index(c)+1 # the number to add
        score = score*5 + i
    scores.append(score)

print(sorted(scores)[(len(scores)-1)//2])
