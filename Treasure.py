import turtle


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.gold = 100
        self.goto(x, y)
        self.shapesize(0.25,0.25)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()