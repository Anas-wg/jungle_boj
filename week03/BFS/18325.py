# 1. 입력받기
# 2. BFS
# 출발노드로 부터 모든 노드까지 거리 계산
# 거리가 K인 노드 리턴

import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
result = [0] * (N + 1)

for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)

def bfs(start, graph, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    node = queue.popleft()
    for i in graph[node]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        result[i] = result[node] + 1


bfs(X, graph, visited)

if result.count(K) == 0:
  print(-1)
else:
  for i in range(len(result)):
    if result[i] == K:
      print(i)
