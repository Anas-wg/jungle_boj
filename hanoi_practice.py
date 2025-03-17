MSG_FORMAT = "{}번 원반을 {}에서 {}으로 이동"

def move(N ,start, end):
  print(MSG_FORMAT.format(N, start, end))

def hanoi(N, start, end, sub):
  if N == 1:
    move(N, start, end)
  else:
    hanoi(N - 1, start, end, sub)
    move(N, start, end)
    hanoi(N - 1, sub, end, start)
  
hanoi(3, "A", "B", "C")
