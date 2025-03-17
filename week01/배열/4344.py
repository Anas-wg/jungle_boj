# 평균을 넘는 학생들의 비율 계산
import sys
input = sys.stdin.readline

C = int(input())
for i in range(C):
  test_case = list(map(int, input().split()))
  students_pax = test_case[0]
  total = sum(test_case) - students_pax
  avg = total / students_pax
  over_avg = 0
  for case in test_case[1:]:
    if case > avg:
      over_avg += 1
# 포맷팅 주의
  print("%0.3f%%" %((over_avg / students_pax) * 100))
