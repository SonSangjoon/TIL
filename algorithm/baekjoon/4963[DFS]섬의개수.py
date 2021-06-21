import sys
sys.setrecursionlimit(10000000)

def dfs(x,y):
    dx = [-1,-1,0,0,1,-1,1,1]
    dy = [-1,1,-1,1,0,0,-1,1]
    visited[x][y] = 1
    for i in range(8):

        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0<= new_x< h and 0<= new_y< w:
            if visited[new_x][new_y] == 0 and mp[new_x][new_y] == 1:
                dfs(new_x, new_y)

answer = []

while True:
    w, h = map(int,input().split())

    if w == 0 and h == 0:
        break 

    mp = [list(map(int, input().split())) for _ in range(h) ]
    visited = [[0]*w for _ in range(h)]
    ans = 0

    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and mp[i][j] == 1:
                ans += 1
                dfs(i,j)
    answer.append(str(ans))

print("\n".join(answer))