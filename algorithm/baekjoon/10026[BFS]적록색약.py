from collections import deque

N = int(input())
test = [list(input()) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    while dq:
        e = dq.popleft()
        x, y = e[0], e[1]
        visited[x][y] = True

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < N and 0 <= new_y < N:
                if visited[new_x][new_y] == False and test[new_x][new_y] == test[x][y]:
                    dq.append((new_x, new_y))

    return result



for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            result += 1
            dq = deque([])
            dq.append((i, j))
non_color_blind = bfs()

print(non_color_blind, end=" ")

for i in range(N):
    for j in range(N):
        if test[i][j] == "G":
            test[i][j] = "R"

color_blind = bfs()

print(color_blind)


