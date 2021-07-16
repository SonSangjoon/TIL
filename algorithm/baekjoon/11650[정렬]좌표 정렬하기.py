n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]

sorted_lst = sorted(lst, key=lambda x: (x[0], x[1]))

for p in sorted_lst:
    print(p[0], p[1])
