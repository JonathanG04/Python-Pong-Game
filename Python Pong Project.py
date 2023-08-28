import turtle
import time


win = turtle.Screen()
win.title("Pong")
win.bgcolor("white")
win.setup(width=800, height=600)
win.tracer(0)

#tracks score for each player
score_for_a = 0
score_for_b = 0

#display for the score
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: {}  Player B: {}".format(score_for_a, score_for_b), align="center", font=("Purisa", 24, "normal"))

#creates each player's paddles
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

#this controls the game loop
game_over = False

#below function pauses the game for a specific duration to provide player with a choice at the end
def pause(duration):
    time.sleep(duration)

def declare_game_over(winner):
    score_display.clear()
    score_display.goto(0, 0)
    score_display.write("{} wins! Game Over".format(winner), align="center", font=("Purisa", 36, "normal"))

def paddle_a_moving_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_moving_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_moving_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_moving_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

win.listen()
win.onkeypress(paddle_a_moving_up, "w")
win.onkeypress(paddle_a_moving_down, "s")
win.onkeypress(paddle_b_moving_up, "Up")
win.onkeypress(paddle_b_moving_down, "Down")

#ensures no error occurs in the terminal once the game is over
while True:
    win.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #this establishes barriers for the ball
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_for_a += 1
        score_display.clear()
        score_display.write("Player A: {}  Player B: {}".format(score_for_a, score_for_b), align="center", font=("Purisa", 24, "normal"))
        if score_for_a >= 5:
            declare_game_over("Player A")


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_for_b += 1
        score_display.clear()
        score_display.write("Player A: {}  Player B: {}".format(score_for_a, score_for_b), align="center", font=("Purisa", 24, "normal"))
        if score_for_b >= 5:
            declare_game_over("Player B")

    if score_for_a >= 5 or score_for_b >= 5:
        declare_game_over("Player A" if score_for_a >= 5 else "Player B")
        game_over = True

        #pauses the game for a brief period
        pause(5)
        response = turtle.textinput("Game Over", "Press 'q' to quit or 'r' to play again:")
        if response and response.lower() == "q":
            break
        else:
            game_over = False
            score_for_a = 0
            score_for_b = 0
            score_display.clear()
            score_display.goto(0, 260) #ensures the score does not move down the screen after another restart
            score_display.write("Player A: {}  Player B: {}".format(score_for_a, score_for_b), align="center", font=("Purisa", 24, "normal"))
            ball.goto(0, 0)
            ball.dx = 1
            ball.dy = -1
            time.sleep(1) #this pauses the game for a second before restarting

    #creates collision between each paddle and the ball
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.color("pink")
        ball.dx *= -1

    elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.color("orange")
        ball.dx *= -1
    
