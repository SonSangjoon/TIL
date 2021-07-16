from collections import deque

R = [i for i in input()]
D = [i for i in input()]
A = [i for i in input()]

A_start, D_start = [0] * len(A), [0] * len(D)
A_count, D_count = [0] * len(A), [0] * len(D)

s = R[0]

for i in range(len(A)):
    if D[i] == s:
        D_start[i] == 1
    if A[i] == s:
        A_start[i] == 1

    R = deque(R)

    count = D + A
