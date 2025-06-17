import turtle as tl
import random as r
import time

#!! Main Screen 
screen = tl.Screen()
screen.title("Snake Game")
screen.bgcolor("#388004")
screen.setup(width=600, height=600)
screen.tracer(0)

#! Snake head
snake_body=[]
for i in range(3):
    snake = tl.Turtle() #? created turtle obj
    snake.shape("classic")
    snake.color("orange")
    snake.shapesize(1.5)
    snake.speed(0)
    snake.penup()
    snake.goto(0,0)
    snake_body.append(snake)
    time.sleep(0.5)

speed=1

food =tl.Turtle()
shapes=r.choice(['circle','arrow','turtle','triangle','square'])
food.shape(shapes)
colors=r.choice(['#decd10','#c95555','#09e3a5','#b267eb','#450606','#e08a2d','#2de0b9'])
food.color(colors)
food.shapesize(0.7)
food.penup()
food.goto(0,100)

score = 0
score_display = tl.Turtle()
score_display.color("Black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

direction='stop'

def move(): 
    if direction != "stop":
        for i in range(len(snake) -1, 0, -1):
            x, y = snake[i - 1].pos()
            snake[i].goto(x, y)
        if direction == "up":
            snake[0].sety(snake[0].ycor() + 20)
        elif direction == "down":
            snake[0].sety(snake[0].ycor() - 20)
        elif direction == "left":
            snake[0].setx(snake[0].xcor() - 20)
        elif direction == "right":
            snake[0].setx(snake[0].xcor() + 20)

def up(): 
    global direction
    if direction != "down": 
        direction = "up"

def down(): 
    global direction
    if direction != "up": 
        direction = "down"

def left(): 
    global direction
    if direction != "right": 
        direction = "left"

def right(): 
    global direction
    if direction != "left": 
        direction = "right"

screen.listen() 
screen.onkey(up, "Up") 
screen.onkey(down, "Down") 
screen.onkey(left, "Left") 
screen.onkey(right, "Right")


while True:
    screen.update()
    move()
    
#     if snake[0].distance(food) < 15:
#         food.goto(r.randint(-280, 280), r.randint(-280, 280)) 
#         new_segment = tl.Turtle("square")
#         new_segment.color("white")
#         new_segment.penup()
#         snake.append(new_segment)
#         score += 10
#         score_display.clear()
#         score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))
#     if (
#         snake[0].xcor() > 290 or snake[0].xcor() < -290 or
#         snake[0].ycor() > 290 or snake[0].ycor() < -290
#     ):
#         game_running = False
#         score_display.goto(0, 0)
#         score_display.write("Game Over!", align="center", font=("Arial", 20, "bold"))

    
#     for segment in snake[1:]:
#         if snake[0].distance(segment) < 10:
#             game_running = False
#             score_display.goto(0, 0)
#             score_display.write("Game Over!", align="center", font=("Arial", 20, "bold"))
            
# while True:
#     screen.update()
#     # snake.forward(speed)

#     if snake.distance(food) < 20:
#        x=r.randint(-600,600)
#        y=r.randint(-300,300)
#        food.goto(x, y)
       
#        new_segment = tl.Turtle()
#        new_segment.speed(0)
#        new_segment.shape("circle")
#        colors=r.choice(['#decd10','#c95555','#09e3a5','#b267eb','#450606','#e08a2d','#2de0b9'])
#        new_segment.color(colors)
#        new_segment.penup()
#        segments.append(new_segment)
    
#     for i in range(len(segments) - 1, 0, -1):
#         x = segments[i - 1].xcor()
#         y = segments[i - 1].ycor()
#         segments[i].goto(x, y)

#     if len(segments) > 0:
#         x = snake.xcor()
#         y = snake.ycor()
#         segments[0].goto(x, y)

#     move()
#     if snake.xcor() > 600 or snake.xcor() < -600 or snake.ycor() > 300 or snake.ycor() < -300:
#         time.sleep(1)
#         snake.goto(0, 0)
#         snake.direction = "stop"
        
#         for segment in segments:
#             segment.goto(1000, 1000)
#         segments.clear()

#     for segment in segments:
#         if snake.distance(segment) < 20:
#             time.sleep(1)
#             snake.goto(0, 0)
#             snake.direction = "stop"
            
#             for segment in segments:
#                 segment.goto(1000, 1000)
#             segments.clear()

    time.sleep(0.1)

screen.mainloop()