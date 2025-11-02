from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

# Detect collision with top and bottom walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
# Detect collision with paddles
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.bounce_x()
# Detect R paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
# Detect L paddle misses
    if ball.xcor() < -390:
        ball.reset_position()

screen.exitonclick()
