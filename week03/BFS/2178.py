# 1 은 이동가능, 0은 이동불가
# (1,1) -> (N, M) => 이동하는데 인접한 칸으로만 이동 가능
# BFS 활용
# 인접한 칸 탐색, 1이라면 이동, 

# 1. 입력받기
# 2. BFS 구현 -> 인접노드를 넣을때 1이면 넣고 0이면 skip
# 3. (N, M) 도착시 시마이

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip()))) 

# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x, y):
    
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    
    return graph[n-1][m-1]

print(bfs(0,0))