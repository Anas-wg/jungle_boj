import sys
input = sys.stdin.readline

def dp(N, coin, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # 0원을 만드는 경우의 수는 항상 1가지 (동전 안 씀)
    for i in range(N + 1):
        dp[i][0] = 1

    for i in range(1, N + 1):  # i번째 동전까지 사용할 때
        for price in range(1, M + 1):  # price 원을 만들기
            dp[i][price] = dp[i - 1][price]  # i번째 동전 안 쓰는 경우
            if price - coin[i - 1] >= 0:
                dp[i][price] += dp[i][price - coin[i - 1]]  # i번째 동전 쓰는 경우

    return dp[N][M]

T = int(input())
for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    print(dp(N, coin, M))
