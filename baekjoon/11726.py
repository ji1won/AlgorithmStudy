n = int(input())
result = [0]*(n+1)
result [0] = 1
result [1] = 2
    
for i in range (2,n):
    result[i] = result[i-2] + result[i-1]

print(result[n-1]%10007)