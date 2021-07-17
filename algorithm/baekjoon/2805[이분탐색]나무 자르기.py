N, M = map(int, input().split())
lst = list(map(int, input().split()))

s, e = 0, max(lst)
ans = 0

while s <= e:
    m = (s + e) // 2
    cnt = 0
    for l in lst:
        if l > m:
            cnt += l - m

    if cnt >= M:
        ans = m
        s = m + 1
    else:
        e = m - 1

print(ans)
