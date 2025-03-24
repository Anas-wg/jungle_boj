import sys
from collections import deque
input = sys.stdin.readline

card = deque([])
N = int(input())

for i in range(1, N + 1):
  card.append(i)


while len(card) > 1:
  # 제일 위의 카드 버리기
  card.popleft()
  # 그 다음 위 카드 뽑기
  first = card.popleft()
  # 바닥으로 옮기기 
  card.append(first)


print(card[0])