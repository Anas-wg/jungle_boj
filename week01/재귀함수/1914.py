# 이동 횟수가 최소인 경우
# K : 이동 횟수, A, B는 이동 과정
# N 이 20보다 크면 과정 출력 필요 없음

# hanoi(N, start, end, sub) => N개의 원판을 start에서 end로 이동
# 이 과정에서 1 -> 2 로 n - 1 만큼 이동
# n 번째 원판을 1 -> 3 으로 이동
# 다시 2에 있던 n - 1 의 원판을 2 -> 3 이동
N = int(input())
moving_count = 2 ** N - 1

def move(start, end):
  print(start, end)

# start : 1, end :3 sub : 2
def hanoi(N, start, end, sub):
  if N == 1:
    move(start, end)
  else:
    hanoi(N - 1, start, sub, end)
    move(start, end)
    hanoi(N - 1, sub, end, start)

if N <= 20:
  print(moving_count)
  hanoi(N, 1, 3, 2)
else:
  print(moving_count)
