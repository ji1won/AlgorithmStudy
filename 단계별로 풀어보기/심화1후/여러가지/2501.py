n, k = map(int,input().split())
result = []
for i in range(1,n+1):
    if n % i == 0:
        result.append(i)

if len(result) != 0 and len(result)>=k:
    print(result[k-1])
else :
    print(0)