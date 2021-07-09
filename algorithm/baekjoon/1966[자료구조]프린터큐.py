from collections import deque


def number_counter(lst, M):
    dq = deque(tpl)
    cnt = 0
    while dq:
        # print("starting", dq)
        max_n = max(dq, key=lambda x: x[1])
        e = dq.popleft()
        # print(max_n,e)
        if e[1] == max_n[1]:
            cnt += 1
            if e[0] == M:
                return cnt
        else:
            dq.append(e)


T = int(input())
answer = []

for _ in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    tpl = [(i[0], i[1]) for i in enumerate(lst)]
    ans = number_counter(tpl, M)
    answer.append(str(ans))

print("\n".join(answer))