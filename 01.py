
with open('data/input.txt') as f:
    lines = f.readlines()

nums = []
for line in lines:
    nums.append(int(line))

count = 0
for i in range(3, len(nums)):
    if nums[i]>nums[i-3]:
        count += 1

print(count)
