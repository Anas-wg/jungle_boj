import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

heapq.heapify(arr)
total = 0  # 결과를 누적할 변수

while len(arr) > 1:
    first = heapq.heappop(arr)
    second = heapq.heappop(arr)
    
    count = first + second
    total += count  # 누적해서 합산
    
    heapq.heappush(arr, count)

print(total)
