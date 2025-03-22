import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input()) 
A_list = list(map(int, input().split())) 
M = int(input()) 
M_list = list(map(int, input().split())) 

A_list.sort() 

# def binary_search(target, start, end):
#   if start > end:
#     return 0
  
#   mid = (start + end) // 2

#   if A_list[mid] == target:
#     return 1
#   elif A_list[mid] > target:
#     end = mid - 1
#   else:
#     start = mid + 1

#   return binary_search(target, start, end)

def binary_search(target, data):
  start = 0
  end = len(data) - 1

  while start <= end:
    mid = (start + end) // 2 
    if data[mid] == target:
      return 1
    elif data[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return 0


for elems in M_list:
  print(binary_search(elems, A_list))