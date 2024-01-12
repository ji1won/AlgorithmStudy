num = []
for i in range(7):
    num.append(int(input()))

odd = []
sum = 0
for j in num:
    if j %2 == 1:
        sum+=j
        odd.append(j)
if len(odd) != 0:
    print(sum)
    odd.sort()
    print(odd[0])
else:
    print(-1)