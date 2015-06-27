def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

assert(factorial(3) == 6)
assert(factorial(4) == 24)
