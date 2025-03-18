def fibo_loop(N):
    num_list = [1, 1]  # Initialize the list with the first two Fibonacci numbers

    if N <= 2:
        return num_list[N - 1]  # Return directly if N is 1 or 2
    else:
        for i in range(2, N):
            num_list.append(num_list[i - 2] + num_list[i - 1])  # Correctly compute Fibonacci numbers
        return num_list[N - 1]  # Return the Nth Fibonacci number

print(fibo_loop(5))  # Output: 5
