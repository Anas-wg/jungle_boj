import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
answer = [0] * N  
stack = [] # 현재 타워 높이 저장 용

