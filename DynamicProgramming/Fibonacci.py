# Fibonacci using normal recurssion

def Fibonacci(Number):
    if Number <= 1:
        return Number
    return Fibonacci(Number-1) + Fibonacci(Number-2)

# for code above fib(5) = fib(3) + fib(4)
# fib(3) = fib(1) + fib(2)
# fib(4) = fib(2) + fib(3)

# hence we are calculating fib(2) multiple times
# if n is greater, then we calculate fib(values less than n) multiple no of times
number = 10
print(Fibonacci(number))

# to avoid this overrepeated tasks we use can use dynamic programming

def FibUsingDynamicProgramming(Number):

    # We know that first, second elements in fib series are 0, 1
    f = [0, 1]

    # from second element to number entered by user
    for i in range(2, Number+1):
        # append fib(i) to f
        f.append(f[i - 2] + f[i - 1])
    # return fib(number)
    return f[i]

# In the dynamic programming approach we never do the same task again
print(FibUsingDynamicProgramming(number))

# output
# 55
# 55
