import sys
import bisect  # 이분 탐색 라이브러리 사용

input = sys.stdin.readline

# 1. 입력받기
N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()  # 오름차순 정렬

# 2. 결과값 초기화
min_sum = float('inf')
result = (0, 0)

# 3. 이분 탐색
for i in range(N - 1): 
    current_value = num_list[i] # 고정할 원소
    
    # 현재 값의 반대 부호에 가장 가까운 값을 찾기
    target = -current_value
    # i 뒤의 값을 탐색
    idx = bisect.bisect_left(num_list, target, i + 1)  


    if idx < N and abs(current_value + num_list[idx]) < abs(min_sum):
        min_sum = current_value + num_list[idx]
        result = (current_value, num_list[idx])
    
    if idx - 1 > i and abs(current_value + num_list[idx - 1]) < abs(min_sum):
        min_sum = current_value + num_list[idx - 1]
        result = (current_value, num_list[idx - 1])

# 4. 결과 출력
print(*sorted(result))








##########################

import sys
input = sys.stdin.readline

# 1. 입력받기
N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

# 2. 이진탐색
start = 0
end = len(num_list) - 1

def search(start, end, arr):
    first, second = arr[start], arr[end]
    min_sum = float('inf')

    while start < end: 
        current_sum = arr[start] + arr[end]

        if abs(current_sum) < abs(min_sum):  
            min_sum = current_sum
            first = arr[start]
            second = arr[end]

        if current_sum == 0:
            break
        elif current_sum < 0:  
            start += 1
        else:  
            end -= 1
            
    return first, second

print(*search(start, end, num_list))

