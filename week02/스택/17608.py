import sys
input = sys.stdin.readline

N = int(input())
sticks = []

for i in range(N):
  sticks.append(int(input()))

count = 1

highest = sticks[-1] # 6

for stick in sticks[::-1]:
  if stick > highest:
    count += 1
    highest = stick

print(count)