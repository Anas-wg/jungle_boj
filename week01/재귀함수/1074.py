# 1. 입력받기

N, R, C = map(int, input().split())
square = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]

# # 2. Z 탐색 진행
# def z_search(N, square):
#   if N == 1:
#     for i in range(2 ** N):