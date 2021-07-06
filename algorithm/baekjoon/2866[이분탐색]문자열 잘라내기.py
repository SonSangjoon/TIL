from collections import deque

R, C = map(int, input().split())

row_lst = [list(input()) for _ in range(R)]

column_lst = list(map(list, zip(*row_lst)))
s, e = 1, R
ch  = False
while s < e:
    m = (s+e)//2 
    checker = []
    for letter in column_lst:
        l = letter[m:] 
        if l in checker:
            e = m-1
            ch = True
            continue
        else:
            checker.append(l)
    s = m + 1

if ch:
    print(e)
else:
    print(e+1)