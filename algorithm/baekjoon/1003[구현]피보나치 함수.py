t = int(input())
for _ in range(t):
    ans = [0, 0]
    n = int(input())
    fibonacci = [[1, 0], [0, 1]]
    if n < 2:

        print(*fibonacci[n])
    else:
        for i in range(2, n + 1):
            nx = fibonacci[i - 1][0] + fibonacci[i - 2][0]
            ny = fibonacci[i - 1][1] + fibonacci[i - 2][1]
            fibonacci.append([nx, ny])

        print(*fibonacci[n])