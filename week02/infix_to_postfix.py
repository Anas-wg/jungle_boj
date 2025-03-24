def infix_to_postfix(expression):
    # 우선순위 설정
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '(': 0  # 여는 괄호는 가장 낮은 우선순위로 설정
    }
    
    stack = []
    result = []

    for char in expression:
        if char not in precedence and char != ')':  # 피연산자라면 (연산자가 아니라면)
            result.append(char)
        
        elif char == '(':  # 여는 괄호는 그냥 스택에 넣기
            stack.append(char)
        
        elif char == ')':  # 닫는 괄호라면 여는 괄호까지 팝
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # 여는 괄호 '(' 제거
        
        else:  # 연산자일 때
            while stack and precedence[stack[-1]] >= precedence[char]:
                result.append(stack.pop())
            stack.append(char)  # 현재 연산자를 스택에 추가

    # 스택에 남아있는 연산자를 결과로 추가
    while stack:
        result.append(stack.pop())
    
    return ''.join(result)  # 리스트를 문자열로 변환하여 반환

# 테스트 예제
expression = "A+B*C-(D/E)"
print(expression)
print(infix_to_postfix(expression))  # 결과: ABC*+DE/-
