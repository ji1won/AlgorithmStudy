from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
day = -1

queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j, 0))
            
                
while queue:
    x, y, day = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny] = 1
            queue.append((nx, ny, day + 1))
            
isall = all(all(box) for box in graph)

if isall :
    print(day)
else:
    print(-1)