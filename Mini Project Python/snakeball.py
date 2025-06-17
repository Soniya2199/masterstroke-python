import turtle 
import time 
import random

screen = turtle.Screen() 
screen.title("Snake Game") 
screen.bgcolor("black") 
screen.setup(width=600, height=600) 
screen.tracer(0) 

head = turtle.Turtle() 
head.speed(0) 
head.shape("square") 
head.color("white") 
head.penup() 
head.goto(0, 0) 
head.direction = "stop"

food = turtle.Turtle() 
food.speed(0) 
food.shape("circle") 
food.color("red") 
food.penup() 
food.goto(0, 100)

def go_up(): 
    if head.direction != "down": 
        head.direction = "up"

def go_down(): 
    if head.direction != "up": 
        head.direction = "down"

def go_left(): 
    if head.direction != "right": 
        head.direction = "left"

def go_right(): 
    if head.direction != "left": 
        head.direction = "right"

def move(): 
    if head.direction == "up": 
        y = head.ycor() 
        head.sety(y + 20)

if head.direction == "down":
    y = head.ycor()
    head.sety(y - 20)

if head.direction == "left":
    x = head.xcor()
    head.setx(x - 20)

if head.direction == "right":
    x = head.xcor()
    head.setx(x + 20)

screen.listen() 
screen.onkey(go_up, "w") 
screen.onkey(go_down, "s") 
screen.onkey(go_left, "a") 
screen.onkey(go_right, "d")

while True: 
    screen.update()

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

    move()
    time.sleep(0.1)

    turtle.done()
    screen.mainloop()