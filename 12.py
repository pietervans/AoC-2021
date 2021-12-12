
with open('data/cave.txt') as f:
    lines = f.readlines()

d = {}
nodes = set()
for line in lines:
    a, b = line.strip().split('-')
    nodes.add(a)
    nodes.add(b)
    conn1 = d.get(a, set())
    conn1.add(b)
    d[a] = conn1
    conn2 = d.get(b, set())
    conn2.add(a)
    d[b] = conn2

def is_valid(path):
    small_nodes = []
    twice = False
    for n in path:
        if n.islower():
            if n in small_nodes:
                if twice:
                    return False
                twice = True
            small_nodes.append(n)
    return True

bin = [['start']]
paths = set()
while len(bin) > 0:
    p = bin.pop()
    p_cont = []
    for next_node in d[p[-1]]:
        if next_node == 'start':
            continue
        new_path = list(p)
        new_path.append(next_node)
        if next_node == 'end':
            paths.add(tuple(new_path))
        elif is_valid(new_path):
            bin.append(new_path)

print(len(paths))
