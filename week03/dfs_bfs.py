
graph = [
    [],         
    [2, 3, 8],   
    [1, 7],     
    [1, 4, 5],  
    [3, 5],      
    [3, 4],    
    [7],        
    [2, 6, 8],  
    [1, 7]      
]

# 재귀를 활용
def dfs (graph, v, visited):
  visited[v] = True # 방문처리
  print(v, end = ' ') # 출력
  for i in graph[v]: # 인접 리스트 방식일 경우
    if not visited[i]:
      dfs(graph, i, visited)
  # for i in range(len(graph[v])):
  #   if graph[v][i] == 1 and not visited[i]:
  #     dfs(graph, i, visited)

def dfs_stack(graph, start, visited):
    stack = [start]  # 스택에 시작 노드를 추가
    
    while stack:  # 스택이 빌 때까지 반복
        v = stack.pop()  # 스택의 가장 위에 있는 노드를 꺼냄

        if not visited[v]:  # 방문하지 않은 노드일 경우
            print(v, end=' ')  # 방문한 노드를 출력
            visited[v] = True  # 방문 처리

            # 현재 노드와 연결된 노드를 모두 스택에 추가 (역순으로 추가)
            for i in reversed(graph[v]):
                if not visited[i]:
                    stack.append(i)

visited = [False] * 9
dfs(graph, 1, visited)

from collections import deque

def bfs(graph, start, visited):
  # deque 모듈 활용한 큐 구현
  queue = deque([start])
  visited[start] = True # 현재 노드 방문 처리
  while queue:
    v = queue.popleft() # front 에서 원소 하나 뽑기
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

visited = [False] * 9
bfs(graph, 1, visited)