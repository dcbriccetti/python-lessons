import turtle as t

t.speed('fastest')

sides = int(input('Num sides in the largest polygon? '))
for sides in range(3, sides + 1):
    for side in range(sides):
        t.fd(100)
        t.right(360 / sides)

input('Press enter to continue')
