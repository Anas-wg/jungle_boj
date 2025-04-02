from itertools import permutations
import sys
input = sys.stdin.readline

def dfs(n, sum, add, sub, mul, div):
  global mn, mx
  
  if n == N :
    mn = min(mn, sum)
    mx = max(mx, sum)
    return
  
  # 연산자 개수 있다면 하부 호출
  if add > 0: # 덧셈으로 가는 경우
    dfs(n+1, sum + num_list[n], add -1, sub, mul, div)
  if sub > 0: # 뺄셈으로 가는 경우
    dfs(n+1, sum - num_list[n], add, sub - 1, mul, div)
  if mul > 0: #곱셉으로 가는 경우
    dfs(n+1, sum * num_list[n], add, sub, mul - 1, div)
  if div > 0: # 나눗셈
    dfs(n+1, int(sum / num_list[n]), add, sub, mul, div - 1)


N = int(input()) # 숫자 개수
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

mn, mx = int(1e9), int(-1e9)

dfs(1, num_list[0], add, sub, mul, div)
print(mx, mn, end='\n')
