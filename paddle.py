from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.y_coordinate = 0
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(position_x, position_y)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
