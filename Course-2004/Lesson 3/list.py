l = list()
while 1:
    word = eval(input("Enter a word: "))
    if word == "":
        break
    if word in l:
        print('already in')
    else:
        l.append(word)

print(l)
