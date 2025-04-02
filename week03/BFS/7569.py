from collections import deque
import sys
input = sys.stdin.readline

# 입력
M, N, H = map(int, input().split())  # 가로(M), 세로(N), 높이(H)
graph = []

for _ in range(H):
    floor = []
    for _ in range(N):
        floor.append(list(map(int, input().split())))
    graph.append(floor)

# 이동 방향: 상, 하, 좌, 우, 위, 아래
dh = [0, 0, 0, 0, 1, -1]  # 높이 방향
dy = [-1, 1, 0, 0, 0, 0]  # 세로 방향
dx = [0, 0, -1, 1, 0, 0]  # 가로 방향

queue = deque()

# 익은 토마토(1)의 위치를 먼저 큐에 넣기
for h in range(H):
    for y in range(N):
        for x in range(M):
            if graph[h][y][x] == 1:
                queue.append((h, y, x))

# BFS
# 1(익은 토마토)에서 출발, 0인 칸을 며칠 만에(몇번 만에) 도달하는 가.
while queue:
    h, y, x = queue.popleft()

    for i in range(6):
        nh = h + dh[i]
        ny = y + dy[i]
        nx = x + dx[i]
        # 범위 벗어나지 않는 것들만 넣기
        if 0 <= nh < H and 0 <= ny < N and 0 <= nx < M:
            if graph[nh][ny][nx] == 0: # 새로 이동한 곳이 0이라면
                graph[nh][ny][nx] = graph[h][y][x] + 1 # 익은 날짜를 기록
                queue.append((nh, ny, nx))

# 결과 확인
max_day = 0
for h in range(H):
    for y in range(N):
        for x in range(M):
            if graph[h][y][x] == 0: # 0이 있으면 -1 만나서 안익는 거
                print(-1) # 안익음을 표시하는 -1
                sys.exit(0) # 출력후 아예 종료
            max_day = max(max_day, graph[h][y][x]) # 가장 오래 걸린 날짜 뽑기

print(max_day - 1)
