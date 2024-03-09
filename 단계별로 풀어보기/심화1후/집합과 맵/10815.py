n = int(input())
num = set(map(int, input().split()))
m = int(input())
check_num = list(map(int, input().split()))
result = []
for i in check_num:
    if i in num:
        result.append(1)
    else:
        result.append(0)
print(" ".join(map(str,result)))
