n = int(input())
ans = 0
while n > 0:
    d, m = divmod(n, 10)
    ans += m
    n = d

print(ans)