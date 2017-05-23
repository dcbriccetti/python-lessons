class Paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 80

    def draw(self):
        print('Drawing at %d, %d' % (self.x, self.y))

    def move(self, amount):
        self.y += amount

left_paddle  = Paddle(10, 10)
left_paddle.draw()
right_paddle = Paddle(400, 10)
right_paddle.draw()

left_paddle.move(1)
left_paddle.draw()

