n = int(input())

lst = [tuple(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda x: x[1])

max_x, max_y = lst.pop()
left = right = max_x
ans = max_y

while lst:
    x, y = lst.pop()
    if x < left:
        ans += (left - x) * y
        left = x
    if x > right:
        ans += (x - right) * y
        right = x

print(ans)