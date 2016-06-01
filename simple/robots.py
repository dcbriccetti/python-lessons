class Robot(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hi. I am %s.' % self.name)

class EvilRobot(Robot):
    def __init__(self, name):
        super().__init__(name)

    def greet(self):
        print('I am %s, and I am not pleased to see you humans here!' % self.name)

robots = (Robot("Robbie"), Robot("Data"), EvilRobot("Lor"))

for robot in robots:
    robot.greet()

