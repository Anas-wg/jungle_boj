# N, V
# Union Find 로 연결요소 판단하자
import sys
input = sys.stdin.readline

N, M = map(int, input().split())


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

parent = [i for i in range(N + 1)]

for i in range(M):

  a, b = map(int, input().split())
  union_parent(parent,a, b)


for i in range(2, N + 1):
  find_parent(parent, i)

print(len(set(parent)) - 1)
