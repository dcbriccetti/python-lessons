from time import sleep
from random import randint

nouns = ['truck', 'baseball', 'fire', 'bicyclist', 'hard drive', 'printer', 'salesperson', 'baker']
adjs = ['red', 'bumpy', 'evil', 'happy', 'enthusiastic', 'flummoxed', 'perturbed', 'innoculated']
advs = ['heartily', 'forcefully', 'gently', 'painfully', 'gleefully', 'derisively']
verbs = ['ran', 'exploded', 'dropped', 'swam', 'ate', 'jiggled', 'levitated', 'unlocked']

def choose_once(words):
    return words.pop(randint(0, len(words) - 1))

while len(nouns) and len(adjs) and len(advs) and len(verbs):
    s = 'The %s %s %s %s' % (choose_once(adjs), choose_once(nouns), choose_once(advs), choose_once(verbs))
    print(s)
    sleep(3)
