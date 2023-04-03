from string import punctuation
from pathlib import Path

NUM_RESULTS = 20
word_counts: dict[str, int] = {}
stopwords: set[str] = {line.strip() for line in Path('stopwords.txt').read_text().splitlines()}

for line in Path('play.txt').read_text().lower().splitlines():
    for word in line.split():
        if (cleaned := word.strip(punctuation)) not in stopwords:
            word_counts[cleaned] = word_counts.get(cleaned, 0) + 1

sorted_counts: list[tuple[str, int]] = sorted(word_counts.items(), key=lambda t: t[1], reverse=True)

for word, count in sorted_counts[:NUM_RESULTS]:
    print(f'{word}\t{count}')
