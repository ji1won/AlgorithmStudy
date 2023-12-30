def lis (arr):
    n = len(arr)
    dp = [1]*n
    for i in range(1, n):
        for j in range (i):
            if arr[i]>arr[j]:
                dp[i] = max(dp[j]+1, dp[i])
                
    return dp

n = int(input())
arr = list(map(int, input().split()))

increase = lis(arr)
decrease = lis(arr[::-1])[::-1]

result = max(increase[i]+decrease[i]-1 for i  in range(n))
print(result)