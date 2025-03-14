import sys
input = sys.stdin.readline

year = int(input())

# 윤년 -> 4의 배수 이면서 100의 배수가 아닌 것 || 400의 배수인것

if year % 400 == 0:
  print(1)
elif year % 4 == 0 and year % 100 != 0:
  print(1)
else:
  print(0)  


# if ((year%4 == 0)and(year%100 != 0)) or (year%400 == 0):
# 이런식으로 하나로 묶어서 간다면 코드가 더 짧아질 듯

# 삼항연산자 활용
# print('1') if ((year%4 == 0)and(year%100 != 0)) or (year%400 == 0) else print('0')
