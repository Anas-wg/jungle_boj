# 한수 -> 양의정수의 각 자리가 등차수열 일때
# 구해야 할 것 : 1 보다 크고 N 보다 작은 한수의 개수
import sys
input = sys.stdin.readline

# 1. 입력 받기 
N = int(input())
answer = []
# 등차수열 판단 함수
def is_hansu(list):
  if len(list) == 1:
    return True
  elif len(list) == 2:
    return True
  else:
    if list[0] - list[1] == list[1] - list[2]:
      return True
  return False

# 1 부터 N 까지 돌면서 한수 판단
for i in range(1, N + 1):
  digit_list = list(map(int, str(i)))
  digit_list.sort
  if is_hansu(digit_list):
    answer.append(digit_list)
    
print(answer)
print(len(answer))