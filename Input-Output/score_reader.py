hs_name = ''
hs_score = 0

with open('scores.csv') as file:
    for line in file:
        name, score_str = line.strip().split(',')
        score = int(score_str)
        if score > hs_score:
            hs_name = name
            hs_score = score

print('%s has the highest score, %d' % (hs_name, hs_score))
