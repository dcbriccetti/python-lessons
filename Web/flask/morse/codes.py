PASSWORD = 'abracadabra'

codes = """
0 -----
1 .----
2 ..---
3 ...--
4 ....-
5 .....
6 -....
7 --...
8 ---..
9 ----.
a .-
b -...
c -.-.
d -..
e .
f ..-.
g --.
h ....
i ..
j .---
k -.-
l .-..
m --
n -.
o ---
p .--.
q --.-
r .-.
s ...
t -
u ..-
v ...-
w .--
x -..-
y -.--
z --..
. .-.-.-
  --..--
? ..--..
! -.-.--
- -....-
/ -..-.
@ .--.-.
( -.--.
) -.--.-
""".split("\n")
morse_codes = {el[0]: el[2:] for el in codes if el}

symbols_and_words = (
    ('-', 'dash'),
    ('.', 'dot')
)

words_by_symbol = {symbol: word for symbol, word in symbols_and_words}
symbols_by_word = {word: symbol for symbol, word in symbols_and_words}
