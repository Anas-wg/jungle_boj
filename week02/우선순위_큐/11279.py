import heapq
import sys
input= sys.stdin.readline


heap_items = []

N = int(input())

for i in range(N):
  num = int(input())
  if num == 0:
    if len(heap_items) == 0:
      print(0)
    else:
      print(heapq.heappop(heap_items)[1])
  else:
    heapq.heappush(heap_items, (-num, num))
