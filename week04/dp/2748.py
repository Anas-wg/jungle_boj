# n이 주어졌을때 n 번째 피보나치 수를 구하는 프로그램?
N = int(input())
# Top-down
def fibo_top_down(n, memo):
    # Memoization 위한 배열 초기화
    if not memo:
        memo = [-1] * (n + 1)

    # Base Case
    if n <= 1:
        return n
    # 만약 계산해둔 값이 있다면 리턴
    if memo[n] != -1:
        return memo[n]
    # 처음 계산이라면 재귀호출 후 memoizaion
    memo[n] = fibo_top_down(n - 1, memo) + fibo_top_down(n - 2, memo)
    return memo[n]
print(fibo_top_down(N, []))


def fibo_bottom_up(N):
    if N == 0:
        return 0
    memo = [0] * (N + 1) # 테이블
    memo[0] = 0
    memo[1] = 1

    for i in range(2, N + 1):
        memo[i] = memo[i - 1] + memo[i - 2] # Table 채우기
    return memo[N]

print(fibo_bottom_up(N))