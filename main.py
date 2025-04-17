from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_l = Paddle(-350, 0)
paddle_r = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=paddle_r.move_up)
screen.onkey(key="Down", fun=paddle_r.move_down)
screen.onkey(key="w", fun=paddle_l.move_up)
screen.onkey(key="s", fun=paddle_l.move_down)




game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with controlllers
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or  ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect when the right paddle misses
    if ball.xcor() > 380:
        ball.restart_position()
        scoreboard.l_point()
    # Detect when the left paddle misses
    if ball.xcor() < -380:
        ball.restart_position()
        scoreboard.r_point()

screen.exitonclick()