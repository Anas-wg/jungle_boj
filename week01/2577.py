# A * B * C 의 결과에 1 ~ 9 가 몇 번 쓰였는지를 출력
import sys
input = sys.stdin.readline
# 입력 받기
A = int(input())
B = int(input())
C = int(input())

# A * B * C 곱셈 연산
result = A * B * C
result_digits = list(str(result))
result_digits = map(int, result_digits)
answer_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 각 숫자가 몇번 쓰였는지 어떻게 계산?
# 1. 조건문 활용해서 1 ~ 9 전부 확인 => 숫자해당하는 idx 증가
for digit in result_digits:
  answer_list[digit] += 1

for answer in answer_list:
  print(answer)

