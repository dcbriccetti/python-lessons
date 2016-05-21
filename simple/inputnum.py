def getNumeric(prompt):
    while True:
        response = input(prompt)
        try:
            return int(response)
        except ValueError:
            print("Please enter a number.")

if __name__ == '__main__':
    age = getNumeric('What is your age? ')
    print(age)
