from itertools import permutations
import sys
input = sys.stdin.readline
# 1. 입력받기
N = int(input())
permut = list(permutations(range(1, N)))   # 도시 방문 순서 순열로 완전탐색
cities = []

for i in range(N):
  city_list = list(map(int, input().split()))
  cities.append(city_list)
# 2. 최소값 할당할 변수 선언
min_cost = float('inf') # 무한대로 아싸리 큰 값 설정

# 출발지, 리스트를 인자로 받는 함수
# Cycle 도는 모든 경로 계산(순열로) => 각 경로마다 가격을 리턴
# Cycle => 출발지 => 출발지 + 모든 노드 방문

for perm in permut:
  total_cost = 0 # 각 경로별 비용
  valid = True
  
  # 출발점은 0 
  start = 0
  for next_city in perm:
    if cities[start][next_city] == 0:
      valid = False
      break
    total_cost += cities[start][next_city]
    start = next_city # 이동한 도시를 다시 출발점으로
  
  # Cycle 이니 마지막 방문도시에서 다시 돌아가야함
  if valid and cities[start][0] != 0:
    total_cost += cities[start][0]
    min_cost = min(min_cost, total_cost)

print(min_cost)