import sys
input = sys.stdin.readline

def max_square(start, end):
  if start == end: # 직사각형이 하나라면 높이를 바로 리턴
    return squares[start] 
  else:
    mid = (start + end) // 2
    new_left = mid
    new_right = mid + 1
    new_height = min(squares[new_left], squares[new_right])
    temp = 2 * new_height
    count = 2 # new_left, new_right 둘다 포함, 따라서 2
    while True:
      if(squares[new_left] == 0 or new_left == start) and (squares[new_right] == 0 or new_right == end):
        break # 하나 남은 경우

      # new_left를 더이상 늘릴 수 없는 경우
      elif squares[new_left] == 0 or new_left == start:
        if squares[new_right + 1] < new_height: # 만약 오른쪽 막대가 더 작다면 갱신
          new_height = squares[new_right + 1]
        new_right += 1 # 왼쪽으로 늘릴 수 없기 때문에 오른쪽을 확장
      
      # new_right를 더이상 늘릴 수 없는 경우
      elif squares[new_right] == 0 or new_right == end:
        if squares[new_left - 1] < new_height: 
          new_height = squares[new_left - 1] # 만약 왼쪽 막대가 더 작다면 갱신
        new_left -= 1 # 오른쪽으로 늘릴 수 없기에 왼쪽을 확장
      
      # 양쪽 다 늘릴 수 있는 경우 => 더 큰 쪽으로 먼저 늘리기
      else:
        if squares[new_left - 1] > squares[new_right + 1]:
          if squares[new_left - 1] < new_height: 
            new_height = squares[new_left - 1] 
          new_left -= 1
        else:
          if squares[new_right + 1] < new_height:
            new_height = squares[new_right + 1]
          new_right += 1
      count += 1
      temp = max(temp, new_height * count)
  return (max(max_square(start, mid), max_square(mid + 1, end), temp))


  
while True:
  squares = list(map(int, input().split()))
  if squares[0] == 0:
    break
  print(max_square(1, len(squares) - 1))