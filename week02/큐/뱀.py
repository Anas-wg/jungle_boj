import sys
input = sys.stdin.readline
# 구해야 할 것 : 게임 종료 소요 시간

# 1. 입력받기
N = int(input()) # 보드판 크기
K = int(input()) # 사과 개수
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input()) # 방향 전환 횟수
heading = [] # 방향 전환 정보 담는 배열

for _ in range(L):
  sec, C = input().split()
  heading.append([int(sec), C])


