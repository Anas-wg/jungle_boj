# N th 줄마다 N개의 별 출력
import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N + 1):
  print("*" * i)
