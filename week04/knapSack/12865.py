import sys
input = sys.stdin.readline

N, K = map(int, input().split())

cost = []
for _ in range(N):
  W, V = map(int, input().split())
  cost.append((W, V))


dp = [[0] * (K + 1) for _ in range(N + 1)]
cost.sort()

for i in range(1, N + 1): 
  for j in range(1, K + 1): # 무게
    if j >= dp[i - 1][0]: # 현재 최대 무게가 해당 물건의 무게 보다 큰 경우
      dp[i][j]