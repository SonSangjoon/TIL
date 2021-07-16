n = int(input())

lst = [list(input().split()) for _ in range(n)]

sorted_lst = sorted(lst, key=lambda x: int(x[0]))

for p in sorted_lst:
    print(p[0], p[1])
