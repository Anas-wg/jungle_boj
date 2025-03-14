# 두개의 숫자를 거꾸로 뒤집고, 이중 큰수를 리턴
import sys
input = sys.stdin.readline
# 입력받기
first, second = input().split()
# 숫자 뒤집기
# 숫자를 어떻게 뒤집어 줄까 -> slicing 활용
first = first[::-1]
second = second[::-1]

print(max(first, second))