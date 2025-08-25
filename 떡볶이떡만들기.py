import sys
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
array = sorted(list(map(int, input().split())))

def cut(H):
  result = 0
  for elem in array:
    if elem < H:
      continue
    else:
      result += M - elem
  return result



def search_H():
  mid = (array[0] + array[-1]) // 2

  if cut(mid) == M:
    return mid
  
  while 



