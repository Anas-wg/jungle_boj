# 정수 N개 중 X 보다 작은 숫자 공백 구분 출력
import sys
input = sys.stdin.readline

N , X = map(int, input().split())
num_list = list(map(int, input().split()))

for num in num_list:
  if num < X:
    print(num, end=' ')