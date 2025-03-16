# 개선 전
for i in range(a, b + 1):
  if i < b:
    print(f'{i} + ', end='')
  else: 
    print(f'{i} = ', end='')
  sum += i

# 개선 후 => i와 b에 대한 비교 없이 같은 연산 수행
for i in range(a, b):
  print(f'{i} + ', end='')
  sum += i

print(f'{i} = ', end='')
sum += b


