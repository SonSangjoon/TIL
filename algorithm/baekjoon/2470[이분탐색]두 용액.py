n = int(input())

lst = list(map(int, input().split()))

lst.sort()

l = 0
r = n-1
v = float('inf')

while l< r:
    tmp = lst[l] + lst[r]
    if abs(tmp) < abs(v):
        v = tmp
        al, ar = l, r
        if v == 0:
            break
    if tmp < 0:
        l +=1
    else:
        r -= 1

print(lst[al], lst[ar])
    
