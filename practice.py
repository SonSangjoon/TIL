n = int(input())
ans = [1,1]
for i in range(2,n):
    ans.append(ans[i-2]+ans[i-1])
print(ans)