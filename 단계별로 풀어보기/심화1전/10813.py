n,m = map(int, input().split())
bucket = list(range(1, n+1))
t = 0
for _ in range(m):
    i, j = map(int, input().split())
    t = bucket[i-1]
    bucket[i-1] = bucket[j-1]
    bucket[j-1] = t
print(" ".join(map(str,bucket)))