n = int(input())
nList=list(map(int,input().split()))
v = int(input())
count = 0
for i in nList:
    if i == v:
        count +=1
print(count)