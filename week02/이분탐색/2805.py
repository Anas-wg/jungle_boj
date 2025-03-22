# N : 나무 개수 (N <= 1,000,000)
# M : 집으로 가져가야하는 나무의 길이
# H : 톱날의 높이 (H <= 2,000,000,000)
# 구해야 할 것 : M미터의 나무를 집에 가져가기 위한 H의 최댓값
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree_list = list(map(int, input().split())) 

# tree_list.sort() 
start = 0 # 4
end = max(tree_list)

# 첫 임시 톱날 높이(temp_h) => (start + end) // 2
# temp_h로 잘랐을때 나오는 나무 길이인 temp_M.
# temp_M > M 일경우, 톱날의 높이는 더 높아야함, 따라서 temp_H ~ end까지
# temp_M < M 일경우 톱날의 높이는 더 낮아야함, 따라서 low ~ temp_H까지

def binary_search(data, start, end):
  temp_h = (start + end) // 2 # 4 + 46 // 2 => 25
  temp_M = 0
  if start > end: # 나중에 34 35일 경우 종료조건으로 진행
    return end
  
  for tree in data:
    if temp_h > tree:
      continue
    else:
      temp_M += tree - temp_h
    
  if temp_M == M:
    return temp_h
  elif temp_M > M:
    return binary_search(data, temp_h + 1, end)
  else:
    return binary_search(data, start, temp_h -1)
  

print(binary_search(tree_list, start, end))