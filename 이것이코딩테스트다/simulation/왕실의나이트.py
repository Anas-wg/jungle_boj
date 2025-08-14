start = input()
row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
cur_col = int(row.index(start[0]) + 1)
cur_row = int(start[1])

print(cur_col, cur_row)

dx = [-1 ,1, -2 ,2, 2, -2, -1, 1]
dy = [-2, 2, -1, 1, -1, 1, 2, -2]

answer = 0

for i in range(8):
  nx = cur_col + dx[i]
  ny = cur_row + dy[i]
  if nx > 0 and nx <= 8 and ny > 0 and ny <= 8:
    answer += 1

print(answer)