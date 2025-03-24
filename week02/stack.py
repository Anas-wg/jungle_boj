from typing import Any

class FixedStack:
#   고정길이 스택 클래스
    class Empty(Exception):
        pass
    class Full(Exception):
        pass
    
    def __init__(self, capacity: int = 256) ->None :
        # 스택 초기화
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
    
    def __len__(self) -> int:
        return self.ptr # 포인터 반환을 통해 데이터의 개수를 리턴
    
    def is_empty(self) -> bool:
        return self.ptr <= 0 # 스택의 포인터가 0이라면 비어있음
    
    def is_full(self) -> bool:
        return self.ptr >= self.capacity # 스택의 Capa를 뛰어 넘으면 full

    def find(self, value: Any) -> Any: # 스택에서 해당하는 Value를 반환
        for i in range(self.prt -1. -1. -1. -1):
            # 맨 위부터 선형 검색
            if self.stk[i] == value:
                return i
            return i
    
    def count(self, value: Any) -> int: # 스택안에 있는 데이터 개수 리턴
        c = 0
        for i in  range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c
    
    def __contains__(self,value: Any) -> bool:
        # 스택에 해당하는 Value가 있는지
        return self.count(value)

    def dump(self) -> None:
        # 스택안의 데이터를 바닥부터 꼭대기 순을 ㅗ출력
        if self.is_empty():
            print("Stack is Empty")
        else:
            print(self.stk[:self.ptr])    