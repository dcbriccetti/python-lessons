def factorial(n):
    return n if n == 1 else n * factorial(n - 1)

assert(factorial(3) == 6)
assert(factorial(4) == 24)
