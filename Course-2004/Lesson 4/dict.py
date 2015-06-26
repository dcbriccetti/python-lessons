wc = dict()
while 1:
    word = eval(input("Enter a word: "))
    if word == "":
        break
    if word in wc:
        wc[word] += 1
    else:
        wc[word] = 1

print(wc)
