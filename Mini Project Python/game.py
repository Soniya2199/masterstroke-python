import turtle as tl
from turtle import *
import time
import random

window=tl.Screen()
window.title('Snake Game')
window.setup(600,600)
window.bgcolor('#899000')
# window.tracer(0)

snake_Body=[]
for i in range(10):
    t=tl.Turtle('classic')
    tl.color('red')
    tl.speed(0)
    tl.showturtle()
    tl.shapesize(1.5)
    tl.penup()
    tl.goto(0,20*i)
    tl.pendown()
    time.sleep(1.5)
    snake_Body.append(tl)
print(snake_Body)
	
# fruit=tl.Turtle('turtle')
# tl.color('dark blue')
# tl.speed()


def up():
	t.setheading(90)
	t.forward(30)

def down():
	t.setheading(270)
	t.forward(30)

def left():
	t.setheading(180)
	t.forward(30)

def right():
	t.setheading(0)
	t.forward(30)

tl.listen()
tl.onkey(up, 'Up')
tl.onkey(down, 'Down')
tl.onkey(left, 'Left')
tl.onkey(right, 'Right')
# tl.done()
window.mainloop()
