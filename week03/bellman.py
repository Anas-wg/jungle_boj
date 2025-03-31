# 음수 간선 포함시 벨만포드 사용

import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력
V, E = map(int, input().split())
# 간선의 정보를 담는 리스트
edges = []
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (V + 1)

# 모든 간선의 정보 입력
for _ in range(E):
  start, end, cost = map(int, input().split())
  edges.append((start, end, cost))

def bellman_fort(start):
  # 시작 노드 초기화
  distance[start] = 0
  # 전체 V - 1 번의 round 반복
  for i in range(V):
    # 매 반복마다 모든 간선 확인
    for j in range(E):
      cur_node = edges[j][0]
      next_node = edges[j][1]
      edge_cost = edges[j][2]
      # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
        distance[next_node] = distance[cur_node] + edge_cost
        # V번째 라운드에서도 값이 갱신시 음수 순환 존재
        if i == (V - 1):
          return True
  return False
