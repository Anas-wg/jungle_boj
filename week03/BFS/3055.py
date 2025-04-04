import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[-1] * C for _ in range(R)]

water_q = deque()
hedgehog_q = deque()

for y in range(R):
    for x in range(C):
        if graph[y][x] == '*':
            water_q.append((y, x))
        elif graph[y][x] == 'S':
            hedgehog_q.append((y, x))
            visited[y][x] = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while hedgehog_q:
    # 먼저 물 퍼뜨리기
    for _ in range(len(water_q)):
        y, x = water_q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if graph[ny][nx] == '.':
                    graph[ny][nx] = '*'  # 물로 확산
                    water_q.append((ny, nx))

    # 그다음 고슴도치 이동
    for _ in range(len(hedgehog_q)):
        y, x = hedgehog_q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if graph[ny][nx] == 'D':  # 비버 굴 도착
                    print(visited[y][x] + 1)
                    sys.exit(0)
                if graph[ny][nx] == '.' and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    hedgehog_q.append((ny, nx))

# 여기까지 왔다면 도달 실패
print("KAKTUS")
