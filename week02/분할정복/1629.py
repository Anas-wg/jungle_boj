import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def program(A, B, C):
  if B == 1:
    return A % C
  
  X = program(A, B // 2, C)

  if (B % 2 == 0):
    return X & X % C
  else:
    return A * X * X % C
  

print(program(A, B, C)) 
