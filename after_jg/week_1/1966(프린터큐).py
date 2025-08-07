
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    N, find_idx = map(int, input().split())
    importances = list(map(int, input().split()))
    count = 0
    printer = deque() 

    for idx, importance in enumerate(importances):
        printer.append([importance, idx])

    while len(printer) > 0 :
        now = printer.popleft()
        is_max = True
        
        for docs in printer:
            if docs[0] > now[0]:
                printer.append(now)
                is_max = False
                break
        
        if is_max:
            count += 1
            if now[1] == find_idx:
                result.append(count)
                break

for res in result:
    print(res)
