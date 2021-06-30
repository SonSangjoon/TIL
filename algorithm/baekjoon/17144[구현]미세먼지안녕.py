import math

def spread():

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    starts = []

    for i in range(R):
        for j in range(C):
            if mp[i][j] != -1 and mp[i][j] != 0:
                starts.append((i,j,mp[i][j]))
    
    for start in starts:
        x = start[0]
        y = start[1]
        spread =  math.floor(start[2]/5)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < R and 0<= ny <C and mp[nx][ny] != -1:
                mp[nx][ny] += spread
                mp[x][y] -= spread

def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        mp[x][y], before = before, mp[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 이동
def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        mp[x][y], before = before, mp[x][y]
        x = nx
        y = ny


def solution():
    global R, C, T, mp ,ac, up, down
    R, C, T = map(int, input().split())

    mp = []
    ac = []
    for i in range(R):
        line = list(map(int, input().split()))
        mp.append(line)

        if line[0] == -1:
            ac.append(i)
    up = ac[0]
    down = ac[1]
    for _ in range(T):
        spread()
        air_up()
        air_down()

    ans = 0
    for line in mp:
        ans += sum(line)

    ans +=2

    print(ans)

solution()



# def filter():
#     top = ac[0]
#     for i in range(1, top, -1):
#         mp[i][0] = mp[i-1][0]
    
#     for i in range(0,C-1):
#         mp[0][i] = mp[0][i+1]   

#     for i in range(0, top):
#         mp[i][C-1] =  mp[i+1][C-1]

#     for i in range(C-1, 1, -1):
#         mp[top][i] = mp[top][i-1]
#     mp[top][1] = 0

#     bottom = ac[1]
#     for i in range(bottom+1, R-1):
#         mp[i][0] = mp[i+1][0]
    
#     for i in range(0,C-1):
#         mp[R-1][i] = mp[R-1][i+1]   

#     for i in range(R-1, bottom, -1):
#         mp[i][C-1] =  mp[i-1][C-1]

#     for i in range(C-1, 1 ,-1):
#         mp[bottom][i] = mp[bottom][i-1]    
#     mp[bottom][1] = 0
