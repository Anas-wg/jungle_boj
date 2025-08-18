from collections import deque

N, M = map(int, input().split())

graph = []

for i in range(N):
  graph.append(list(map(int , input())))

visited = [[False] * M for _ in range(M)]
dx = [0, 0, 1, -1]
dy = [-1, 1,0, 0]

def bfs(x, y):
  queue = deque([])
  queue.append([x, y, 1])
  visited[x][y] = True
  while queue:
    x,y,dist = queue.popleft()
    if x == N -1 and y == M - 1:
      return dist
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
        if graph[nx][ny] ==1 :
          queue.append([nx,ny,dist+1])
          visited[nx][ny] = True


print(bfs(0,0))



