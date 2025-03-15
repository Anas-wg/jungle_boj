# V 미터인 나무 막대를 A미터 올라가고 B 미터 미끄러질때 얼마나 걸리는가
import math

A, B, V = map(int, input().split())

# 마지막 날에는 미끄러지지 않기에 V가 아닌 V - B
# 또한 7.4일은 없기에 올림 처리
days = math.ceil((V - B) / (A - B))

print(days)
