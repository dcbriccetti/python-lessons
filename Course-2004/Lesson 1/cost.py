costPerHour = int(eval(input('How much per hour? ')))
numStudents = int(eval(input('How many students? ')))
numHours = float(eval(input('How many hours? ')))

costPerStudentPerHour = costPerHour / numStudents
costPerStudent = costPerStudentPerHour * numHours
totalCost = costPerHour * numHours

print(('Total cost: $%.2f' % totalCost))
print(('Cost per student per hour: $%.2f' % costPerStudentPerHour))
print(('Total cost per student: $%.2f' % costPerStudent))
