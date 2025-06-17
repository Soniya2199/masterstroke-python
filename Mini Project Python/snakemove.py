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
snake.penup()
snake.speed(10)

speed=1

def up():
	snake.setheading(90)
	snake.forward(15)

def down():
	snake.setheading(270)
	snake.forward(15)

def left():
	snake.setheading(180)
	snake.forward(15)

def right():
	snake.setheading(0)
	snake.forward(15)


#! key press movements	
screen.listen()
screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')

while True:
	snake.forward(speed)

tl.done()
screen.mainloop()