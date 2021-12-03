import numpy as np

with open('data/bin.txt') as f:
    lines = f.readlines()

N = len(lines)
M = len(lines[0])-1
A = np.zeros((N, M))

for i in range(len(lines)):
    for j in range(M):
        num = int(lines[i][j])
        A[i,j] = num

index = 0
B = A # used for CO2

while np.size(A,0) > 1:
    num = sum(A[:,index])
    tot = len(A[:,index])
    if num >= tot/2:
        A = A[np.where(A[:,index]==1)]
    else:
        A = A[np.where(A[:,index]==0)]
    index += 1

index = 0
while np.size(B, 0) > 1:
    num = sum(B[:,index])
    tot = len(B[:,index])
    if num >= tot/2:
        B = B[np.where(B[:,index]==0)]
    else:
        B = B[np.where(B[:,index]==1)]
    index += 1

print(A)
print(B)
