N, K = map(int, input().split())

array_A = list(map(int,input().split()))
array_B = list(map(int, input().split()))

array_A.sort()
array_B.sort(reverse=True)

for i in range(K):
  array_A[i] = array_B[i]

print(sum(array_A))