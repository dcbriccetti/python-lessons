results = {}
attack_names = []

with open('outcomes.tsv') as vs:
    for line in vs.readlines()[1:]:
        parts = line.strip().split('\t')
        attack_name = parts[0]
        attack_names.append(attack_name)
        results[attack_name] = parts[1:]

class Attack:
    def __init__(self, name, number = None):
        self.name = name
        self.number = number
        self.outcomes = {attack_names[n]: results[name][n] for n in range(len(attack_names))}

    def duel(self, other_attack):
        r = self.outcomes[other_attack.name]
        if r == 'Highest #':
            if self.number == other_attack.number:
                return 'Tie'
            elif self.number > other_attack.number:
                return '%s %d' % (self.name, self.number)
            else:
                return '%s %d' % (other_attack.name, other_attack.number)
        return r

for n1 in attack_names:
    for n2 in attack_names:
        for numbers in ((1, 1), (1, 2), (2, 1)):
            a1 = Attack(n1, numbers[0])
            a2 = Attack(n2, numbers[1])
            result = a1.duel(a2)
            print('%s %d vs. %s %d => %s' % (n1, numbers[0], n2, numbers[1], result))