stack = [] # 스택
temp = 1 # result에 더해주기 전 임시 변수
result = 0 # 결과 변수
string = list(input()) # 입력값

for i in range(len(string)):
  # 여는 괄호일 경우, 괄호 종류 따라 temp에 점수를 저장

  if string[i] == '(':
    temp *= 2
    stack.append(string[i])
  elif string[i] == '[':
    temp *= 3
    stack.append(string[i])
  # 둥근 닫힌 괄호일 경우
  elif string[i] == ')':
    if not stack or stack[-1] != '(': # 스택이 비었거나 짝이 안맞는 경우
      result = 0
      break # 나가리
    if string[i - 1] == '(': # 짝이 맞는 경우, 바로 앞이 열린 둥근 괄호
      result += temp
    temp //= 2 # temp 1로 원상 복구
    stack.pop()
  # 각진 닫힌 괄호
  elif string[i] == ']':
    if not stack or stack[-1] != '[': # 스택이 비었거나 짝이 안맞는 경우
      result = 0
      break # 나가리
    if string[i - 1] == '[': # 짝이 맞는 경우, 바로 앞이 닫힌 각진 괄호
        result += temp
    temp //= 3
    stack.pop()

# 다 맞아도 스택에 뭐가 남아있다면 짝 안맞으니 0
if stack:
  print(0)
else:
  print(result)


