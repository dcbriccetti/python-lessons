def letter_grade(score):
    if score >= 90:
        grade = 'A'
    else:
        grade = 'B'
    return grade

while True:
    score = int(input('Score? '))
    if score < 0:
        break
    print(letter_grade(score))
