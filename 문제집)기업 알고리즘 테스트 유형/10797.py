day = int(input())
cars = list(map(int,input().split()))
count = 0
for i in cars:
    if i == day :
        count += 1

print(count)