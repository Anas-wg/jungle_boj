import sys
input = sys.stdin.readline

N, K = map(int, input().split())

items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = items[i - 1]  # 현재 물건의 무게와 가치
    for j in range(1, K + 1):  # 현재 배낭 무게
        if j < weight:
            dp[i][j] = dp[i - 1][j]  # 물건 못 넣음
        else:
            dp[i][j] = max(
                dp[i - 1][j],  # 안 넣은 경우
                dp[i - 1][j - weight] + value  # 넣은 경우 , 무게 차감
            )

print(dp[N][K])  # 최대 가치 출력
