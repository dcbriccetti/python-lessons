gameChars = {}

while 1:
    name = eval(input("Player name? "))
    if name == "":
        break
    magic = int(eval(input("Magic power value? ")))
    gameChars[name] = magic

print("These characters have magic power values over 80:")

for key in gameChars:
    if gameChars[key] > 80:
        print(key)

print([key for key in gameChars if gameChars[key] > 80])
