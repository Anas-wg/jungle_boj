import sys
input = sys.stdin.readline

# 1. 입력받기
N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

# 2. 이진탐색
start = 0
end = len(num_list) - 1

def binary_search(start, end, arr):
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

print(*binary_search(start, end, num_list))
