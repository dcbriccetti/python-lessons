'Drill pilots on the mental math of airport traffic pattern flying'

from random import randint, choice

legs = [
    ('crosswind',       270),
    ('downwind',        180),
    ('45 to downwind',  135),
    ('base',            90)
]

while True:
    # Randomly choose a runway heading
    runway_heading = randint(1, 360)

    # Randomly choose a leg
    leg_name, angle = choice(legs)

    # Calculate the runway number
    runway = runway_heading // 10

    # Ask the pilot for the leg direction
    response = input(
        f'You are landing on runway {runway}, left traffic. What direction will you fly on the {leg_name} leg? ')
    if not response:
        break

    leg_heading = int(response)

    # Tell the pilot if they are correct
    actual_leg_heading = ((runway * 10) + angle) % 360

    print('Right! Perhaps you will land successfully.' if leg_heading == actual_leg_heading else
          f'Your error may lead to catastrophe. The correct answer is {actual_leg_heading}.')
