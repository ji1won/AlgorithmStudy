n = int(input())
score = list(map(int, input().split()))
result = []
plus = 0
for i in score:
    if i == 1 :
        plus += 1
        result.append(plus)
    else:
        plus = 0
total = sum(result)
print(total)     
    