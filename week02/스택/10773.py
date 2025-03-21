import sys
input = sys.stdin.readline

K = int(input())
wallet = []
for i in range(K):
  num = int(input())
  if num == 0:
    wallet.pop()
  else:
    wallet.append(num)

print(sum(wallet))
