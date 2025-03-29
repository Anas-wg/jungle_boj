def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]
	
def union_parent(parent, a, b):
	a = find_parent(parent, a) # a의 부모 노드 찾기
	b = find_parent(parent, b) # b의 부모 노드 찾기
	# 더 큰 번호에 해당하는 노드의 부모를 작은 노도로 변경
	if a < b:
		parent[b] = a	
	else:
		parent[a] = b

V, E = map(int, input().split())
parent = [0] * (V + 1) # 부모테이블

for i in range(1, V + 1):
	parent[i] = i # 자기 자신으로 부모 초기화
	
is_cycle = False


for i in range(E): # 간선 하나씩 체크
	a, b = map(int, input().split())
	# 사이클 발생시 종료
	if find_parent(parent, a) == find_parent(parent, b):
		is_cycle = True
		break
  # 사이클 없다면 Union 수행
	else:
		union_parent(parent, a, b)
