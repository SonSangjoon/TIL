import sys
from collections import Counter

n, m, b = map(int, input().split())
lst = []

for _ in range(n):
    lst += list(map(int, sys.stdin.readline().split()))

cnt_lst = dict(Counter(lst))
t, ans = float("inf"), 0

for i in range(0, 257):
    inventory, added = b, 0
    temp_t = 0
    for h, cnt in cnt_lst.items():
        if h > i:
            inventory += (h - i) * cnt
            temp_t += (h - i) * cnt * 2
        elif h < i:
            added += (i - h) * cnt
            temp_t += (i - h) * cnt

    if inventory >= added and temp_t < t:
        t = temp_t
        ans = i

print(t, ans)