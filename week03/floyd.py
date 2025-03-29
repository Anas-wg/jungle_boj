INF = 1e9

# 노드의 개수 및 간선의 개수 입력
V = int(input())
E = int(input())

# 2차원 그래프 만들고 무한으로 초기화
graph = [[INF] * (V + 1) for _ in range(V + 1)]

# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for start in range(1, V + 1):
  for end in range(1, V + 1):
    if start == end:
      graph[start][end] = 0

# 각 간선에 대한 정보를 입력받고, 그 값으로 초기화
for _ in range(E):
  # A에서 B로 가는 비용
  start, end, price = map(int, input().split())
  graph[start][end] = price

# 점화식에 따라 Floyd-Warshall 수행
for k in range(1, V+ 1):
  for a in range(1, V + 1):
    for b in range(1, V + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for start in range(1, V + 1):
  for end in range(1, V + 1):
    # 도달 불가일 경우 INF 출력
    if graph[start][end] == 1e9:
      print('INF')
    # 도달 가능하면 거리 출력
    else:
      print(graph[start][end], end=' ')

