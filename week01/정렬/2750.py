# 수가 주어졌을때 오름차순으로 정렬
import sys
input = sys.stdin.readline
# from heapq import heappop, heappush

# def heap_sort(nums):
#     heap = []
#     for num in nums :
#        heappush(heap, num)
#     sorted_list = []
#     while heap:
#         sorted_list.append(heappop(heap))
#     return sorted_list

# def selection_sort(num_list):
#    n = len(num_list)
#    for i in range(0, n - 1):
#       min_idx = i
#       for j in range(i + 1, n):
#         if num_list[j] < num_list[min_idx]:
#             min_idx = j
#       num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]

N = int(input())
num_list = []
for i in range(N):
  number = int(input())
  num_list.append(number)


# result = heap_sort(num_list)

# selection_sort(num_list)

for num in sorted(num_list):
  print(num)