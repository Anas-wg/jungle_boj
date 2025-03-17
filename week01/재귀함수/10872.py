# N! 을 출력하는 프로그램 입력
import sys
input = sys.stdin.readline

N = int(input())

def factorial(N):
  if N <= 1:
    return 1
  else:
    return factorial(N - 1) * N

print(factorial(N))