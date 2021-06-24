N = int(input())

def solution(N):
    ans = [0,1]
    if N <=1:
        return ans[N]
    for i in range(2,N+1):
        ans.append(ans[i-2]+ans[i-1])

    return ans[N]

print(solution(N))