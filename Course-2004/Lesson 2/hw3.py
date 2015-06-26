num1 = float(eval(input('Please enter a number: ')))
if num1 < 0:
    num1 *= 2
else:
    num1 *= 3

num2 = float(eval(input('Please enter a number: ')))
if num2 < 0:
    num2 *= 2
else:
    num2 *= 3

print(('The result is', num1 + num2))
