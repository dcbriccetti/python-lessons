import random
num = random.randint(1,100)
guess = 0

print("I am thinking of a number between 1 and 100. See if you can guess it.")

while (guess != num):

    guess = int(input("Your guess: "))

    if guess == num:
        print("That's right!")
    elif guess < num:
        print(guess, "is too low")
    else:
        print(guess, "is too high")

