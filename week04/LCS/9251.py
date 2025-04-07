

import sys
input = sys.stdin.readline

str_A = input().rstrip()
str_B = input().rstrip()

def LCS(str_A, str_B):
  M, N = len(str_A), len(str_B)
  LCS = [[0] * (N + 1) for _ in range(M + 1)]
  
  for i in range(1, M + 1):
    for j in range(1, N + 1):
      if str_A[i - 1] == str_B[j - 1]:
        LCS[i][j] = LCS[i - 1][j - 1] + 1
      else:
        LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
  return LCS[M][N]

print(LCS(str_A, str_B))
      
    