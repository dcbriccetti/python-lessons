from random import randint

num_dice = 2
num_sides = 6
num_throws = 10000
list_len = num_dice * num_sides + 1

counts = [0 for n in range(list_len)]

for i in range(num_throws):
	outcome = sum([randint(1, num_sides) for j in range(num_dice)])
	counts[outcome] += 1

for outcome, count in enumerate(counts[num_dice: list_len]):
	print(f'{outcome + num_dice:3,}\t{count:6,}')
