N = int(input())
count = 0
pos = [0] * N
flag_col = [False] * N
flag_diagonal_up = [False] * (2 * N - 1)
flag_diagonal_down = [False] * (2 * N - 1)

def put():
    global count
    count += 1

def solve(row):
    if row == N:  # 모든 행에 대해 퀸을 놓았으면 카운트 증가
        put()
        return
    
    for col in range(N):
        if not flag_col[col] and not flag_diagonal_up[row + col] and not flag_diagonal_down[row - col + (N - 1)]:
            pos[row] = col
            flag_col[col] = flag_diagonal_up[row + col] = flag_diagonal_down[row - col + (N - 1)] = True
            solve(row + 1)  # 다음 행으로 이동
            flag_col[col] = flag_diagonal_up[row + col] = flag_diagonal_down[row - col + (N - 1)] = False  # 백트래킹

solve(0)
print(count)
