# 점수, O 가 연속된 개수, 총 점수 구하기
import sys
input = sys.stdin.readline

T = int(input().rstrip())

for i in range(T):
  results = list(input())
  score = 0
  rows = []
  for result in results:
    if result == "O":
      rows.append(result)
      score += len(rows)
    else:
      rows = []
  print(score)
