# 1. 입력받기
# 제일 작은거 부터 가야함
# 2. DFS,BFS 함수 구현
# 3. 각각 결과 출력
from collections import deque
import sys
input = sys.stdin.readline


N, M, V = map(int,input().split())
graph = [[] for _ in range(N + 1)]


for i in range(M):
  start, end = map(int, input().split())
  graph[start].append(end)
  graph[end].append(start)

for i in range(1, N + 1):
  graph[i].sort() # 🚨

def dfs(graph, v, visited):
  visited[v] = True
  print(v ,end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, v, visited):
  queue = deque([v])
  visited[v] = True
  while queue:
    node = queue.popleft()
    print(node, end=' ')
    for i in graph[node]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

visited_dfs  = [False] * (N + 1)
visited_bfs  = [False] * (N + 1)

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)
