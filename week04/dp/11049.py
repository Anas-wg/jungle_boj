import sys

input = sys.stdin.readline

n = int(input())
matrices = [tuple(map(int, input().split())) for _ in range(n)]

# DP 테이블 초기화
dp = [[0] * n for _ in range(n)]

# 체인 길이 l (2부터 n까지)
for l in range(2, n + 1):
    for i in range(n - l + 1):
        j = i + l - 1
        dp[i][j] = float('inf')

        for k in range(i, j):
            cost = (
                dp[i][k] + dp[k + 1][j]
                + matrices[i][0] * matrices[k][1] * matrices[j][1]
            )
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][n - 1])
