N = int(input())
plan = input().split()

dx, dy = [
  [0, 0, -1, 1],
  [-1, 1, 0, 0]
]

moves = ['L', 'R', 'U', 'D']

cur_x = 1
cur_y = 1

for i in range(len(plan)):
  for j in range(4):
    if plan[i] == moves[j]:
      nx = cur_x + dx[j]
      ny = cur_y + dy[j]
  # 공간 벗어날 경우 예외처리
  if nx < 1 or nx > N or ny < 1 or ny > N:
    continue
  cur_x = nx
  cur_y = ny

print(nx, ny)