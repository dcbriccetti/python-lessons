def getNum():
    num = float(eval(input('Please enter a number: ')))
    if num < 0:
        num *= 2
    else:
        num *= 3
    return num

result = getNum() + getNum()
print(('The result is', result))
