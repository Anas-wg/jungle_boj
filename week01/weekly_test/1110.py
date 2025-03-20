import sys
input = sys.stdin.readline

N = int(input())
count = 0

def plus_cycle(num):
	global count
	
	ten_digit = num // 10 # 10의 자릿수 (2)
	first_digit = num % 10 # 1의 자릿수 (6)
	
  # 6 * 10 + (2 + 6) => 68
	new_num = (first_digit) * 10 + (ten_digit + first_digit) % 10
	count += 1
	# print(new_num)
	if new_num == N:
		return
	else:
		plus_cycle(new_num)

plus_cycle(N)
print(count)
		

