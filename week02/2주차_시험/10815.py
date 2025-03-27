# 1. 입력받기
# 2. 상근이 카드, 비교 숫자 리스트 정렬
# 3. M개 각 숫자에 해당하는 카드 있는지 이분 탐색
# 3-1. bisect...? 직접구현...? 해시로 푸는게 빠를듯 한데 구현 못할듯
# 4. 카드 있다면 1을, 없다면 0을 리턴



import sys
input = sys.stdin.readline

N = int(input())
sangeun = sorted(list(map(int, input().split())))
M = int(input())
num_list = list(map(int, input().split()))

start = 0
end = len(sangeun) - 1

def binary_search(arr, start, end, target):
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] > target: # mid 기준 왼쪽에 target 위치
      end = mid - 1
    elif arr[mid] == target:
      return 1
    else:
      start = mid + 1
  return 0


for num in num_list:
  print(binary_search(sangeun,start, end, num), end=' ')

# 다른 풀이 -> Set vs list (왜 시간초과가 나는가?)