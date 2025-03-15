# 구해야 할 것 : 직사각형의 경계선까지의 최소거리
# 최소 거리 -> 가로변 까지의 거리(h - y), 세로변까지의 거리(w - x), x축까지의 거리, y축 까지의 거리 중 더 작은 값

import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())
print(min(h - y , w - x, x, y))