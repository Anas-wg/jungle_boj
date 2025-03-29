import sys
from collections import deque
input = sys.stdin.readline

V, E = map(int,input().split())
# 진입차수 초기화
indegree = [0] * (V + 1)
# 그래프 정보 담기 위한 연결 리스트
graph = [[] for _ in range(V + 1)]

# 연결리스트로 그래프 생성
for _ in range(E):
  start, end = map(int, input().split())
  graph[start].append(end)
  indegree[end] += 1 # 진입차수 추가

# 위상 정렬 함수

def topology_sort():
  result = []
  q = deque()
  for i in range(1 , V + 1):
    if indegree[i] == 0: # 진입차수가 0이라면 큐에 Enque
      q.append(i)

  while q:
    now = q.popleft()
    result.append(now)
    for g in graph[now]:
      indegree[g] -= 1
      if indegree[g] == 0:
        q.append(g) 
