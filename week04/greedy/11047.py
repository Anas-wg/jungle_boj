# 그리디
# N : 동전 종류
# 그 동전을 적절히 사용해서 K 만들기
# 구할 것 : 필요한 동전 개수의 최솟값
# K 보다 작은 것중 제일 큰 것부터 골라야 최소한의 지폐로 가능

import sys
input = sys.stdin.readline

N, K = map(int ,input().split())
coins = [int(input().rstrip()) for _ in range(N)]

# K 보다 작은 것들 다 없애기
under_coin = []

for coin in coins:
  if coin <= K:
    under_coin.append(coin)

under_coin.sort()

# 하나씩 뽑아서 가장 많이 쓰기
total = K
answer = 0
while total != 0:
  coin = under_coin.pop()
  cnt = total // coin
  if total - (coin * cnt) >= 0:
    total -= coin * cnt
    answer += cnt
  else:
    continue

print(answer)