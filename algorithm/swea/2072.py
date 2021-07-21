n = int(input())

for i in range(1, n + 1):
    lst = list(map(int, input().split()))
    ans = 0
    for num in lst:
        if num % 2:
            ans += num
    print(f"#{i} {ans}")