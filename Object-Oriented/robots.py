class Robot(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hi, I am ' + self.name)

class SuperRobot(Robot):
    def __init__(self, name):
        super().__init__(name)

    def greet(self):
        print('Watch out, human! I am %s and I am dangerous!' % self.name)

robots = (SuperRobot("Robbie"), Robot("Marvin"), Robot("Rosie"), Robot('Data'))

for robot in robots:
    robot.greet()
