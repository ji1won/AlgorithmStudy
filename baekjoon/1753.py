import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (V + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    return distance

V, E = map(int, input().split())  # 정점의 개수 V, 간선의 개수 E
start = int(input())  # 시작 정점의 번호
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())  # u에서 v로 가는 가중치 w의 간선
    graph[u].append((v, w))

result = dijkstra(start)

for i in range(1, V + 1):
    if result[i] == INF:
        print("INF")
    else:
        print(result[i])
