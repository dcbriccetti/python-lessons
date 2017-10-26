current, next = 0, 1

for n in range(10):
    print(current)
    current, next = next, current + next
