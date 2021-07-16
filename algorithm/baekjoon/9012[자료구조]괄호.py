from collections import deque


def check_vps(lst):
    dq = deque(lst)
    cnt = 0
    while dq:
        e = dq.pop()
        if e == ")":
            cnt += 1
        else:
            if cnt > 0:
                cnt -= 1
            else:
                return "NO"
    if cnt == 0:
        return "YES"
    else:
        return "NO"


n = int(input())
lst = [list(input()) for _ in range(n)]

for sets in lst:
    print(check_vps(sets))
