def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  
  mid = len(arr) // 2
  left = merge_sort(arr[:mid]) 
  right = merge_sort(arr[mid:]) 
  return merge(left, right)

def merge(left, right):
  merged_arr = []
  i = j = 0
  while i < len(left) and j < len(right):
    if left[i] > right[j]:
      merged_arr.append(left[i])
      i += 1
    else:
      merged_arr.append(right[j])
      j += 1
  merged_arr = merged_arr + left[i:] + right[j:]
  return merged_arr


print(merge_sort([2,3,1,4]))

# 
from typing import Any 
 
class FixedQueue: 
    def __init__(self, capacity: int) -> None: 
        self.no = 0 # 현재 데이터 개수 
        self.front = 0 # 맨 앞 원소 커서 
        self.rear = 0 # 맨 끝 원소 커서 
        self.capacity = capacity # 큐의 크기 
        self.que = [None] * capacity # 큐의 본체 
 
    def __len__(self) -> int: 
        return self.no 
     
    def is_empty(self) -> bool: 
        return self.no <= 0 
 
    def is_full(self) -> bool: 
        return self.no >= self.capacity 
 
      # 데이터를 큐에 추가
    def enque(self, x: Any) -> None:
        if self.is_full():
            raise OverflowError('Queue is full')
        
        self.que[self.rear] = x  # 데이터를 rear 위치에 삽입
        self.rear = (self.rear + 1) % self.capacity  # rear 포인터를 한 칸 이동 (환형 구조)
        self.no += 1  # 데이터 개수 증가

    # 데이터를 큐에서 삭제
    def deque(self) -> Any:
        if self.is_empty():
            raise IndexError('Queue is empty')
        
        x = self.que[self.front]  # front 위치의 데이터를 꺼냄
        self.que[self.front] = None  # 데이터 제거 (필수는 아니지만 보기 좋게 초기화)
        self.front = (self.front + 1) % self.capacity  # front 포인터를 한 칸 이동 (환형 구조)
        self.no -= 1  # 데이터 개수 감소
        return x
 
 
