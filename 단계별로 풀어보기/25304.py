x = int(input())
n = int(input())
sum = 0
for _ in range(n):
    price, num = map(int, input().split())
    sum += (price * num)

if x == sum:
    print('Yes')
else:
    print('No')