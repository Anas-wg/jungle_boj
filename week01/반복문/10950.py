# 구해야할 것 :  TestCase의 A + B 값
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
  A, B = map(int, input().split())
  print(A + B)
