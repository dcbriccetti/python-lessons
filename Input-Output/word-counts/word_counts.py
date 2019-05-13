from typing import Dict, Set
from string import punctuation

NUM_RESULTS = 20
counts: Dict[str, int] = {}

with open('stopwords.txt') as file:
    stopwords: Set[str] = {line.strip() for line in file}

with open('play.txt') as file:
    for line in file:
        for word in line.split():
            cleaned = word.lower().strip(punctuation)
            if cleaned not in stopwords:
                counts[cleaned] = counts.get(cleaned, 0) + 1

for word in sorted(counts, key=counts.get, reverse=True)[:NUM_RESULTS]:
    print(f'{word}\t{counts[word]}')
