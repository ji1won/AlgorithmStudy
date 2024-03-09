import sys
n, m = map(int, sys.stdin.readline().split())
pocketmon = {}
for i in range(n):
    name = sys.stdin.readline().rstrip()
    pocketmon[name] = i+1
    pocketmon[i+1] = name

for _ in range(m):
    name = sys.stdin.readline().rstrip()
    if name.isdigit(): 
        print(pocketmon[int(name)])
    else:
        print(pocketmon[name])
