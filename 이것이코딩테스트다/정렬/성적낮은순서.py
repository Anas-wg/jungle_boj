N = int(input())
array = []

for i in range(N):
  info = input().split()
  array.append([info[0], int(info[1])])

array.sort(key=lambda x:x[1])

for student in array:
  print(student[0], end=' ')