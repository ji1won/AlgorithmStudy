import sys
n, k = map(int, sys.stdin.readline().split())
weight = 0
wv = []
small = []
for _ in range(n):
    w,v = map(int, sys.stdin.readline().split())
    wv.append((w,v))
for i in range(n):
    for j in range(i,n):
        weight += wv[j][0]
        if weight <= k:
            small.append(wv[j])
        else: weight -= wv[j][0]
# 두 번째 요소를 기준으로 리스트 정렬

small.sort(key = lambda x:x[1])
print(small[0])