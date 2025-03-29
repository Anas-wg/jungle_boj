# 부모 노드를 찾는 함수 (경로 압축 포함)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 집합을 합치는 함수 (Union)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 크루스칼 알고리즘 함수
def kruskal(V, edges):
    # 부모 테이블 초기화
    parent = [i for i in range(V + 1)]

    # 간선을 비용 기준으로 정렬
    edges.sort(key=lambda x: x[2])
    
    total_cost = 0  # 최소 신장 트리의 가중치 합
    mst_edges = []  # 최소 신장 트리에 포함된 간선들

    for a, b, cost in edges:
        # 사이클이 발생하지 않는 경우에만 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b) # 부모노드 갱신
            total_cost += cost # 간선의 가중치 더하기
            mst_edges.append((a, b, cost)) # 간선 추가

    return total_cost, mst_edges

# 입력 받기
V, E = map(int, input().split())  # 노드 수, 간선 수
edges = []
for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))

# 크루스칼 알고리즘 실행
total_cost, mst_edges = kruskal(V, edges)

# 결과 출력
print(f"최소 신장 트리의 총 비용: {total_cost}")
print("최소 신장 트리에 포함된 간선들:")
for a, b, cost in mst_edges:
    print(f"{a} - {b} (비용: {cost})")
