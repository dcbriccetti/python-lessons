import random
strings = []

while 1:
    s = eval(input("Give us a string, gov. "))
    if s == "":
        break
    strings.append(s);

random.shuffle(strings)
print(("Here are your strings, all nice and shuffled: ", strings))

