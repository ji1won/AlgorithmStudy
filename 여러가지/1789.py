s = int(input())
index = 1
count = 0
while(True):
    if s >= index:
        s -= index
        count += 1
        index += 1

    else :
        break

print(count)