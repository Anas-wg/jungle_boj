# 포인터로 연결리스트 구현

from __future__ import annotations
from typing import Any, Type

class Node:
  def __init__(self, data : Any = None, next: Node = None):
    # 초기화
    self.data = data # 데이터
    self.next = next # 뒤쪽 포인터


class LinkedList:
  def __init__(self):
    self.no = 0 # 노드의 개수
    self.head = None # 머리 노드
    self.current = None # 주목 노드

  def __len__(self):
    # 연결 리스트의 노드 개수 반환
    return self.no
  
  def search(self, data):
    #  data와 값이 같은 노드를 검색
    cnt = 0
    ptr = self.head
    while ptr is not None:
      if ptr.data == data:
        self.current = ptr
        return cnt
      cnt += 1
      ptr = ptr.next
    return -1
  
  def __contains__(self, data):
    # 연결리스트에 데이터 포함 여부를 확인
    return self.search(data) >= 0
  
  def add_first(self, data):
    # 맨 앞에 노드 삽입
    ptr = self.head
    self.head = self.current = Node(data, ptr)
    self.no += 1
  
  def add_last(self, data):
    # 맨 끝에 노드 삽입
    if self.head is None: # 리스트 비어 있다면
      self.add_first(data)
    else:
      ptr = self.head
      while ptr.next is not None:
        ptr = ptr.next
      ptr.next = self.current = Node(data, None)
      self.no += 1
  
  def remove_first(self):
    #  머리 노드 삭제
    if self.head is not None: # 리스트가 비어있지 않다면
      self.head = self.current = self.head.next
    self.no -= 1
  
  def remove_last(self):
    # 꼬리 노드 삭제
    if self.head is not None:
      if self.head.next is None: # 노드가 1개 뿐이라면
        self.remove_first() # 머리 노드 삭제
      else:
        ptr = self.head # 스캔 중인 노드
        pre = self.head # 스캔 중인 노드의 앞쪽 노드

        while ptr.next is not None:
          pre = ptr
          ptr = ptr.next
        
        pre.next = None
        self.current = pre
        self.no -= 1

def remove(self, p:Node):
  

