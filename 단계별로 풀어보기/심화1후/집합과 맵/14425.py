n, m = map(int, input().split())
count = 0

stc_list = []
check_stc_list = []

for _ in range(n):
    stc_list.append(input())  

for _ in range(m):
    check_stc_list.append(input())

for check_stc in check_stc_list:
    if check_stc in stc_list:
        count +=1

print(count)
