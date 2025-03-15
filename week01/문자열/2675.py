# 문자열 S를 각 문자를 R번 반복해서 새 문자열 P를 출력
import sys
input = sys.stdin.readline

# 입력받기
T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
# 문자열 쪼개기 -> 각 문자 R번 반복
    S = list(S)
    answer = ""
    for char in S:
      char_repeat = char * R
      answer += char_repeat
    print(answer)

