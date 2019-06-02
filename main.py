import threading
import turtle
import math
import random
from Pen import *
from Treasure import *

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("PacMan --version 0.5")
wn.setup(772, 868)
wn.tracer(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 0
        self.state = 'normal'
        self.direction = 'Left'

    def go_up(self):
        x = self.xcor()
        y = self.ycor() + 24
        if (x, y) not in walls:
            self.goto(x, y)
        # print("Player: ", x, y)
        self.direction = 'up'

    def go_down(self):
        x = self.xcor()
        y = self.ycor() - 24
        if (x, y) not in walls:
            self.goto(x, y)
        # print("Player: ", x, y)
        self.direction = 'down'

    def go_right(self):
        x = self.xcor() + 24
        y = self.ycor()
        if (x, y) not in walls:
            self.goto(x, y)
        # print("Player: ", x, y)
        self.direction = 'right'

    def go_left(self):
        x = self.xcor() - 24
        y = self.ycor()
        if (x, y) not in walls:
            self.goto(x, y)
        # print("Player: ", x, y)
        self.direction = 'left'

    def move_continues(self):
        if self.direction == 'left':
            self.go_left()

        elif self.direction == 'right':
            self.go_right()

        elif self.direction == 'up':
            self.go_up()

        elif self.direction == 'down':
            self.go_down()

        else:
            self.go_left()

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
        self.penup()
        self.speed(10)
        self.gold = 25
        self.x = x
        self.y = y
        self.goto(self.x, self.y)
        self.direction = random.choice(["up",
                                        "down",
                                        "left",
                                        "right"])


    def move(self):
        wallleft = self.x - 24
        wallright = self.x + 24
        wallup = self.y + 24
        walldown = self.y - 24
        print("Status: ",player.state)

        self.chasing()

        if self.direction == "up":
            # print("up")
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
            # print("down")
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        # print("dx ", dx)
        # print("dy ", dy)

        self.x = self.x + dx
        self.y = self.y + dy



        if (self.x, self.y) not in walls:
            self.goto(self.x, self.y)
        # elif x <= -360:
        #     x=312
        #     y=-24
        #     self.goto(x, y)
        # elif x >= 336:
        #     x = -336
        #     y = -24
        #     self.goto(x, y)
        else:
            wallleft = self.x - 24
            wallright = self.x +24
            wallup = self.y + 24
            walldown = self.y -24
            if ((wallleft,self.y) and (wallright,self.y)) in walls:
                if ((self.x),wallup) in walls:
                    self.direction = "down"
                if (self.x, walldown) in walls:
                    self.direction = "up"
            elif ((self.x, wallup) and (self.x, walldown)) in walls:
                if (wallleft,self.y) in walls:
                    self.direction = "right"
                if (wallright,self.y) in walls:
                    self.direction = "left"
        turtle.ontimer( self.move, t=180)
        print("Enemy: ", self.x, self.y)


    def is_close(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2)+(b**2))
        # print("a: ", a)
        # print("b: ", b)
        # print("distance: ",distance)
        if distance < 901:
            # print("True")
            return True
        else:
            # print("False")
            return False

    def calculateUpDown(self,x,y,first,second):
        x=self.x
        y=self.y

        x1=x
        y1=y

        firstPoint = 0
        secondPoint = 0
        if (first,second) is ("up","down"):
            while((x1+24) in walls):
                y1 +=24
                firstPoint += 1
            x1 = x
            y1 = y
            while ((x1 + 24) in walls):
                y1 -= 24
                secondPoint += 1

            if secondPoint > firstPoint:
                return "up"
            else:
                return "down"

        if (first,second) is ("left","right"):
            while((y1-24) in walls):
                x1 +=24
                firstPoint += 1
            x1 = x
            y1 = y
            while ((y1 - 24) in walls):
                x1 -= 24
                secondPoint += 1

            if secondPoint > firstPoint:
                return "up"
            else:
                return "down"


    def chasing(self):
        if self.is_close(player):
            if (player.xcor() < self.x):
                if player.xcor() in walls:
                    self.direction = self.calculateUpDown(self.x,self.y,'up','down')

                # print("Turn left")
                self.direction = "left"
            elif player.xcor() > self.x:
                if player.xcor() in walls:
                    self.direction = self.calculateUpDown(self.x,self.y,'up','down')
                # print("Turn right")
                self.direction = "right"
            elif player.ycor() < self.y:
                if self.y +24 in walls:
                    self.direction = self.calculateUpDown(self.x,self.y,'left','right')
                # print("Turn down")
                self.direction = "down"
            elif player.ycor() > self.y:
                # print("Turn up")
                self.direction = "up"

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Shield(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("Blue")
        self.penup()
        self.x = x
        self.y = y
        self.goto(self.x, self.y)
        self.status = 'shield'

    def collission(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()




levels = [""]
mess=[""]

level1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XE                         X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X   XX XX XXXXXXXX XX XX   X",
    "XXX XX XX          XX XX XXX",
    "XXX XX XXXXX XX XXXXX XX XXX",
    "XXX    XXXXX XX XXXXX    XXX",
    "XXX XX XX    XX    XX XX XXX",
    "XXX XX XX XXXXXXXX XX XX XXX",
    "XXX XX XX XXXXXXXX XX XX XXX",
    "X   XX XX          XX XX   X",
    "X XXXX XX XXX  XXX XX XXXX X",
    "X XXXX    X      X    XXXX X",
    "X   XX XX X      X XX XX P X",
    "XXX XX XX X      X XX XX XXX",
    "XXX XX XX XXXXXXXX XX XX XXX",
    "       XX          XX       ",
    "XXX XXXXX XXXXXXXX XXXXX XXX",
    "XXX XXXXX XXXXXXXX XXXXX XXX",
    "X      XX          XX      X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X XX      XX    XX      XX X",
    "X XX XXXX XX XX XX XXXX XX X",
    "X XX XXXX XX XX XX XXXX XX X",
    "X      XX    XX    XX    S X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X      XX          XX      X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ]

mess1=[
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X                           X",
    "X  XXXXX    X   X   X XXXX  X",
    "X  X      X   X XX XX X     X",
    "X  X  XXX X   X X X X XXXX  X",
    "X  X   X  XXXXX X   X X     X",
    "X  XXXXX  X   X X   X XXXX  X",
    "X                           X",
    "X    XXX  X    X XXXX XXXX  X",
    "X   X   X X    X X    X  X  X",
    "X   X   X X    X XXXX XXXX  X",
    "X   X   X  X  X  X    X X   X",
    "X    XXX    XX   XXXX X  X  X",
    "X                           X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

mess.append(mess1)
levels.append(level1)


def setup_maze(level):
    print("Maze")
    for y in range(len(level)):
        for x in range(len(level[y])):
            cha = level[y][x]
            screen_x = -336 + (x * 24)
            screen_y = 384 - (y * 24)
            if cha == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if cha == "S":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                shields.append(Shield(screen_x, screen_y))

            if cha == 'E':
                enemies.append(Enemy(screen_x, screen_y))
                print("x: ", screen_x , " y: " , screen_y)

            if cha == ' ' and cha != 'P' and cha !='E':
                treasures.append(Treasure(screen_x,screen_y))

            if cha == 'P':
                print("Repeat")
                player.goto(screen_x, screen_y)
                print("x: ", screen_x, " y: ", screen_y)


def print_mess(mess1):
    for y in range(len(mess1)):
        for x in range(len(mess1[y])):
            cha = mess1[y][x]
            screen_x = -360 + (x * 24)
            screen_y = 360 - (y * 24)
            if cha == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()

shields = []
enemies = []
treasures = []
player = Player()
walls = []
pen = Pen()




# Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")


wn.tracer(0, 0)

def cancel():
    threading.Timer(5.0, cancel).start()
    player.state = 'normal'

def play():

    setup_maze(levels[1])

    for enemy in enemies:
        turtle.ontimer(enemy.move, t=250)
    while True:
        x = player.xcor()
        y = player.ycor()

        for shield in shields:
            if player.collission(shield):
                player.state = 'shield'
                print("After eat shield, status: ", player.state)
                shield.destroy()
                # cancel()




        for treasure in treasures:
            if player.collission(treasure):
                player.gold += treasure.gold
                print("player gold: {}".format(player.gold))
                treasure.destroy()
                treasures.remove(treasure)

        for enemy in enemies:
            if player.collission(enemy) and player.state == 'normal':
                player.goto(2000,2000)
                player.hideturtle()
                mess='done'
                if mess== 'done':
                    print("Player died!")

                    f=open('score.txt','w')
                    f.write("Score: "+ str(player.gold))
                    f.close()
                    wn.clear()
                    wn.bgcolor("black")
                    print_mess(mess1)
            if player.collission(enemy) and player.state == 'shield':
                enemy.goto(2000,2000)
                enemy.destroy()
                player.gold += enemy.gold



        if x <= -360:
            player.goto(312,-24)
        elif x >= 336:
            player.goto(-336,-24)
        # turtle.ontimer(player.move_continues(),t=200)



        wn.update()
play()