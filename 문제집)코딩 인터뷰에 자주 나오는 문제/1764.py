n, m = map(int, input().split())
listen = set()
result=[]
for _ in range(n):
    name = input()
    listen.add(name)

for _ in range(m):
    name = input()
    if name in listen:
        result.append(name)
   

print(len(result))
result.sort()
for i in result:
    print(i)
