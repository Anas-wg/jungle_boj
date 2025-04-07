# Recursive
def cut_rod_recursive(price, n):
    if n == 0:
        return 0
    result = -float('inf')
    for i in range(1, n + 1):
        result = max(result, price[i - 1] + cut_rod_recursive(price, n - i))
    return result

# 사실상 재귀인데, 같은 문제를 다시 계산하지 않는 똑똑한 재귀
def cut_rod_memoized(price, n):
    memo = [-1] * (n + 1) # 값 저장해둘 배열

    def recurse(n):
        if n == 0:
            return 0
        if memo[n] >= 0: # 이미 저장된 값이 있다면 리턴
            return memo[n]
        result = -float('inf') # 없으면 계산 시작
        for i in range(1, n + 1):
            result = max(result, price[i - 1] + recurse(n - i)) # n 크기에서 n - 1 크기로 점점 내려옴
        memo[n] = result
        return result

    return recurse(n)

def cut_rod_bottom_up(price, n):
    # memo[0] ~ memo[n]까지 저장하는 DP 배열 (최대 수익 저장용)
    memo = [0] * (n + 1)

    for j in range(1, n + 1):  # 막대의 길이 j
        result = -float('inf')
        for i in range(1, j + 1):  # i는 첫 번째 자르는 위치
            result = max(result, price[i - 1] + memo[j - i])
        memo[j] = result  # 길이 j에 대한 최대 수익 저장

    return memo[n]

def extended_cut_rod_and_print(price, n):
    memo = [0] * (n + 1)  # 최대 수익 저장
    s = [0] * (n + 1)     # 자르는 위치 저장

    for j in range(1, n + 1):  # 막대 길이 j에 대해
        result = -float('inf')
        for i in range(1, j + 1):  # i는 자르는 위치
            if result < price[i - 1] + memo[j - i]:
                result = price[i - 1] + memo[j - i]
                s[j] = i  # 최적의 첫 조각 크기 저장
        memo[j] = result

    # 결과 출력
    print("최대 수익:", memo[n])
    print("자르기 순서:", end=' ')
    while n > 0:
        print(s[n], end=' ')
        n -= s[n]


