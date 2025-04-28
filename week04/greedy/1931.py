# 회의실 배정
import sys
input = sys.stdin.readline

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

# 끝나는 시간이 가장 빠르고, 그 후에 시작 시간 오름차순 까지 해야 그리디 전략 유지 가능
# 같은 종료시간이면 더 빨리 시작하는 회의부터 봐야함
meetings = sorted(meetings, key = lambda x : (x[1],x[0]), reverse=True )
answer = 1

cur_start, cur_end = meetings.pop() # 1 4


while meetings:
  next_start,next_end = meetings.pop()
  if cur_end <= next_start:
    cur_start, cur_end = next_start, next_end
    answer += 1

print(answer)  

