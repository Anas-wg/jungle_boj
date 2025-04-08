INF = 1e9

V = int(input())
E = int(input())

graph = [[INF] * (V + 1) for _ in range(V + 1)]

# 자기 자신으로 가는 비용은 0
for i in range(1, V + 1):
    graph[i][i] = 0

# 간선 정보 입력
for _ in range(E):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost

# Floyd-Warshall 알고리즘 수행
for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # ⭐ 중간 노드 k를 거친 후 그래프 상태 출력
    print(f"\n=== After considering node {k} ===")
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if graph[i][j] == INF:
                print("INF", end=' ')
            else:
                print(int(graph[i][j]), end=' ')
        print()
