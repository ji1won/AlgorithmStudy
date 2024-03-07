n,k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
    
result = 0
for i in reversed(coin):
    if i <= k:
        result += k//i
        k %= i

print(result)