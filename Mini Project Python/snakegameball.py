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

segments = []

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

def go_up(): 
    if head.direction != "down": head.direction = "up"

def go_down(): 
    if head.direction != "up": head.direction = "down"

def go_left(): 
    if head.direction != "right": head.direction = "left"

def go_right(): 
    if head.direction != "left": head.direction = "right"

screen.listen() 
screen.onkey(go_up, "Up") 
screen.onkey(go_down, "Down") 
screen.onkey(go_left, "Left") 
screen.onkey(go_right, "Right")

while True: 
    screen.update()

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segments first in reverse order
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for collision with wall
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

    time.sleep(0.1)