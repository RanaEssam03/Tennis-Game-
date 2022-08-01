import turtle

screen = turtle.Screen()
turtle.bgcolor("black")
ball = turtle.Turtle()
ball.shape("circle")
ball.color("green")
screen.title("Tennis Game")
screen.tracer(0)
turtle.speed(0)
ball.penup()
ball.speed(0)
y1 = turtle.Turtle()
y1.shape("square")
y1.color("white")
y1.shapesize(stretch_wid=5, stretch_len=1)
y1.penup()
y1.goto(360, 0)
y2 = turtle.Turtle()
y2.shape("square")
y2.color("pink")
y2.shapesize(stretch_wid=5, stretch_len=1)
y2.penup()
y2.goto(-360, 0)


txtbox = turtle.Turtle()
txtbox.hideturtle()
txtbox.shapesize(stretch_wid=7, stretch_len=2)
txtbox.color('white')


def up():
    if y1.ycor() < 250:
        y = y1.ycor()
        y+=20
        y1.sety(y)

def down():
    if y1.ycor() > -250:
        y = y1.ycor()
        y-=20
        y1.sety(y)

screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")

def up1():

    if y2.ycor() < 250  :
        y = y2.ycor()
        y += 20
        y2.sety(y)


def down1():
    if y2.ycor() > -250:
        y = y2.ycor()
        y-=20
        y2.sety(y)

screen.onkeypress(up1, "w")
screen.onkeypress(down1, "s")


ball_dx = 0.2
ball_dy =0.2

score1 = 0
score2 = 0

screen.setup(width=800,height=600)

while True:
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)



    if ball.ycor()>= 299 or ball.ycor()<= -299 :
        ball_dy *= -1



    if ball.ycor() >= y1.ycor()-50 and ball.ycor() <= y1.ycor()+50   and ball.xcor() >= 360:
        ball_dx *= -1

    if ball.ycor() >= y2.ycor() - 50 and ball.ycor() <= y2.ycor() + 50 and ball.xcor() <= -360:
        ball_dx *= -1

    if ball.xcor() >= 380:
        ball.goto(0, 0)
        ball_dx *= -1
        if score1 >= 4 :
            txtbox.clear()
            txtbox.write("The winner is player 1", align="center" , font=("Ubuntu", 30, "bold"))
        else:
            score1 +=1
            txtbox.clear()
            txtbox.write(str(score1) + '      ' + str(score2), align="center" , font=("Ubuntu", 30, "bold"))

    if ball.xcor() <= -380:
        ball.goto(0, 0)
        ball_dx *= -1
        if score2 >= 4 :
            txtbox.clear()
            txtbox.write("The winner is player2", align="center" , font=("Ubuntu", 30, "bold"))

        else:
            score2 += 1
            txtbox.clear()
            txtbox.write(str(score1) + '      ' + str(score2), align="center" , font=("Ubuntu", 30, "bold"))



    screen.update()



