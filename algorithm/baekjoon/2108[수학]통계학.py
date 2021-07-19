from collections import Counter

n = int(input())
lst = sorted([int(input()) for _ in range(n)])
cnt = Counter(lst)


print(round(sum(lst) / n))
print(lst[(n // 2)])

max_cnt = 0
max_lst = []

for k, v in cnt.items():
    if v > max_cnt:
        max_cnt = v
        max_lst = [k]
    elif v == max_cnt:
        max_lst.append(k)
srt_lst = sorted(max_lst)


if len(srt_lst) == 1:
    print(srt_lst[-1])
else:
    print(srt_lst[1])

print(lst[-1] - lst[0])
