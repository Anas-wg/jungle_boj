# 수 정렬하기 2 N이 1에 비해 더 커짐
# N <= 1,000,000 이기에, O(N^2)의 시간 복잡도 쓰는 방식은 틀림
import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for i in range(N):
  number = int(input())
  num_list.append(number)

for num in sorted(num_list):
  print(num)