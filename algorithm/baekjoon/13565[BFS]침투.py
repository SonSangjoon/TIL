from collections import deque

def solution():
    M, N = map(int, input().split())
    fiber = [list(input()) for _ in range(M)]
    visited = [[False]*N for _ in range(M)]
    answer = "NO"

    dq = deque([])
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    for i in range(N):
        if fiber[0][i] == '0':
            dq.append([0,i])

    while dq:
        e = dq.popleft()
        if e[0] == M-1:
            return "YES"

        visited[e[0]][e[1]] =True
        for i in range(4):
            new_x = e[0] + dx[i]
            new_y = e[1] + dy[i]
            if 0<= new_x < M and 0<= new_y < N:
                if visited[new_x][new_y] == False and fiber[new_x][new_y] == '0':
                    dq.appendleft([new_x, new_y])
    
    return answer

print(solution())
        