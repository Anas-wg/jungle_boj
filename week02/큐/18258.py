# 큐의 6가지 명령 처리
# First In first out

from collections import deque
import sys
input = sys.stdin.readline
q = deque([])

def push(q, X):
  q.append(X)

def pop(q):
  if len(q) == 0:
    print(-1)
  else:
    print(q.popleft())

def size(q):
  print(len(q))

def empty(q):
  if len(q) == 0:
    print(1)
  else:
    print(0)

def front(q):
  if len(q) == 0:
    print(-1)
  else:
    print(q[0])

def back(q):
  if len(q) == 0:
    print(-1)
  else:
    print(q[-1])


N = int(input())
for i in range(N):
  command = input().split()

  if command[0] == 'push':
    push(q, int(command[1]))
  elif command[0] == 'pop':
    pop(q)
  elif command[0] == 'size':
    size(q)
  elif command[0] =='empty':
    empty(q)
  elif command[0] == 'front':
    front(q)
  elif command[0] == 'back':
    back(q)