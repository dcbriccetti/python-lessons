from random import randint

outcomes = [0] * 13

for _ in range(1_000):
    outcome = randint(1, 6) + randint(1, 6)
    outcomes[outcome] += 1

for outcome_index, outcome in enumerate(outcomes[2:], 2):
    print(f'{outcome_index:2}: {"*" * outcome} {outcome}')

