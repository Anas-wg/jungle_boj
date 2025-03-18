import sys
input = sys.stdin.readline

cities = []
price = []
N = int(input())
for i in range(N):
  cities.append(list(map(int, input().split())))

visited = [False] * N

# 가장 적은 비용 가진 도시 찾는 함수
def find_cheap(list):
  min_val = 10000
  min_idx = -1
  for i, price in enumerate(list):
    if price == 0:
      continue
    if price < min_val:
      min_val = price
      min_idx = i
  return min_val, min_idx

# print(find_cheap([0, 10, 15 ,20]))

for i in range(N):
  price, next_idx = find_cheap(cities[i])

