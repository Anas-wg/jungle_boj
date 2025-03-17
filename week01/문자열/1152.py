# 문자열에 있는 단어의 개수
import sys
input = sys.stdin.readline

# 입력받기 -> 리스트로 전환 => length 출력
string = input().split()
print(len(string))

# 완전 탐색
# 단어 판단-=> 공백
# 글자당 공백을 만나면 
# 공백의 개수 + 1 => 단어의 개수