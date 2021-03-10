## 가장 큰 부분합 구하기

```
def maxSubArray(nums):
    
    #기존 부분합 수열(O(n^2))
     <!-- ans = -9999999999
    
     for i in range(len(nums)):
         for j in range(i):
             if sum(nums[j:i+1]) > ans:
                 ans = sum(nums[i:j])
    
     return ans -->
    
    #동적 계획법O(n))

    ans = [None] * len(nums)
    
    ans[0] = nums[0]
    
    for i in range(1, len(nums)):
        ans[i] = max(0, ans[i-1]) + nums[i]
        
    return max(ans)
```

배열의 합을 구할때 마지막 index 를 기준으로 해결한다.
이때 아래의 식이 성립하게 된다.

f(i)
/ nums[i] (if i == 0)
\ max(0,f(i-1)) + nums[i] (if i >0)
