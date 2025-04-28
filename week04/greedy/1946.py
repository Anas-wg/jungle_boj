# 

import sys
input = sys.stdin.readline

T = int(input())

result = []
def hire_process(arr):
  answer = 1
  cur_1, cur_2 = arr.pop()
  while arr:
    next_1, next_2 = arr.pop()
    if cur_2 > next_2:
      answer += 1
      cur_1, cur_2 = next_1, next_2
  result.append(answer)



for _ in range(T):
  N = int(input())
  arr = [tuple(map(int, input().split())) for _ in range(N)]
  hire_process(sorted(arr, key=lambda x: (x[0], x[1]), reverse= True))

for elems in result:
  print(elems)