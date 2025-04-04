# 시간 제한이 일단 0.75
# 
N = int(input())
def make_bi_tile(N):
  dp = [0] * (N + 1)
  if N == 1:
    return 1
  dp[1] = 1
  dp[2] = 2
  # 여기서 리턴 1을 하게 되면 dp[2] 때문에 idx 에러
  for i in range(3, N + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746 # 안에서 계속 나눈 나머지로 저장해야 정답
  return dp[N]


print(make_bi_tile(N))
