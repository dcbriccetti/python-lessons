num, next_num = 0, 1

for n in range(10):
    print(num)
    num, next_num = next_num, num + next_num
