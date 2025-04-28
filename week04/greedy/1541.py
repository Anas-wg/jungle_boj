# 1. 입력받기
# 입력을 어떻게 받냐
# 2. 빼기가 없다면 그냥 더한 값이 최소
# 3. 빼기가 있다면 빼기 다음 수부터 끝까지 전부 음수로 전환

expr = input()

parts = expr.split('-')

total = sum(map(int, parts[0].split('+')) )

for part in parts[1:]:
  total -= sum(map(int, part.split('+')))

print(total)