import sys

# 입력 받기
n = int(sys.stdin.readline())
nList = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split()))

# 각 원소가 nList에 있는지 확인하여 결과 출력
for i in mList:
    if i in nList:
        print(1)
    else:
        print(0)
