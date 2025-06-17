import turtle as tl
import random as r
import time

#! Main Screen 
screen=tl.Screen()
screen.title("Snake Game")
screen.bgcolor("grey")
screen.setup(width=600, height=600)
screen.tracer(0)

#! Snake head
snake = tl.Turtle()
snake.speed(0)
snake.shape("classic")
snake.color("#071e91")
snake.shapesize(2)
snake.penup()
snake.goto(0,0)
snake.direction='stop'

#! food
food =tl.Turtle()
food.speed(0)
food.penup()
food.goto(0,100)

body=[]

score=0
max_score=50
scores=tl.Turtle()
scores.speed(0)
scores.color("black")
scores.penup()
scores.hideturtle()
scores.goto(0,270)
scores.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

#! move functions
def up():
    snake.direction='up'
    snake.setheading(90)

def down():
    snake.direction='down'
    snake.setheading(270)

def left():
    snake.direction='left'
    snake.setheading(180)

def right():
    snake.direction='right'
    snake.setheading(0)

#!main key moves function
def move():
    if snake.direction=='up':
        snake.sety(snake.ycor()+15)
    if snake.direction=='down':
        snake.sety(snake.ycor()-15)
    if snake.direction=='left':
        snake.setx(snake.xcor()-15)
    if snake.direction=='right':
        snake.setx(snake.xcor()+15)

#! key press movements	
screen.listen()
screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(left,"Left")
screen.onkey(right,"Right")

def restart():
    global score
    time.sleep(1)
    snake.goto(0,0)
    snake.direction='stop'
    
    for xy in body:
        xy.goto(1000,1000)
    body.clear()
    score=0
    update_mark()

def update_mark():
    scores.clear()
    scores.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

#! loop
while True:
    screen.update()
   
    #! sw
    if snake.distance(food)<15:
        food.shapesize(0.7)
        shapes=r.choice(['circle','arrow','turtle','triangle','square'])
        food.shape(shapes)
        colors=r.choice(['#decd10','#c95555','#09e3a5','#b267eb','#450606','#e08a2d','#2de0b9'])
        food.color(colors)
        food.goto(r.randint(-260,260),r.randint(-260,260))
        
        #! snake body grows
        snake_Body=tl.Turtle()
        snake_Body.speed(0)
        snake_Body.shapesize(0.7)
        snake_Body.shape("circle")
        colors=r.choice(['#decd10','#c95555','#09e3a5','#b267eb','#450606','#e08a2d','#2de0b9'])
        snake_Body.color(colors)
        snake_Body.penup()
        body.append(snake_Body)

        score+=10
        update_mark()

        if score>=max_score:
            scores.clear()
            scores.write("you won the game", align="center", font=("times new roman", 18, "normal"))
            time.sleep(2)
            restart()

    for i in range(len(body) - 1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)

    if len(body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)

    move()

    if snake.xcor() > 280 or snake.xcor() < -280 or snake.ycor() > 280 or snake.ycor() < -280:
        restart()

        for xy in body:
            if snake.direction(xy)>15:
                restart()
    time.sleep(0.1)

screen.mainloop()