import sys
input = sys.stdin.readline

T = int(input())
num_list = [int(input().strip()) for _ in range(T)]

dp = [0] * 1000  # Increased size to be safe for larger numbers
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

max_num = max(num_list)
for i in range(4, max_num + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
 
for nums in num_list:
    print(dp[nums])
