N = int(input())
def same(dice):
    count = 0
    same = []
    for i in range(4):
        for j in range(i+1,4):
            if dice[i] == dice[j]:
                count+=1
                same.append(dice[i])
    
    if count == 6:
        return 50000+same[0]*5000
    elif count == 3 :
         return 10000+same[0]*1000
    elif count == 2 and len(same) == 2:
        return 2000+same[0]*500 + same[1]*500
    elif count == 1 and len(same) == 1:
        return 1000 + same[0]*100
    else:
        return max(dice)*100
    
result = []       
for _ in range(N):
    dice = list(map(int, input().split()))
    result.append(same(dice))
print(max(result))
    