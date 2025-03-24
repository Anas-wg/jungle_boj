import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
for i in range(1, N + 1):
  arr.append(i)

# K[idx: k - 1] 번째 사람이 짤리면, 그 다음 사람[k + 1 => 0] 이 1번째,

result = []

def yose_permu(arr):
  if len(arr) < K :
    # 만약 K보다 작더라도 계속 돌려야함.
    for elems in arr[: K]:
      result.append(elems)
    return 
  first = arr[ : K]
  result.append(first.pop())
  second = arr[K : ]
  arr = second + first
  yose_permu(arr)

yose_permu(arr)
print("<" + ", ".join(map(str, result)) + ">")

