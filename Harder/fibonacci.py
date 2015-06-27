num_to_make = 10

num1, num2 = 0, 1
print(num1)
print(num2)

for n in range(num_to_make - 2):
    num1, num2 = num2, num1 + num2
    print(num2)

