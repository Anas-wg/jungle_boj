INF = int(1e9)
graph = [[] for _ in range(N + 1)]
visited = [] # 방문처리 기록용
distance = [INF] * (N + 1) # 거리 테이블


# 미방문 노드이면서 시작노드와 최단거리 노드 반환
def get_smallest_node():
  min_value = INF # 겁나 큰 값으로 초기화
  index = 0
  for i in range(1, N + 1):
    if not visited[i] and distance[i] < min_value:
      min_value = distance[i]
      index = i
  return index


def dijikstra_sequential(start):
  # 시작노드 거리 계산 및 방문처리
  distance[start] = 0
  visited[start] = True

  # 시작노드와 인접한 노드들에 대해 최단 거리를 계산
  for i in graph[start]:
    now = get_smallest_node() # 미방문이면서 start와 최단거리인 노드 반환
    visited[now]  # 선택 정점 방문처리
    for next in graph[now]:
      cost = distance[now] + next[1] # 시작 ~ now + now ~ next 거리
      if cost < distance[next[0]]:
        distance[next[0]] = cost

import heapq
def dijikstra_prorityQ(start):
  queue = []
  heapq.heappush(queue, (0, start))
  distance[start] = 0
  while queue:
    dist, node = heapq.heappop(queue)
    # 큐에서 뽑아낸 거리가 이미 갱신 된 거리보다 클 경우 무시
    if distance[node] < dist:
      continue
    # 큐에서 뽑아낸 노드와 연결된 인접 노드 탐색
    for next in graph[node]:
      cost = distance[node] + next[1] # start ~ node + node ~ next 
      if cost < distance[next[0]]: 
        distance[next[0]] = cost
        heapq.heappush(queue, (cost, next[0]))

