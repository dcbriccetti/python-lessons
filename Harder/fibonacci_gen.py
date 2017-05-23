def fibs(highest):
    current = 1
    next = 2
    while current <= highest:
        yield current
        current, next = next, current + next


g = fibs(13)
print(list(g))

# Produces 1 2 3 5 8 13