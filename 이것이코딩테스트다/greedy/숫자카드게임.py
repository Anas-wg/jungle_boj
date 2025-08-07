N, M = map(int, input().split())
card = []
for i in range(N):
  card.append(sorted(list(map(int, input().split()))))

card.sort()
print(card[-1][0])