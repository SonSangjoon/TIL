n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(6)]

# 긴 변 및 긴 변 기준 짧은 변위치 생성
long_idx = {}
for idx, v in enumerate(lst):
    d, l = v
    if d in long_idx:
        long_idx.pop(d)
    else:
        long_idx[d] = [idx, idx - 3]

# 큰 사각형, 작은 사각형 넓이 계산
max_area, min_area = 1, 1
for d, idx in long_idx.items():
    max_area *= lst[idx[0]][1]
    min_area *= lst[idx[1]][1]

print(n * (max_area - min_area))
