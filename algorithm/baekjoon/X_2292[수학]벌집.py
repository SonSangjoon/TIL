n = int(input())

if n == 1:
    print(0)

else:
    ans = 0
    while True:
        max_cnt = ans * (ans - 1)
        min_cnt = (ans - 1) * (ans - 2)

        if min_cnt <= n < max_cnt:
            print(ans - 2)
            break
        ans += 1
