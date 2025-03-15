import sys
input = sys.stdin.readline
####### 노가다로 하나씩 판독
N = int(input())
num_list = list(map(int, input().split()))
answer = 0  # 소수 개수 카운트

for num in num_list:
    if num < 2:  # 1은 소수가 아님
        continue
    
    is_prime = True  # 기본적으로 소수라고 가정
    for j in range(2, num):  # 2부터 X-1까지 모두 나눠보기
        if num % j == 0:
            is_prime = False  # 나누어 떨어지면 소수가 아님
            break  # 더 확인할 필요 없음
    
    if is_prime:
        answer += 1  # 소수 개수 증가

print(answer)

######## 제곱근까지만 판독
import math

# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True

######### 에라토스테네스의 체 -> 배수 제거

import math

n = 1000 # 2부터 1000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제와)

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=" ")