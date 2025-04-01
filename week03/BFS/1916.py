# 1. 입력받기
# 2. 출발지, 도착지 설정
# 3. 다익스트라 함수 정의
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
  start,end,cost = map(int,input().split())
  graph[start].append((cost, end))
origin, destination = map(int, input().split())

dist = [INF] * (N + 1)

def dijikstra(origin):
  hq = []
  heapq.heappush(hq,(0, origin))
  dist[origin] = 0
  while hq:
    cost, node = heapq.heappop(hq)
    if dist[node] < cost: # 기존 거리보다 더 큰 경우
      continue
    
    # heap에서 꺼낸 노드 인접한 노드 탐색
    for weight, neighbor in graph[node]:
      # 새로운 cost -> origin ~ node + node ~ next 
      new_cost = dist[node] + weight
      # 기존 가격보다 새로운 cost가 더 싸다면 갱신
      if new_cost < dist[neighbor]:
        dist[neighbor] = new_cost
        # 갱신후 heappush
        heapq.heappush(hq, (new_cost, neighbor))

dijikstra(origin)

print(dist[destination])