# 입력으로 주어지는 값을 아스키 코드로 변환
import sys
input = sys.stdin.readline

# sys 모듈은 개행문자 포함하기에 반드시 rstrip
val = input().rstrip()
# 아스키 코드로 출력하는 메서드 ord()
print(ord(val))