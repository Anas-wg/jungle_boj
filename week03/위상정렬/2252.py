# 1. 입력받기 
# 2. 진입차수 0으로 초기화
# 3. 그래프 생성하면서 진입차수 반영
# 4. 진입차수 0인 것 부터 시작
# 4. 그 노드의 인접한 간선을 제거
# 5. 새롭게 진입차수가 0이된 노드를 큐에 삽입

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  indegree[v] += 1

def topology_sort():
  result = []
  queue = deque()

  for i in range(1, N + 1):
    if indegree[i] == 0:
      queue.append(i)
    
  while queue:
    now = queue.popleft()
    result.append(now)
    for node in graph[now]:
      indegree[node] -= 1
      if indegree[node] == 0:
        queue.append(node)
  return result


result = topology_sort()

for elems in result:
  print(elems, end=' ')

