import turtle as tl
from turtle import *
import random as r
import time

#! Main Screen 
screen = tl.Screen()
screen.title("Snake Game")
screen.bgcolor("#388004")
screen.setup(width=700, height=500)

#! food shape
for i in range(100):
    
    food =tl.Turtle()
    food.hideturtle()
    shapes=r.choice(['circle','arrow','turtle','triangle','square'])
    food.shape(shapes)
    colors=r.choice(['#decd10','#c95555','#09e3a5','#b267eb','#450606','#e08a2d','#2de0b9'])
    food.color(colors)
    food.shapesize(0.7)
    food.penup()
    food.speed(0)
    x=r.randint(-600,600)
    y=r.randint(-300,300)
    food.goto(x,y)
    time.sleep(1)
    food.showturtle()

screen.mainloop()