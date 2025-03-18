# # 조합 라이브러리 활용
# from itertools import combinations

# smalls = []

# for i in range(9):
#   smalls.append(int(input()))


# seven_smalls = list(map(list, combinations(smalls, 7)))

# for case in seven_smalls:
#   if sum(case) == 100:
#     case.sort()
#     for elems in case:
#       print(elems)
#     break


# 완전탐색 => 9명의 합을 구해서 2명의 키를 제함
smalls = []

for i in range(9):
  smalls.append(int(input()))

S = sum(smalls)
res = sorted(smalls)

check = False

for i in range(8):
  if check == True:
    break
  for j in range(i + 1, 9):
    if S - smalls[i] - smalls[j] == 100:
      res.remove(smalls[i])
      res.remove(smalls[j])
      check = True
      break


for small in res:
  print(small)