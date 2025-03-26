import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
# 사대 리스트 입력받고 정렬
shot_place = sorted(list(map(int, input().split())))
animals = [list(map(int, input().split())) for _ in range(N)]

#  거리 구하는 함수
def get_distance(M, a ,b):
  return abs(M - a) + b

count = 0

def search_shot(a, b, list, start, end):
  global count
  # 이분 탐색 진행
  while start <= end:
    mid = (start + end) // 2
    dist = get_distance(list[mid], a, b)
    # 사정거리 안에 있다면 count ++
    if dist <= L:
      count += 1
      return
    # 사정거리 밖,  동물이 사대 오른쪽 위치시
    elif list[mid] < a:
      start = mid + 1 # 오른쪽으로 사대 이동
    else: # 동물이 사대 왼쪽 위치시
      end = mid - 1


start = 0
end = len(shot_place) - 1

for a, b in animals:
  search_shot(a, b, shot_place, start, end)


print(count)
