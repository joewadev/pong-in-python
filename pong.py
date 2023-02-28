import turtle

# conda activate py-pong-3110

# Set up game screen
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(800, 600)
wn.tracer(0)

score1 = 0
score2 = 0

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("red")
paddle1.shapesize(stretch_wid=5, stretch_len=1) # make the paddle wider
paddle1.penup()
paddle1.goto(-350, 0)

paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.color("blue")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350,0)

# Creating the Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.5
ball.dy = -0.5

# Game Rules
game_over = False
winner = None
points = {
    "player1": 0,
    "player2": 0
}
game_rules = {
    "max_points": 3,
    "ball_speed": 3
}

# Score Display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0 Player 2: 0", align="center", font=("Arial", 24, "normal"))

# Function to move paddle1 up
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)

# Set up keyboard bindings
turtle.listen()
turtle.onkeypress(paddle1_up, "w")
turtle.onkeypress(paddle1_down, "s")
turtle.onkeypress(paddle2_up, "Up")
turtle.onkeypress(paddle2_down, "Down")

# Main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= 1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score_display.clear()
        score_display.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Arial", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score_display.clear()
        score_display.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Arial", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
