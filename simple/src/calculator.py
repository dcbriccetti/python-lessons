'''A simple calculator using a dictionary to look up functions for operators'''

def add(n1, n2): return n1 + n2
def mult(n1, n2): return n1 * n2

opers = {
    '+': add,
    '*': mult
}

print("Enter expressions like 23 * 10 or 2 - 5")

while True:
    expr = input('> ')
    if expr:
        try:
            (op1, op, op2) = expr.split(' ')
            print(opers[op](int(op1), int(op2)))
        except Exception:
            print("Sorry, I couldn't make sense of that")
    else:
        break
