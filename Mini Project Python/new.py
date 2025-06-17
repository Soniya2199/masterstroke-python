import turtle as tl
from turtle import *
import random as r
import time

#!! Main Screen 
screen = tl.Screen()
screen.title("Snake Game")
screen.bgcolor("#388004")
screen.setup(width=600, height=600)

#! Snake head
snake = tl.Turtle() #? created turtle obj
snake.shape("classic")
snake.color("#071e91")
snake.shapesize(1.5)
snake.speed(0)
snake.penup()

#! food shape
def snake_Food():
    for i in range(100):
        food =tl.Turtle()
        shapes=r.choice(['circle','arrow','turtle','triangle','square'])
        food.shape(shapes)
        colors=r.choice(['#decd10','#c95555','#09e3a5','#b267eb','#450606','#e08a2d','#2de0b9'])
        food.color(colors)
        food.shapesize(0.7)
        food.penup()
        food.speed(2)
        x=r.randint(-600,600)
        y=r.randint(-300,300)
        food.goto(x,y)
        time.sleep(1)

#! move upward
def up():
	snake.setheading(90)
	snake.penup()
	snake.forward(15)
	
#! move downward
def down():
	snake.setheading(270)
	snake.penup()
	snake.forward(15)
	
#! move left	
def left():
	snake.setheading(180)
	snake.penup()
	snake.forward(15)

#! move right	
def right():
	snake.setheading(0)
	snake.penup()
	snake.forward(15)

#! key press movements	
snake.listen()
snake.onkey(up, 'Up')
snake.onkey(down, 'Down')
snake.onkey(left, 'Left')
snake.onkey(right, 'Right')

screen.mainloop()