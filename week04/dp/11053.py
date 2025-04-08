# O(N^2)
N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N

for i in range(N): # i가 가장 끝 점
  for j in range(i): # i보다 앞에 있는 모든 j
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
