# DFS 로 부모 노드를 우째 찾을까?
# 일단 DFS를 돌아봅시다 => DFS를 돌고 자신의 노드 앞이 바로 부모노드? => 아 아니네...
# 

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[]for _ in range(N + 1)]
visited = [False] * (N + 1)
parent = [0] * (N + 1)

for _ in range(N - 1):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

result = []

def dfs(v, graph, visited):
  visited[v] = True
  result.append(v)
  for i in graph[v]:
    if not visited[i]:
      parent[i] = v
      dfs(i, graph, visited)


dfs(1, graph, visited)

for elems in parent[2:]:
  print(elems)

