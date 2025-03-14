# V 미터인 나무 막대를 A미터 올라가고 B 미터 미끄러질때 얼마나 걸리는가
import sys
input = sys.stdin.readline
# 입력받기
A, B, V = map(int, input().split())
# 현재 위치가 V에 도달할때까지 +A, -B 과정 몇번 반복하는지
cur_location = 0
days = 1

while cur_location == V:
  cur_location += A
  cur_location -= B
  days += 1

print(days)
