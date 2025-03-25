import sys
import heapq
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    start, end = map(int, input().split())
    if start > end: 
        start, end = end, start
    arr.append((start, end))

L = int(input())

sorted_arr = sorted(arr, key=lambda x: x[1])

# 최대 카운트를 저장할 변수
max_count = 0
queue = deque()

for start, end in sorted_arr:
    # 현재 end - L 보다 start가 작은 것들을 제외 (왼쪽으로 밀려난 것들 제거)
    while queue and queue[0][0] < end - L:
        queue.popleft()
    
    # 큐에 추가
    queue.append((start, end))
    
    # 최대 값 갱신
    max_count = max(max_count, len(queue))

# 결과 출력
print(max_count)
