import sys
input = sys.stdin.readline

first = int(input().rstrip())
second = int(input().rstrip())

second_digit = []
for i in str(second):
  second_digit.append(int(i))
# 3 -> (1)과 (2)의 1의 자리
print(first * second_digit[-1])
# 4 -> (1)과 (2)의 10 의 자리
print(first * second_digit[-2])
# 5 -> (1)과 (2)의 100의 자리
print(first * second_digit[-3])
# 6 -> (1) * (2)의 곱셈 연산 값
print(first * second)


#### 단순

a = int(input())  
b = input()

print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))