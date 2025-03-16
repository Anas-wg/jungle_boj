# 골드바흐 수 => 2보다 모든 짝수는 두 소수의 합으로 나타내기 가능
# 골드바흐 파티션 => 짝수를 두 소수의 합으로 표현 (6 = 3 + 3)
# 구해야 할 것 -> 골드바흐 파티션을 출력, 여러개라면 두 소수의 차이가 가장 작은것 
import sys
import math
input = sys.stdin.readline


def is_prime(N):
  for i in range(2, int(math.sqrt(N)) + 1):
    if N % i == 0:
      return False
  return True

T = int(input())

for i in range(T):
  N = int(int(input()) / 2)
  if is_prime(N) == True:
    print(N, N)
  else:
    prime_num_list = []
    for i in range(2, int(math.sqrt(N)) + 1):
      if N % i == 0:
        continue
      else:
        prime_num_list.append(N)
    
    for nums in prime_num_list[-1::]:
      if is_prime(N - nums):
        print(nums, N - nums)
        break



import sys
import math

input = sys.stdin.readline

# 소수 판별 함수 (2 포함)
def is_prime(N):
    if N < 2:
        return False
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
    return True

T = int(input())

for _ in range(T):
    N = int(input())  # 입력받은 짝수
    
    # N보다 작은 소수를 찾는다.
    for i in range(N // 2, 1, -1):  # 두 소수의 차이가 최소인 것을 찾기 위해 N//2에서 시작
        if is_prime(i) and is_prime(N - i):
            print(i, N - i)
            break
