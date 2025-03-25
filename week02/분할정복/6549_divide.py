import sys

input = sys.stdin.readline

res = []


# 분할 정복
def divide_and_conquer(histogram, start, end):
    if end == start: # 하나 있는 경우니까 그대로 리턴
        return histogram[end]
    elif end - start == 1: # 2개 남았을 경우 => 더 짧은 쪽을 2배 하는 것과, 높은 쪽 하나의 넓이 비교
        if histogram[end] < histogram[start]: 
            return max(2*histogram[end], histogram[start])
        else:
            return max(2*histogram[start], histogram[end])
    
    mid = (start + end) // 2 # 가운데 인덱스를 기준으로 분할

    left_area = divide_and_conquer(histogram, start, mid) # 앞쪽 재귀 실행
    right_area = divide_and_conquer(histogram, mid+1, end) # 뒤쪽 재귀 실행
    left = mid-1 # 왼쪽으로 확장
    right = mid+1 # 오른쪽으로 확장
    mid_area = histogram[mid] #  기준 사각형의 넓이
    now_height = histogram[mid] # 현재 기준점의 높이
    while start <= left and right <= end: # 왼쪽, 오른쪽 둘다 확장한 경우(분할 기준점 포함)
        if histogram[left] < histogram[right]:  # 오른쪽 확장이 더 높다면
            if histogram[right] < now_height: # 현재보다 작다면
                now_height = histogram[right]
            mid_area = max(mid_area, now_height * (right - left))
            right += 1
        else:
            if histogram[left] < now_height:
                now_height = histogram[left]
            mid_area = max(mid_area, now_height * (right - left))
            left -= 1
            
    while start <= left: # 왼쪽 범위의 최대
        if histogram[left] < now_height:
            now_height = histogram[left]
        mid_area = max(mid_area, now_height * (right - left))
        left -= 1
    while right <= end: # 오른쪽 범위의 최대
        if histogram[right] < now_height:
            now_height = histogram[right]
        mid_area = max(mid_area, now_height * (right - left))
        right += 1

    return max(left_area, right_area, mid_area)
        
            
        
res = []
while True:
    histogram = list(map(int, input().split()))
    
    if histogram[0] == 0: break
    
    n = histogram[0]
    
    res.append(divide_and_conquer(histogram, 1, n))

    
for i in res:
    print(i)