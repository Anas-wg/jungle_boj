import sys
# 10000보다 작거나 같은 자연수
# 그렇다면 10001 길이의 배열 선언
# 만약 숫자 1이 2개면 arr[1] = 2 로 지정, 숫자 1을 두번 프린트하는게 낫다

N = int(sys.stdin.readline())
arr = [0] * 10001 # 1억만큼 생기지 않게

for _ in range(N):
  num = int(sys.stdin.readline())
  arr[num]+= 1 # num이 들어온 개수 Count
  
for i in range(10001):
  if arr[i] != 0: # 숫자가 들어왔다면
    for j in range(arr[i]):
      print(i)