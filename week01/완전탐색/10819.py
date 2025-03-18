from itertools import permutations
# N = 8, 8개의 배열을 나열하는 방법은 8!
N = int(input())

num_list = list(map(int, input().split()))

def get_sum(N, arr):
  result = 0
  for i in range(1, N):
    result += abs(arr[i] - arr[i - 1])
  return result

# 그럼 N개의 원소를 가진 배열을 싹 나열후 각각 배열의 합을 구하면?

temp = list(map(list, permutations(num_list, N)))
sum_list = []

for cases in temp:
  total = get_sum(N, cases)
  sum_list.append(total)

print(max(sum_list))

