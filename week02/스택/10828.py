# 5가지 명령에 따라 출력
import sys
input = sys.stdin.readline

# 명령의 수
N = int(input())

stack = []

def push(arr, X):
  arr.append(X)

def pop(arr):
  if len(arr) == 0:
    print(-1)
  else:
    print(arr[-1])
    arr.pop()
    

def size(arr):
  print(len(arr))

def empty(arr):
  if len(arr) == 0:
    print(1)
  else:
    print(0)

def top(arr):
  if len(arr) == 0:
    print(-1)
  else:
    print(arr[-1])


for i in range(N):
  inst = input().split()
  # 명령어를 받을때 어떻게 입맛에 맞게 바꿀까
  if inst[0] == 'push':
    push(stack, int(inst[1]))
  elif inst[0] == 'top':
    top(stack)
  elif inst[0] == 'size':
    size(stack)
  elif inst[0] == 'pop':
    pop(stack)
  elif inst[0] == 'empty':
    empty(stack)