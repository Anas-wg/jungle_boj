# 두 인접한 공유기의 거리를 이진탐색으로 찾는 것
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
home = sorted([int(input()) for _ in range(N)])

start = 1
end = home[-1] - home[0]
answer = 0

def binary_search(list, start, end):
  global answer
  while start <= end:
    mid = (start + end) // 2
    cur = home[0] # 첫 집 주소
    installed = 1 # 첫집에 하나 기본으로 깔고 시작
    for i in range(1, N):
      if list[i] - cur >= mid: # mid보다 크거나 같은 거리 떨어진 곳에 설치
        installed += 1 
        cur = list[i] # 설치위치 갱신
    if installed >= C: # C의 개수보다 설치 개수가 많다면 
      answer = mid # answer 갱신
      start = mid + 1 # 1을 증가시켜 더 큰 값 확인
    else:
      end = mid - 1 # Mid가 너무 크기에 Mid값 감소

binary_search(home, start, end)

print(answer)
      
