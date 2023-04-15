name = "Sue"
age = 12
score = 95

print(name, age, score)
print(name + str(age) + str(score))
print(name + " " + str(age) + " " + str(score))
print(name + ", " + str(age) + ", " + str(score))

print(name + ", age", str(age) + ", scored", score)
print(name + ", age", str(age) + ", scored " + str(score))
print("%s, age %d, scored %x" % (name, age, score))
print(f"{name}, age {age}, scored {score}")
