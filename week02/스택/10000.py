import sys
input = sys.stdin.readline
# 1. 입력받기
N = int(input())
circle_info = []

for i in range(N):
  x,r = map(int, input().split())
  circle_info.append([x, r])

# 2. 입력값을 교점으로 변환
for i in range(len(circle_info)):
  x, r = circle_info[i][0], circle_info[i][1]
  circle_info[i][0] = x - r
  circle_info[i][1] = r + x

# 3. 작은 값 부터 돌리기 위해 sort
circle_info.sort()
print(circle_info)

# 4. 가장 작은 x 축 값부터 시작 => 해당 좌표 지나가는 원 stack에 append
# stack의 길이를 합치기
stack = []
answer = 0

for i in range(len(circle_info)):
    start, end = circle_info[i]
    
    # stack에 추가하기 (겹치는 원 추가)
    stack.append(end)
    
    # answer에 현재 스택의 길이를 더하기
    answer += len(stack)
    
    # 만약 스택의 길이가 N과 같아진다면 멈추기
    if len(stack) == N:
        break

print(answer)