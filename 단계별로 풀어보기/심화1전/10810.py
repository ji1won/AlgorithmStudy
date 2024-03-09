n,m = map(int, input().split())
bucket = [0]*n
for _ in range(m):
    i, j, k = map(int, input().split())
    for index in range(i-1, j):
        bucket[index] = k

print(" ".join(map(str, bucket)))
