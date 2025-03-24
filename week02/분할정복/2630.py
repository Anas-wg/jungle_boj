import sys
input = sys.stdin.readline

# 1. 입력받기
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

result = []

def solution(a, b, N):
  color = paper[a][b]
  for i in range(a, a + N):
    for j in range(b, b + N):
      if color != paper[i][j]:
        solution(a, b, N // 2)
        solution(a, b + N // 2, N // 2)
        solution(a + N // 2, b, N // 2)
        solution(a + N // 2 , b + N // 2, N // 2)
        return
  if color == 0:
    result.append(0)
  else:
    result.append(1)
  
solution(0, 0, N)
print(result.count(0))
print(result.count(1))


