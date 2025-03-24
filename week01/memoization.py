def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)	

dic = {0 : 0, 1 : 1}
def fibonacci_memo(n):
	if n in dic: # 0과 1의 경우
		return dic[n]
	dic[n]= fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
	return dic[n]

from timeit import *
t3 = Timer("fibonacci(30)","from __main__ import fibonacci")
t4 = Timer("fibonacci_memo(30)","from __main__ import fibonacci_memo")

print("단순 재귀 * 20번", t3.timeit(number = 20), "seconds")
print("재귀 + 메모이제이션 * 20번", t4.timeit(number = 20), "seconds")