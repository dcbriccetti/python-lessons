import math
from time import time
start_time = time()
HIGHEST = 100
sieve = [True] * (HIGHEST + 1)

for prime in range(2, int(math.sqrt(HIGHEST + 1))):
    for n in range(prime * 2, HIGHEST + 1, prime):
        sieve[n] = False

elapsed_time = time() - start_time

print()
print(elapsed_time)

for n in range(1, HIGHEST + 1):
    if sieve[n]:
        print(n, end=' ')

