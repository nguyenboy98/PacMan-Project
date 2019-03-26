import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Runner")
wn.setup(772, 868)
wn.tracer(0)


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.direction = ['up', 'down', 'left', 'right']


class Weapon(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.goto(x, y)
        self.velocity = 10

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

    def move(self, other):
        if other.direction == 'up':
            self.direction = 'up'
            dx = 0
            dy = 24
        elif other.direction == 'down':
            self.direction = 'down'
            dx = 0
            dy = -24
        elif other.direction == 'left':
            self.direction = 'left'
            dx = 24
            dy = 0
        elif other.direction == 'right':
            self.direction = 'right'
            dx = -24
            dy = 0
        else:
            dx = 0
            dy = 0

        x = self.xcor() + dx*self.velocity
        y = self.ycor() + dy*self.velocity

        if (x, y) in enemies:
            self.goto(x, y)
            Enemy.destroy()
        else:
            self.direction = random.choice(["up",
                                            "down",
                                            "left",
                                            "right"])

    def colission(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        x = self.xcor()
        y = self.ycor() + 24
        if (x, y) not in walls:
            self.goto(x, y)
        print("Player: ", x, y)

    def go_down(self):
        x = self.xcor()
        y = self.ycor() - 24
        if (x, y) not in walls:
            self.goto(x, y)
        print("Player: ", x, y)

    def go_right(self):
        x = self.xcor() + 24
        y = self.ycor()
        if (x, y) not in walls:
            self.goto(x, y)
        print("Player: ", x, y)

    def go_left(self):
        x = self.xcor() - 24
        y = self.ycor()
        if (x, y) not in walls:
            self.goto(x, y)
        print("Player: ", x, y)

    def collission(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a**2)+(b**2))

        if distance < 5:
            return True
        else:
            return False


class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("Pink")
        self.pendown()
        self.speed(10)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up",
                                        "down",
                                        "left",
                                        "right"])

    def move(self):

        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = 24
            dy = 0
        elif self.direction == "right":
            dx = -24
            dy = 0
        else:
            dx = 0
            dy = 0
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        x = self.xcor() + dx
        y = self.ycor() + dy

        if (x, y) not in walls:
            self.goto(x, y)
        else:
            self.direction = random.choice(["up",
                                            "down",
                                            "left",
                                            "right"])
        turtle.ontimer(self.move, t=10)
        print("Enemy: ", x, y)

    def is_close(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2)+(b**2))

        if distance < 25:
            print("True")
            return True
        else:
            print("False")
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


levels = [""]

level1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X                          X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X   XX XX XXXXXXXX XX XX   X",
    "XXX XX XX          XX XX XXX",
    "XXX XX XXXXX XX XXXXX XX XXX",
    "XXX    XXXXX XX XXXXX    XXX",
    "XXX XX XX    XX    XX XX XXX",
    "XXX XX XX XXXXXXXX XX XX XXX",
    "XXX XX XX XXXXXXXX XX XX XXX",
    "X   XX XX     E    XX XX   X",
    "X XXXX XX XXX  XXX XX XXXX X",
    "X XXXX    X E    X    XXXX X",
    "X   XX XX X E    X XX XX   X",
    "XXX XX XX X E    X XX XX XXX",
    "XXX XX XX XXXXXXXX XX XX XXX",
    "X      XX          XX      X",
    "XXX XXXXX XXXXXXXX XXXXX XXX",
    "XXX XXXXX XXXXXXXX XXXXX XXX",
    "X      XX          XX      X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X XX      XX    XX      XX X",
    "X XX XXXX XX XX XX XXXX XX X",
    "X XX XXXX XX XX XX XXXX XX X",
    "X      XX    XX    XXP     X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X      XX          XX      X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ]

levels.append(level1)


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            cha = level[y][x]
            screen_x = -336 + (x * 24)
            screen_y = 384 - (y * 24)
            if cha == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            if cha == 'P':
                player.goto(screen_x, screen_y)
            if cha == 'T':
                treasures.append(Treasure(screen_x, screen_y))

            if cha == 'E':
                enemies.append(Enemy(screen_x, screen_y))

            if cha == 'W':
                weapons.append(Weapon(screen_x, screen_y))


weapons = []
enemies = []
treasures = []
player = Player()
walls = []
pen = Pen()
setup_maze(levels[1])



# Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")


wn.tracer(0, 0)

for enemy in enemies:
    turtle.ontimer(enemy.move(), t=250)


while True:
    for treasure in treasures:
        if player.collission(treasure):
            player.gold += treasure.gold
            print("player gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

    for enemy in enemies:
        if player.collission(enemy):
            player.hideturtle()
            print("Player died!")
        for weapon in weapons:
            if weapon.colission(enemy):
                print("enemy died!")
                weapon.destroy()
                enemy.destroy()
                weapons.remove(weapon)
                enemies.remove(enemy)


    wn.update()
