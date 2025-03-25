import heapq
import sys

input = sys.stdin.readline

n = int(input())
left_heap = [] #중간값보다 작거나 같은 값
right_heap = [] # 중간값보다 큰 값

for _ in range(n):
    x = int(input())
    
    if len(left_heap) == len(right_heap): 
        #중간값을 left_h의 루트로 유지하기 위해 길이가 같으면 left_h에 push
        heapq.heappush(left_heap, -x) # 음수를 넣어서 최대 힙으로 사용
    
    else:
        # 길이가 다르면 right_heap에 삽입
        heapq.heappush(right_heap, x)

    # 만약 left_heap 의 루트 값이 right_heap의 루트 값 보다 크다면, 둘의 값이 잘못 배치
    if left_heap and right_heap and left_heap[0] * -1 > right_heap[0]:
        max_value = heapq.heappop(left_heap)
        min_value = heapq.heappop(right_heap)
        
        # 두 값을 서로 바꾸어 다시 집어 넣기
        heapq.heappush(left_heap, min_value * -1)
        heapq.heappush(right_heap, max_value * -1)
    # lef_heap의 루트값이 무조건 중간 값
    print(left_heap[0] * -1)