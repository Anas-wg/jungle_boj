import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
K = int(input())

def DFS(start, visited, graph, group):
  visited[start] = group # 현재 노드 그룹 저장
  # 인접 노드 탐색
  for v in graph[start]:
    if visited[v] == 0: # 아직 방문하지 않은 노드
      result = DFS(v, visited, graph, -group) # 음수로 반전하여 인접노드와 다른 그룹으로 저장
      if not result:
        return False
    else:
      if visited[v] == group: # 이미 방문한 곳 중 노드가 현재 그룹과 같다면 이분 그래프가 아님
        return False
  return True

for _ in range(K):
  V, E = map(int, input().split())
  graph = [[] for _ in range(V + 1)]
  visited = [0] * (V + 1)
  for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
  
  for i in range(1, V + 1): # 모든 노드에서 DFS 돌리기
    if visited[i] == 0:
      result = (DFS(i, visited, graph, 1))
      if not result:
        break

  if result:
    print("YES")
  else:
    print("NO")