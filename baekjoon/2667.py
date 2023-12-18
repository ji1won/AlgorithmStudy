n = int(input())
dx = [0,0,-1,1]
dy = [1,-1,0,0]
graph = [list(map(int,input())) for _ in range(n)] #입력 받은 지도 정보
result = [] #결과 단지 저장 리스트
count = 0 #현재 단지 집수
def dfs(x, y):
    global count
    if x<0 or x>=n or y<0 or y>=n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0 #방문했다고 표시
        count += 1 #집 개수 증가
        
        #상하좌우 DFS하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    return False
    
for i in range (n):
    for j in range(n):
        if dfs(i,j):
            result.append(count)
            count = 0

result.sort()
print(len(result))
for i in result:
    print(i)