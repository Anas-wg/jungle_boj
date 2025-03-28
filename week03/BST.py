from __future__ import annotations
from typing import Any, Type

class Node :
  def __init__(self, key : Any, value : Any, left : Node = None, right : Node = None):
    self.key = key # 키
    self.value = value # 값
    self.left = left #  왼쪽 포인터
    self.right = right # 오른쪽 포인터

class BinarySearchTree:
  def __init__(self):
    self.root = None # 초기화시 루트 없음
  
  def search(self, key : Any):
    p = self.root # p는 주목하는 노드
    while True:
      if p is None:
        return None
      if key == p.key:
        return p.value
      elif key < p.key: # 찾고자 하는 키가 주목노드의 키보다 작다면
        p = p.left # 왼쪽 서브트리로 이동
      else:
        p = p.right

  def add(self, key: Any, value: Any) -> bool:
    def add_node(node: Node, key: Any, value: Any) -> None:
      if key == node.key: # 동일한 키값 있다면 삽입불가
        return False
      elif key < node.key: # 삽입하고자 하는 키가 더 작다면
        if node.left is None: # 왼쪽자식으로 이동, 자식 비었다면 거기 삽입
          node.left = Node(key, value, None, None)
        else: # 자식 있다면 이동하여 다시 탐색 후 삽입
          add_node(node.left, key, value)
      else: # 삽입하고자 하는 키가 더 크다면
        if node.right is None: # 오른쪽 자식으로 이동
          node.right = Node(key, value, None, None)
        else:
          add_node(node.right, key, value)
        return True
      
      if self.root is None: # 루트가 빈 상태인 경우
        self.root = Node(key, value, None, None)
        return True
      else:
        return add_node(self.root, key, value)
  
  def remove(self, key: Any) -> bool:
    p = self.root  # 스캔 중인 노드 (현재 탐색 중인 노드를 의미)
    parent = None  # 스캔 중인 노드의 부모 노드 (부모를 기억해둬야 연결을 변경할 수 있음)
    is_left_child = True  # 스캔 중인 노드가 부모의 왼쪽 자식인지 여부 체크
    
    while True:
        if p is None:  # 더 이상 진행 불가 (트리에 해당 키가 없음)
            return False
        
        if key == p.key:  # 삭제할 노드를 찾은 경우
            break  # 검색 성공, 삭제 작업으로 이동
        else:
            parent = p  # 부모 노드를 현재 노드로 갱신 (이동하기 전에 저장)
            
            if key < p.key:  # 탐색할 키가 현재 노드의 키보다 작은 경우
                is_left_child = True  # 왼쪽 자식으로 이동할 것이므로 True로 설정
                p = p.left  # 왼쪽 자식으로 이동
            else:  # 탐색할 키가 현재 노드의 키보다 큰 경우
                is_left_child = False  # 오른쪽 자식으로 이동할 것이므로 False로 설정
                p = p.right  # 오른쪽 자식으로 이동
    
    # ---------- 여기서부터 삭제 작업 ----------
    
    # 1. 자식 노드가 없는 노드를 삭제하는 경우 (단말 노드 삭제)
    if p.left is None:  # 현재 노드의 왼쪽 자식이 없는 경우 (오른쪽 자식만 존재하거나 없음)
        if p is self.root:  # 삭제할 노드가 루트 노드인 경우
            self.root = p.right  # 오른쪽 자식을 새로운 루트로 설정
        elif is_left_child:  # 부모의 왼쪽 자식인 경우
            parent.left = p.right  # 부모의 왼쪽 포인터가 현재 노드의 오른쪽 자식을 가리키게 함
        else:  # 부모의 오른쪽 자식인 경우
            parent.right = p.right  # 부모의 오른쪽 포인터가 현재 노드의 오른쪽 자식을 가리키게 함

    # 2. 오른쪽 자식이 없는 노드를 삭제하는 경우 (왼쪽 자식만 존재)
    elif p.right is None:  # 현재 노드의 오른쪽 자식이 없는 경우 (왼쪽 자식만 존재)
        if p is self.root:  # 삭제할 노드가 루트 노드인 경우
            self.root = p.left  # 왼쪽 자식을 새로운 루트로 설정
        elif is_left_child:  # 부모의 왼쪽 자식인 경우
            parent.left = p.left  # 부모의 왼쪽 포인터가 현재 노드의 왼쪽 자식을 가리키게 함
        else:  # 부모의 오른쪽 자식인 경우
            parent.right = p.left  # 부모의 오른쪽 포인터가 현재 노드의 왼쪽 자식을 가리키게 함

    # 3. 자식 노드가 둘 다 존재하는 경우 (왼쪽, 오른쪽 자식 모두 존재)
    else:  
        parent = p  # 삭제할 노드를 p로 지정 (부모를 임시 저장)
        left = p.left  # 왼쪽 서브트리의 루트로 이동 (왼쪽 서브트리에서 가장 큰 값을 찾기 위해)
        is_left_child = True  # 왼쪽 자식을 탐색할 것이므로 True로 설정
        
        while left.right is not None:  # 왼쪽 서브트리에서 가장 큰 값을 찾기 위해 오른쪽으로 계속 이동
            parent = left  # 부모를 왼쪽 노드로 갱신
            left = left.right  # 오른쪽 자식으로 계속 이동
            is_left_child = False  # 오른쪽으로 이동 중이므로 False로 설정

        # 찾은 노드(left)의 키와 값을 현재 노드(p)에 복사 (대체)
        p.key = left.key  # 키 값 대체
        p.value = left.value  # 데이터 값 대체
        
        # 기존의 left 노드를 삭제 (부모 노드의 포인터 재설정)
        if is_left_child:  # 삭제할 노드가 부모의 왼쪽 자식인 경우
            parent.left = left.left  # 부모의 왼쪽 포인터를 삭제할 노드의 왼쪽 자식으로 변경
        else:  # 삭제할 노드가 부모의 오른쪽 자식인 경우
            parent.right = left.left  # 부모의 오른쪽 포인터를 삭제할 노드의 왼쪽 자식으로 변경

    return True  # 삭제 완료

  
  def dump(self) -> None:
    def print_subtree(node: Node):
      if node is not None:
        print_subtree(node.left)
        print(f'{node.key} {node.value}')
        print_subtree(node.right)
    print_subtree(self.root)
  

        

