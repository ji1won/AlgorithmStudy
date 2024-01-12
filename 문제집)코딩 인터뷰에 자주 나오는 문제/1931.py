n = int(input())
time = []
for _ in range(n):
    start, end = map(int, input().split())
    time.append((start, end))

time.sort(key = lambda x:(x[1],x[0]))#끝나는 시간 기준 오름차순 정렬 후 시작 시간 기준 오름차순 정렬함.   
count = 0
endTime = 0
for start, end in time:
    if start >=endTime:
        count += 1
        endTime = end
print(count)         
