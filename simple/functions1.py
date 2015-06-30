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

def shorter_letter_grade(score):
    for index, min in enumerate((90, 80, 70, 60, 0)):
        if score >= min:
            return 'ABCDF'[index]

for score in range(55, 101):
    grade1 = letter_grade(score)
    grade2 = shorter_letter_grade(score)
    assert(grade1 == grade2)
    print(score, grade1)
