def letter_grade(score):
    if score < 60:
        grade = 'F'
    elif score < 70:
        grade = 'D'
    elif score < 80:
        grade = 'C'
    elif score < 90:
        grade = 'B'
    else:
        grade = 'A'
    return grade

for score in range(55, 101):
    print(score, letter_grade(score))
