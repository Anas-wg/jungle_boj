# 1. 입력받기
# 2. 우선순위 큐 활용 



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
        is_max = True # flag
        
        for docs in printer:
            if docs[0] > now[0]: # 더 높은 우선순위 있으면
                printer.append(now) # 뒤로 append
                is_max = False 
                break
        
        if is_max: # 가장 높은 거
            count += 1 # 출력하니까 1 추가
            if now[1] == find_idx:
                result.append(count)
                break

for res in result:
    print(res)
