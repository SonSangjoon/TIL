n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

for nums in lst:
    h, w, n = nums[0], nums[1], nums[2]

    if n % h == 0:
        flr = h * 100
        room = n // h
    else:
        flr = n % h * 100
        room = n // h + 1
    print(flr + room)
