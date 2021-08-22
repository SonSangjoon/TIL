def color_bingo(n: int):
    for i in range(25):
        r, c = divmod(i, 5)
        if bingo[r][c] == n:
            bingo[r][c] = 0


def is_bingo():
    cnt = 0
    left, right = 0, 0
    for i in range(5):
        col, row = 0, 0
        left += bingo[i][i]
        right += bingo[4 - i][i]
        for j in range(5):
            col += bingo[i][j]
            row += bingo[j][i]
        if not col:
            cnt += 1

        if not row:
            cnt += 1

    if not left:
        cnt += 1

    if not right:
        cnt += 1

    if cnt < 3:
        return False

    return True


bingo = [list(map(int, input().split())) for _ in range(5)]
num_set = [list(map(int, input().split())) for _ in range(5)]

ans = 0

for i in range(25):
    r, c = divmod(i, 5)
    num = num_set[r][c]
    color_bingo(num)

    if is_bingo():
        ans = i + 1
        break

print(ans)