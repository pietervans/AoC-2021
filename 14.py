
with open('data/poly.txt') as f:
    lines = f.readlines()

p = lines[0].strip()

d = {}
for i in range(2, len(lines)):
    line = lines[i].strip()
    parts = line.split(' -> ')
    d[parts[0]] = parts[1]

pairs = {}
for i in range(len(p)-1):
    pairs[p[i:i+2]] = pairs.get(p[i:i+2], 0) + 1

for _ in range(40):
    new_pairs = {}
    for k, v in pairs.items():
        if k in d:
            c = d[k]
            new_pairs[k[0]+c] = new_pairs.get(k[0]+c,0) + v
            new_pairs[c+k[1]] = new_pairs.get(c+k[1],0) + v
        else:
            new_pairs[k] = new_pairs.get(k,0) + v
    pairs = new_pairs

counts = {} # For every letter
letters = set()
letters.add(p[0])
for k in pairs:
    letters.add(k[1])

for l in letters:
    s = 0
    for k in pairs:
        if k[1] == l:
            s += pairs[k]
    counts[l] = counts.get(l,0) + s

counts[p[0]] = counts[p[0]]+1


a = min(counts.values())
b = max(counts.values())
print(b-a)
