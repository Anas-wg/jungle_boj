# 1. 입력받고 그래프 구현
# 2. 그래프 순회 함수 구현
# 3. 순회결과 리턴
import sys
input = sys.stdin.readline

N = int(input())
graph = {} # 키가 문자열이니까 dict 로 가자

for i in range(1, N + 1):
    node, left, right = input().split()
    
    if left == '.':
        left = None
        
    if right == '.':
        right = None
        
    graph[node] = (left, right)

print(graph)

def preorder(graph, node, visited):
    if node is None:
        return
    visited.append(node)
    preorder(graph, graph[node][0], visited)
    preorder(graph, graph[node][1], visited)

def inorder(graph, node, visited):
    if node is None:
        return
    inorder(graph, graph[node][0], visited)
    visited.append(node)
    inorder(graph, graph[node][1], visited)

def postorder(graph, node, visited):
    if node is None:
        return
    postorder(graph, graph[node][0], visited)
    postorder(graph, graph[node][1], visited)
    visited.append(node)

    

visited_pre = []
preorder(graph, 'A', visited_pre)

visited_in = []
inorder(graph, 'A', visited_in)

visitied_post = []
postorder(graph, 'A', visitied_post)

print(''.join(visited_pre))
print(''.join(visited_in))
print(''.join(visitied_post))