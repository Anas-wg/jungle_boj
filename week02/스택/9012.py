# ( => push, ) => pop
# 스택에 뭐라도 남아있다면 No, 없으면 YES

import sys
input = sys.stdin.readline

T = int(input().rstrip())

for i in range(T):
  stack = []
  str = list(input().rstrip())
  is_VPS = True

  for char in str:
    if char == "(":
      stack.append("(")
    else:
      if len(stack) == 0:
        is_VPS = False
        break
      else:
        stack.pop()
  if len(stack) > 0:
    is_VPS = False

  print("YES" if is_VPS  else "NO")
  