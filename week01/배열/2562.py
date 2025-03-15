# 9개의 자연수 중 최댓값 찾고 몇번째 수 인지 구하기
import sys
input = sys.stdin.readline


num_list = []
for i in range(9):
  num = int(input())
  num_list.append(num)

max_val = max(num_list)

print(max_val)
print(num_list.index(max(num_list)) + 1)
