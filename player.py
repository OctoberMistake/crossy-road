from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.x_pos = STARTING_POSITION[0]
        self.y_pos =  STARTING_POSITION[1]
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.color("darkolivegreen")
        self.left(90)
        self.alive = True

    def walk(self, x, y):
        if self.alive:
            self.y_pos = self.ycor() + 10
            self.goto(self.x_pos, self.y_pos)

    def rst(self):
        self.teleport(0, -280)
    
    def hited(self):
        self.alive = False
        self.color("black")


