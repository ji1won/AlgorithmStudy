n, k = map(int,input().split())
MOD = 1000000000
dp = [[0]*(n+1)for j in range(k+1)]
dp[0][0] = 1

for i in range(1,k+1):
    for j in range( n+1):
        for x in range(j+1):
            dp[i][j] += dp[i-1][j-x]
            dp[i][j] %= MOD
print(dp[k][n])