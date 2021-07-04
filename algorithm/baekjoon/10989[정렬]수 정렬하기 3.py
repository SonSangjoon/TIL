import sys

n = int(input())
lst = [0]*10001
for _ in range(n):
    x = int(sys.stdin.readline())
    lst[x] += 1

for i in range(10001):
    if lst[i] != 0:
        for _ in range(lst[i]):
            print(i)
