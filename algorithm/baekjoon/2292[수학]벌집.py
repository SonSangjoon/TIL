n = int(input())

start = 1
plus = 6
ans = 1

if n == 1:
    print(1)

else:
    while True:
        start = start + plus
        ans += 1
        if n <= start:
            print(ans)
            break
        plus += 6