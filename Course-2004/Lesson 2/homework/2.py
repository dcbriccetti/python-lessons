def getNum():
    num = float(eval(input('Please enter a number: ')))
    if num < 0:
        num *= 2
    else:
        num *= 3
    return num

num1 = getNum()
num2 = getNum()

print(('The result is', num1 + num2))
