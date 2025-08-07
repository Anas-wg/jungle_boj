N, M, K = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
print(array)

first = array[-1]
second = array[-2]

answer = 0

while(True):
  for i in range(K):
    if M == 0:
      break
    answer += first
    M -= 1
  if M == 0:
    break
  answer += second
  M -= 1

print(answer)
