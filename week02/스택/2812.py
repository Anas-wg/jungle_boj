import sys
input = sys.stdin.readline

N, K = map(int,input().split())
digits = input().rstrip()
digits = list(map(int, digits))

stack = []

for digit in digits:
  # 스택이 비어있지 않고, TOP이 들어올 수(digit) 보다 작고, K가 남아있을 때
  while (len(stack) > 0 and stack[-1] < digit and K > 0):
    stack.pop() # 원소제거
    K -= 1 # POP 했으니 1 차감
  stack.append(digit) # 나머지는 스택에 PUSH

result = ''.join(map(str, stack))
result = int(result)
print(result)