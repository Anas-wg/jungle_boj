# 연산을 사용하는 최소 횟수
# Base Case
# 관계
# dp[i] = min(dp[i - 1], dp[i / 3], dp[i / 2])

N = int(input())

if N == 1:
  print(0)
  exit()
elif N <= 3:
  print(1)
  exit()

dp = [0] * (N + 1)
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N + 1):
  if i % 2 == 0 and i % 3 == 0:
    dp[i] = min(dp[i // 2], dp[i // 3]) + 1
  elif i % 2 == 0:
    dp[i] = min(dp[i // 2], dp[i - 1]) + 1
  elif i % 3 == 0:
    dp[i] = min(dp[i // 3], dp[i - 1]) + 1
  else:
    dp[i] = dp[i - 1]  + 1


print(dp[N])