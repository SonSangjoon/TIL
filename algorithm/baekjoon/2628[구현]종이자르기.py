a, b = map(int, input().split())
n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]


lst.append((1, a))
lst.append((0, b))
lst.sort(key=lambda x: (x[0], x[1]))

max_row, prev_row = 0, 0
max_col, prev_col = 0, 0

for idx, cut in lst:
    if idx:
        l = cut - prev_row
        max_row, prev_row = max(max_row, l), cut
    else:
        l = cut - prev_col
        max_col, prev_col = max(max_col, l), cut

ans = max_row * max_col
print(ans)
