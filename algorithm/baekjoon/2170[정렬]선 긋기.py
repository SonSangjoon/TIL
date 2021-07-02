import sys
N = int(input())

opt = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
opt = sorted(opt, key=lambda x: (x[0], -x[-1]))

n = float('-inf')
ans = 0

for i in range(N):
    s,e = opt[i]
    if n < s:
        n = s
    if n < e:
        ans += e - n
        n = e

# temp_s =  opt[0][0]
# temp_e =  opt[0][1]

# for i in range(1, len(opt)):
#     s, e = opt[i][0], opt[i][1]
#     if temp_s <= s <= temp_e:
#         if temp_e < e:
#             temp_e = e
#     else:
#         ans += temp_e - temp_s
#         temp_s, temp_e = s, e

ans += e-s
print(ans)