def matrix_chain_order(dimensions):
    num_matrices = len(dimensions) - 1
    min_cost = [[0] * (num_matrices + 1) for _ in range(num_matrices + 1)]
    split_point = [[0] * (num_matrices + 1) for _ in range(num_matrices + 1)]

    for chain_length in range(2, num_matrices + 1):
        for start in range(1, num_matrices - chain_length + 2):
            end = start + chain_length - 1
            min_cost[start][end] = float('inf')
            for mid in range(start, end):
                cost = (
                    min_cost[start][mid]
                    + min_cost[mid + 1][end]
                    + dimensions[start - 1] * dimensions[mid] * dimensions[end]
                )
                if cost < min_cost[start][end]:
                    min_cost[start][end] = cost
                    split_point[start][end] = mid
    return min_cost, split_point


def print_optimal_parens(split_point, start, end):
    if start == end:
        print(f"A{start}", end='')
    else:
        print("(", end='')
        k = split_point[start][end]
        print_optimal_parens(split_point, start, k)
        print_optimal_parens(split_point, k + 1, end)
        print(")", end='')


# 예제 실행
if __name__ == "__main__":
    p = [30, 35, 15, 5, 10, 20, 25]
    m, s = matrix_chain_order(p)

    print("📌 최적 곱셈 수 (최소 연산 수):", m[1][len(p) - 1])
    print("🧩 최적 괄호 묶기:")
    print_optimal_parens(s, 1, len(p) - 1)

"""
행렬: A1 × A2 × A3 × A4 × A5 × A6
차원: [30, 35, 15, 5, 10, 20, 25]

      A1: 30x35
      A2: 35x15
      A3: 15x5
      A4: 5x10
      A5: 10x20
      A6: 20x25

-------------------------------------------------

s[1][6] = 3 → A1~A3 | A4~A6 로 나눔
  s[1][3] = 2 → A1~A2 | A3
    s[1][2] = 1 → A1 | A2
  s[4][6] = 5 → A4~A5 | A6
    s[4][5] = 4 → A4 | A5

괄호로 묶이면:
→ ((A1(A2A3))((A4A5)A6))

-------------------------------------------------

m[1][6] = 15125 → 최소 연산 수
"""
