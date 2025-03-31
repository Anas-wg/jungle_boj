# 특정 노드와 연결된 노드 개수를 출력
# Union-Find 알고리즘 통해 해당 노드와 같은 부모 노드(대표)를 가진 원소 개수 출력
import sys
input = sys.stdin.readline

# 1. 입력받기 & 그래프 만들기
# 2. Union, Find 함수 정의
# 3. 모든 정점 Union-Find 실행
# 4. 1번 컴퓨터와 동일한 부모 노드를 갖는 노드 개수 출력

N = int(input()) # 컴퓨터 수
M = int(input())

parent = [i for i in range(N + 1)]

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a) 
  b = find_parent(parent, b)

  if a > b :
    parent[a] = b
  else:
    parent[b] = a

for i in range(M):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

target = find_parent(parent, 1)

answer = 0

for i in range(2, N + 1):
  if find_parent(parent, i) == target:
    answer += 1

print(answer)