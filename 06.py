import numpy as np

with open('data/fish.txt') as f:
    lines = f.readlines()

elem = lines[0].strip().split(',')

seq = np.zeros((len(elem)), dtype=int)
for i in range(len(elem)):
    seq[i] = int(elem[i])
nums = np.bincount(seq, minlength=9)
print(nums)

for _ in range(256):
    nums[7] = nums[7] + nums[0] # 0 means 6 in end result
    nums = np.hstack((nums[1:], nums[0]))

print(nums)
print(np.sum(nums))
