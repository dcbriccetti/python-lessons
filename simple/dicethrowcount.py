from random import randint

num_dice = 3
num_sides = 6
num_throws = 10000
list_len = num_dice * num_sides + 1

counts = [0 for n in range(list_len)]

for n in range(num_throws):
	outcome = sum([randint(1, num_sides) for n in range(num_dice)])
	counts[outcome] += 1

for outcome, count in enumerate(counts[num_dice: list_len]):
	print("{:3,} {:6,}".format(outcome + num_dice, count))
