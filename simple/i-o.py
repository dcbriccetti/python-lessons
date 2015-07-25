with open('scores.txt') as files:
    lines = files.readlines()

scores = []

for line in lines:
    line_strip = line.strip()
    name, score_str = line_strip.split(',')
    score = int(score_str)
    scores.append(score)
    print('The score of %s is %d' % (name, score))

print('Min: %d, avg: %d, max: %d' % (min(scores), sum(scores) / len(scores) ,max(scores)))
