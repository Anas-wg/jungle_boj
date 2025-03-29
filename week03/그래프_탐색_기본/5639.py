# 1. 입력받기
# 2. 전위순회 순서로 
# 가장 첫번째 원소가 Root, 그거 보다 작은건 왼쪽 서브, 큰건 오른쪽 서브
# 3. 후위 순회로 변경
# 왼쪽 서브 - 오른쪽 서브 - 루트 순


import sys
sys.setrecursionlimit(10**6)
num_list = []

while True:
  num = sys.stdin.readline().strip()
  if num == '':
    break
  else:
    num_list.append(int(num))

def pre_to_post(list):
  if not list:
    return
  root = list[0]
  left_sub = []
  right_sub = []

  for elems in list[1:]:
    if elems < root:
      left_sub.append(elems)
    else:
      right_sub.append(elems)
  
  pre_to_post(left_sub)
  pre_to_post(right_sub)

  print(root)


pre_to_post(num_list)
