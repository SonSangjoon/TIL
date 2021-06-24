from collections import deque

A = [0] + list(input())
B = [0] + list(input())
len_A = len(A)
len_B = len(B)
LCS = [[0]*len_B for _ in range(len_A)] 

def print_lcs():
    answer = []
    dq = deque([])
    dq.append([len_A-1, len_B-1, LCS[-1][-1]])
    while dq:
        e = dq.popleft()
        if e[2] == 0:
            break
        if LCS[e[0]-1][e[1]] == e[2]:
            dq.append([e[0]-1,e[1], e[2]])
        elif LCS[e[0]][e[1]-1] == e[2]:
            dq.append([e[0],e[1]-1, e[2]])
        elif LCS[e[0]-1][e[1]-1] == e[2]-1:
            answer.append(A[e[0]])
            dq.append([e[0]-1, e[1]-1, e[2]-1])

    answer.reverse()
    print("".join(answer))

def solution():
    for i in range(1,len_A):
        for j in range(1,len_B):
            if A[i] == B[j]:
                LCS[i][j] = LCS[i-1][j-1]+1
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
    print(LCS[len_A-1][len_B-1])
    print(LCS)
    print_lcs()

solution()