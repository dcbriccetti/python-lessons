class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    def divide(self, num1, num2):
        return num1 / num2

calc = Calculator()
print((calc.add(2.5, 5)))
try:
    print((calc.divide(3,1)))
except ZeroDivisionError:
    print('Oops')
