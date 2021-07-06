T = int(input())
ans = []
for _ in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    max_level = 0
    for i in range(2,n):
        l = lst[i]-lst[i-2]
        if l > max_level:
            max_level = l
    ans.append(str(max_level))

print("\n".join(ans))