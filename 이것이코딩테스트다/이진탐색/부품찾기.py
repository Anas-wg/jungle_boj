N = int(input())
N_list = sorted(list(map(int, input().split())))

M = int(input())
M_list = list(map(int, input().split()))

def binary_search(array, start, end, target):
  if start > end:
    return "No"
  mid = (start + end) // 2
  if array[mid] == target:
    return "yes"
  elif array[mid] > target:
    return binary_search(array, start, mid - 1, target)
  else:
    return binary_search(array, mid+1, end, target)


answer = []

for elem in M_list:
    print(binary_search(N_list, 0, N - 1, elem), end=' ')

# 계수정렬 풀이

array = [0] * 100001

for elem in N_list:
  array[elem] = 1

for elem in M_list:
  if array[elem] == 1:
    print('yes')
  else:
    print('No')