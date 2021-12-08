from itertools import product
from copy import deepcopy
from tqdm import tqdm

with open('data/digits.txt') as f:
    lines = f.readlines()

observed = []
for line in lines:
    line = line.split(' | ')
    nums = line[0].split(' ')
    nums += line[1].strip().split(' ')
    for i in range(len(nums)):
        nums[i] = set([c for c in nums[i]])
    observed.append(nums)

def only_leave(s, letters):
    # Only leave the listed letters in the given set
    for c in s.copy():
        if c not in letters:
            s.remove(c)

special_nums = {2:1, 4:4, 3:7, 7:8}
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
map = {
    0: set([0, 1, 2, 4, 5, 6]),
    1: set([2, 5]),
    2: set([0, 2, 3, 4, 6]),
    3: set([0, 2, 3, 5, 6]),
    4: set([1, 2, 3, 5]),
    5: set([0, 1, 3, 5, 6]),
    6: set([0, 1, 3, 4, 5, 6]),
    7: set([0, 2, 5]),
    8: set(range(7)),
    9: set([0, 1, 2, 3, 5, 6])
}
inv_map = { # from display indices to number
    (0, 1, 2, 4, 5, 6): 0,
    (2, 5): 1,
    (0, 2, 3, 4, 6): 2,
    (0, 2, 3, 5, 6): 3,
    (1, 2, 3, 5): 4,
    (0, 1, 3, 5, 6): 5,
    (0, 1, 3, 4, 5, 6): 6,
    (0, 2, 5): 7,
    (0, 1, 2, 3, 4, 5, 6): 8,
    (0, 1, 2, 3, 5, 6): 9
}

all_res = []
for i in range(len(observed)):
    obs = observed[i]
    res = [] # The possible letters for each position on the display
    for j in range(7):
        res.append(set(LETTERS))
    for o in obs:
        if len(o) in [2, 4, 3, 7]:
            # This is a 1, 4, 7 or 8
            n = special_nums[len(o)]
            for k in range(7):
                if k in map[n]:
                    only_leave(res[k], o)
                else:
                    res[k] -= o
    all_res.append(res)

def is_finished(res):
    for s in res:
        if len(s) != 1:
            return False
    return True

for i in tqdm(range(len(observed))):
    obs = observed[i] # List of sets of letters
    res = all_res[i]  # idem
    
    obs5 = [] # Length 5
    obs6 = []
    for o in obs:
        if len(o) == 5:
            obs5.append(o)
        elif len(o) == 6:
            obs6.append(o)
    obs56 = obs5+obs6

    nums5 = [2, 3, 5]
    nums6 = [0, 6, 9]

    guess5 = product(nums5, repeat=len(obs5))
    guess6 = product(nums6, repeat=len(obs6))
    guess56 = product(guess5, guess6)
    for g in guess56:
        res_try = deepcopy(res)
        nums_try = g[0]+g[1] # guessed nums corresponding to obs56
        
        for j in range(len(nums_try)):
            num = nums_try[j]
            o = obs56[j]
            for k in range(7):
                if k in map[num]:
                    only_leave(res_try[k], o)
                else:
                    res_try[k] -= o
        if is_finished(res_try):
            all_res[i] = res_try
            break

TOT = 0
for i in range(len(observed)):
    output_vals = observed[i][-4:] # List (length 4) of sets of letters
    res = [list(s)[0] for s in all_res[i]] # List of letters

    num_obs = 0
    base = 1000
    for o in output_vals:
        inds = []
        for letter in o:
            disp_index = res.index(letter)
            inds.append(disp_index)
        single_num = inv_map[tuple(sorted(inds))]
        num_obs += base*single_num
        base /= 10
    TOT += num_obs

print(TOT)
