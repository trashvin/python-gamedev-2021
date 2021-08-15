class Ball:

    # instance attributes
    # contructor
    def __init__(self, name, color = 'white'):
        self.name = name
        self.color = color

    # instance method
    def bounce(self):
        print(f'{self.name} is bouncing')

# instantiate the object
beach_ball = Ball('beach ball', 'red')
baseball_ball = Ball('baseball ball')

beach_ball.bounce()
print(baseball_ball.color)