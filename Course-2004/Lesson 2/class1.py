class Robot:
    def workOn(self, task):
        print(('I am working on', task))
    def giveStatus(self):
        print('Everything is fine')

robot1 = Robot()
robot1.workOn('welding')
robot1.giveStatus()
