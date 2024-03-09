n, m = map(int, input().split())
bucket = list(range(1,n+1))


for _ in range(m):
    i, j = map(int, input().split())
    bucket[i-1:j]=bucket[i-1:j][::-1]
    
print(" ".join(map(str,bucket)))