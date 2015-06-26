def getNum(prompt = 'Positive real number, please: '):
    while 1:
        try:
            num = float(eval(input(prompt)))
            if num >= 0:
                return num
        except ValueError:
            print('Bad number')

num = getNum(prompt = 'Give it! ')
print(num)
