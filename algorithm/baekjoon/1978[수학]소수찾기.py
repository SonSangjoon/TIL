def prime_lst(n):
    num_lst = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if num_lst[i] == True:
            for j in range(i * 2, n, i):
                num_lst[j] = False
    return [i for i in range(2, n) if num_lst[i] == True]


n = int(input())
lst = list(map(int, input().split()))

prime = prime_lst(1000)
ans = 0

for num in lst:
    if num in prime:
        ans += 1

print(ans)