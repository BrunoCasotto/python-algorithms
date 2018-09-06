

# function basic to calculate fibonacci using recursive programming
def basic_calc(n):
    if n == 1 or n == 2:
        return 1

    return basic_calc(n-1) + basic_calc(n-2)

# function to calculate fibonacci using memoize strategy
def memoize_calculate(n, memo):
    if memo[n] is not None:
        return memo[n]

    if n == 1 or n == 2:
        result = 1
    else:
        result = memoize_calculate(n-1 , memo) + memoize_calculate(n-2, memo)

    memo[n] = result
    return result

# function to create a memo and call calculate function
def memoize_calc(n):
    memo = [None] * (n + 1)
    return memoize_calculate(n, memo)

# function to calculate the fibonacci number using bottom_up technical
def bottom_up_calc(n):
    if n == 1 or n == 2:
        return 1
    fibo = [None] * (n + 1)

    fibo[1] = 1
    fibo[2] = 1

    index = n
    cursor = 1

    while index > 0:
        if fibo[cursor] is None:
            fibo[cursor] = fibo[cursor - 1] + fibo[cursor - 2]
        index -= 1
        cursor+= 1

    return fibo[n]