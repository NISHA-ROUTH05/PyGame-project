import turtle
import random

score = 0
lives = 3
wn = turtle.Screen()
wn.title("Space Rocket Game Made by Nisha")
wn.bgpic("background.png")
wn.setup(width=600, height=600)
wn.tracer(0)
wn.addshape("rocket.gif")

pen = turtle.Turtle()
pen.up()
pen.hideturtle()
pen.goto(0, 260)
pen.color("white")
pen.write("Score: {} lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

bucket = turtle.Turtle()
bucket.speed(0)
bucket.shape("rocket.gif")
bucket.penup()
bucket.goto(0, -200)
bucket.direction = "stop"

apple = []
for _ in range(20):
    apple = turtle.Turtle()
    apple.speed(0)
    apple.shape("circle")
    apple.color("white")
    apple.penup()
    apple.goto(0, -450)
    apple.direction = "stop"
    #apple.dy = -2
    apple.speed(random.randint(1, 4))


def go_left():
    bucket.direction = "left"


def go_right():
    bucket.direction = "right"


def go_up():
    bucket.direction = "up"


def go_down():
    bucket.direction = "down"


wn.listen()
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")

while True:
    wn.update()

    if bucket.direction == "left":
        x = bucket.xcor()
        x -= 2
        bucket.setx(x)

    if bucket.direction == "right":
        x = bucket.xcor()
        x += 2
        bucket.setx(x)

    if bucket.direction == "up":
        y = bucket.ycor()
        y += 2
        bucket.sety(y)

    if bucket.direction == "down":
        y = bucket.ycor()
        y -= 2
        bucket.sety(y)

    y = apple.ycor()
    y -= 2
    apple.sety(y)

    if y < -300:
        x = random.randint(-380, 380)
        y = random.randint(300, 400)
        apple.goto(x, y)

    if apple.distance(bucket) < 30:
        x = random.randint(-380, 380)
        y = random.randint(300, 400)
        apple.goto(x, y)
        score += 10
        pen.clear()
        pen.write("Score: {} lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    if bucket.xcor() > 290 or bucket.xcor() < -290 or bucket.ycor() > 290 or bucket.ycor() < -290:
        bucket.goto(0, -200)
        bucket.direction = "stop"
        lives -= 1
        pen.clear()
        pen.write("Score: {} lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
        if lives == 0:
            pen.goto(0, 0)
            pen.write("GAME OVER", align="center", font=("courier", 33, "normal"))
            pen.goto(0, -30)
            pen.write("your score is {} ".format(score), align="center", font=("courier", 28, "normal"))
            wn.mainloop()









