import numpy as np

with open('data/crab.txt') as f:
    s = f.readline().strip()

elems = s.split(',')
nums = np.zeros((len(elems)))
for i in range(len(elems)):
    nums[i] = int(elems[i])

min = np.inf
for num in nums:
    offsets = np.abs(nums-num)
    changed = .5*offsets*(offsets+1)
    tot = np.sum(changed)
    if tot < min:
        min = tot

print(min)
