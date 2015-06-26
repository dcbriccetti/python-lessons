while True: # Continue while input is invalid
    try:
        num = int(input('Integer between 1 and 10? '))
        if num > 0 and num < 11:
            break
    except ValueError:
        print("That wasn't even an integer.")

print('Your number is %d' % num)
