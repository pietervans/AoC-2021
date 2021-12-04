import numpy as np

with open('data/bingo.txt') as f:
    lines = f.readlines()

seq = lines[0].strip()
seq = seq.split(',')
for i in range(len(seq)):
    seq[i] = int(seq[i])


num_boards = len(lines)//6
boards = np.zeros((num_boards,5,5), dtype=int)

lines = lines[2:]
for nb in range(num_boards):
    b = np.zeros((5,5))
    row = 0
    for i in range(6*nb, 6*nb+5):
        line = lines[i].strip()
        line = line.replace('  ', ' ')
        nums = line.split(' ')
        for j in range(5):
            nums[j] = int(nums[j])
        b[row] = nums
        row += 1
    boards[nb] = b



def has_full_line(mat):
    for row_or_col in range(5):
        if np.sum(mat[row_or_col]) == 5:
            return 1
        if np.sum(mat[:,row_or_col]) == 5:
            return 1
    return 0

def compute_sum(board, mat):
    non_mat = 1-mat
    selected = np.multiply(board, non_mat)
    return np.sum(selected)

markers = np.zeros((num_boards,5,5), dtype=int)

index = 0
while True:
    num = seq[index]
    for i in range(num_boards):
        board = boards[i]
        indices = np.where(board==num)
        row, col = indices[0], indices[1]
        if len(row) > 0:
            row, col = row[0], col[0]
            markers[i,row,col] = 1

    cont = False
    for k in range(num_boards):
        has = has_full_line(markers[k])
        if has == 0:
            last_k = k
            cont = True
    if not cont:
        break

    index += 1
    

sum = compute_sum(boards[last_k], markers[last_k])
score = sum*num
print(score)
