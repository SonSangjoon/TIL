n = int(input())

for i in range(1, n + 1):
    lst = list(map(int, input().split()))
    ans = round(sum(lst) / 10)
    print(f"#{i} {ans}")