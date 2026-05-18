from turtle import *
import random
import time

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('white')
    pen.begin_fill()
    pen.goto(130,200)
    pen.goto(130,-200)
    pen.goto(-130,-200)
    pen.goto(-130,200)
    pen.goto(130,200)
    pen.end_fill()


    

class Player(Turtle):
    def __init__(self, x, y, color, screen, right_key, left_key, fire_key, health):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(x,y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.hue = color
        self.alive = True
        self.health = health
        self.score = 0
        self.st()
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkey(self.fire, fire_key)

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def fire(self):
        if len(self.bullets)<5:
            new_bullet = Bullet(self)
            self.bullets.append(new_bullet)


class Score(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.ht()
        self.color("white")
        self.pu()
        self.goto(x, y)
        self.score = 0
        self.write(f"Score: {self.score}")
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}")
        
      


class Block(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.ht()
        self.speed(0)
        self.pu()
        self.shape("square")
        self.goto(x,y)
        self.color(color)
        self.st()
        self.health = 3
        self.alive = True
    
    def hit(self,blocks,player, scores):
        self.health -= 1
        if self.health == 2:
            self.color("orange")
        elif self.health == 1:
            self.color("red")
        elif self.health == 0:
            self.ht()
            blocks.remove(self)
            scores.score += 1
            
            

            

class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.ht()
        self.speed(0)
        self.pu()
        self.setheading(player.heading())
        self.color(player.hue)
        self.player = player
        self.goto(player.xcor(),player.ycor())
        self.st()
        

    def move(self):
        self.forward(10)
        if self.xcor() > 130 or self.xcor() < -130:
            self.setheading(180 - self.heading())
        if self.ycor() > 130:
            self.die()

    def die(self):
        self.ht()
        if self in self.player.bullets:
            self.player.bullets.remove(self)
                 


def update():
    # if time.time() - start > 2:
    #     start = time.time()
    if p1.alive and p2.alive:
        for bullet in p1.bullets:
            bullet.move()
            for block in blocks:
                if bullet.distance(block) < 20:
                    bullet.die()
                    block.hit(blocks, p1, score1)
                    score1.update_score()
        for bullet in p2.bullets:
            bullet.move()
            for block in blocks:
                if bullet.distance(block) < 20:
                    bullet.die()
                    block.hit(blocks, p2, score2)
                    score2.update_score()
    

    screen.ontimer(update,30)

   
        
    





screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
screen.listen()


playing_area()


blocks = []
bullets = []
p1 = Player(-70, -180, "red",screen, "d", "a", "w",1)
p2 = Player(70,-180,"blue",screen, "Right","Left", "Up",1)
score1 = Score(-200,200,"white")
score2 = Score(200,200, "white")

screen.tracer(0)
for y in range(190,120,-20):
    for x in range(-120,130,20):
        if len(blocks) % 3 == 0:
            blocks.append(Block(x,y,"lightgray"))
        elif len (blocks) % 3 == 1:
            blocks.append(Block(x,y, "gray"))
        else:
            blocks.append(Block(x,y, "darkgray"))
screen.tracer(1)

update()

screen.exitonclick()

### CLASS and FUNCTION DEFINITIONS ###










### PROGRAM ###
screen = Screen()





screen.exitonclick()