# 1. 입력받기
# 2. 그래프 생성 -> 노드와 실내,실외 정보 담기
# 3. DFS 탐색 실행 -> 실내 - 실내 면 종료, 실내 - 실외는 실내 만날때 까지 진행

import sys
input = sys.stdin.readline

N = int(input())

status = [0] +list(map(int,list(input().rstrip()))) # 1이면 실내, 0이면 실외

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
route = 0

for _ in range(N - 1):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)
  # 두 정점 모두 실내라면 경로의 수 2 증가
  if status[u] == 1 and status[v] == 1:
    route += 2


def DFS(start):
  visited[start] = True
  inside_count = 0 # 현재 노드와 인접한 실내 노드 개수 저장할 변수
  for v in graph[start]:
    if status[v] == 1:
      inside_count += 1 # 실내 노드 개수 증가

    elif not visited[v] and status[i] == 0:
      inside_count += DFS(v) # 인접 노드가 실외라면 그 노드부터 탐색하여 실내 노드 개수 증가
  return inside_count

for i in range(1, N + 1):
  if status[i] == 0 and not visited[i]:
    result = DFS(i)
    route += result * (result - 1)


print(route)