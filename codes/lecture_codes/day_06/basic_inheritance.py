class Ball:
    def __init__(self):
        print("Ball is ready")

    def get_class_name(self):
        print("Ball")

    def play(self):
        print("Lets play ball")


class BasketballBall(Ball):
    def __init__(self):
        # call super() function
        super().__init__()
        print("Basketball ball is ready")

    def get_class_name(self):
        print("BasketballBall")

    def play(self):
        print("Lets play basketball")

random_ball = Ball()
random_ball.get_class_name()
random_ball.play()
print('-----------------------------')
mikasa = BasketballBall()
mikasa.get_class_name()
mikasa.play()