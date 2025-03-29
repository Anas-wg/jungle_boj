# 1. 입력받기
# 2. 그래프 만들기
# 3. Union_find 
# 4. Kruskal
# 간선을 하나씩 추가하면서 최소 가중치인 간선 선택
# 만약 사이클 형성한다면 넘기기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
V, E = map(int, input().split())
graph = []

for i in range(E):
  start, end, price = map(int, input().split())
  graph.append((start, end, price))

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a > b:
    parent[a] = b
  else:
    parent[b] = a

def kruskal(V, graph):
  parent = [i for i in range(V + 1)]
  graph.sort(key=lambda x :x[2])

  total_cost = 0

  for start, end, price in graph:
    if find_parent(parent, start) != find_parent(parent, end):
      union_parent(parent, start, end)
      total_cost += price
  
  return total_cost


print(kruskal(V, graph))


