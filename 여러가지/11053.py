n = int(input())
numList = list(map(int,input().split()))

def dplen(arr):
    n = len(arr)
    dp = [1]*n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i] = max(dp[i],dp[j]+1)
                
    return max(dp)        
print(dplen(numList))