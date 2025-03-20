# ( => push, ) => pop
# 스택에 뭐라도 남아있다면 No, 없으면 YES

import sys
input = sys.stdin.readline

T = int(input().rstrip())

for i in range(T):
  stack = []
  str = list(input().rstrip())
  