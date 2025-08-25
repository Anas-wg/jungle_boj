# 재귀 버전
def binary_search(array, start, end, target):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    binary_search(array, start, mid -1, target)
  else:
    binary_search(array,mid+1,end,target)

# 반복문 버전
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid -1
    else:
      start = mid + 1
  return None
