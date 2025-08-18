N, M = map(int, input().split())

graph = []
for i in range(N):
  graph.append(list(map(int, input())))

visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  # 그래프 범위를 벗어나거나, 방문했거나, 얼음이 아닌 경우
  if x < 0 or x >= N or y < 0 or y >= M or visited[x][y] or graph[x][y] == 1:
    return

  visited[x][y] = True
  
  # 상하좌우 탐색
  dfs(x - 1, y)
  dfs(x + 1, y)
  dfs(x, y - 1)
  dfs(x, y + 1)


answer = 0
for x in range(N):
  for y in range(M):
    if graph[x][y] == 0 and not visited[x][y]:
      dfs(x, y)
      answer += 1

print(answer)