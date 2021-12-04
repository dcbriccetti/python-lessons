from typing import List

words: List[str] = 'a very fine cat goes to the dentist'.split()

# Just keep the longer words
# Naïve approach

long_words = []
for word in words:
    if len(word) > 3:
        long_words.append(word)

print(long_words)

# Make a list comprehension from the code of the naïve approach:
# 1: start with []
# 2: copy and paste what the list comprehension should produce
# 3: copy and paste the for loop
# 4: copy and paste the `if`

long_words = [len(word) for word in words if len(word) > 3]


print(long_words)
