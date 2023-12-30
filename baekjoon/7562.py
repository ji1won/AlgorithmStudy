from collections import deque
def bfs (size, start_x, start_y, end_x, end_y):
    dx = [1,2,2,1,-1,-2,-1,-2]
    dy = [2,1,-1,-2,-2,-1,2,1]

    queue = deque([(start_x, start_y, 0)])
    visited = [[False] * size for _ in range(size)]
    visited[start_x][start_y] = True
    
    while queue:
        x, y, count = queue.popleft()
        if x == end_x and y == end_y :
            return count
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<size and 0<=ny<size and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count+1))
    return -1
      
n = int(input())
for _ in range(n):
    size = int(input())
    now_x , now_y = map(int,input().split())
    goal_x, goal_y = map(int,input().split())
    result = bfs(size, now_x, now_y, goal_x, goal_y)
    print(result)
   