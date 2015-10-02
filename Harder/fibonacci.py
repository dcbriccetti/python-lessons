num_to_make = 10

num1, num2 = 0, 1

for n in range(num_to_make):
    print(num1)
    num1, num2 = num2, num1 + num2
