N, M = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * M for _ in range(N)]

x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문 처리

maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

# 0 북 1 동 2 남 3 서 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전 정의
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0  # 회전 횟수
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 맵의 범위를 벗어낫다면 무시
    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        turn_time += 1
    # 회전한 이후 정면에 가보지 않은 육지 칸이 존재하는 경우 이동
    elif d[nx][ny] == 0 and maps[nx][ny] == 0:
        d[nx][ny] = 1  # 방문처리
        x = nx
        y = ny
        count += 1
        turn_time = 0  # 이동하면 회전 횟수 초기화
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if nx >= 0 and ny >= 0 and nx < N and ny < M:
            # 뒤로 갈 수 있다면 이동하기
            if maps[nx][ny] == 0:
                x = nx
                y = ny
            # 뒤가 바다로 막혀있는 경우
            else:
                break
        else:
            break
        turn_time = 0

print(count)