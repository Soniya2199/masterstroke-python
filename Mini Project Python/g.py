import turtle as tl
from turtle import *


window=tl.Screen()
window.title('Snake Game')
window.setup(500, 500)
window.bgcolor('#899000')

t = tl.Turtle()
t.speed(10)

def up():
	t.setheading(90)
	t.penup()
	t.forward(30)
	t.penup()


def down():
	t.setheading(270)
	t.forward(30)
	t.penup()


def left():
	t.setheading(180)
	t.forward(30)
	t.penup()


def right():
	t.setheading(0)
	t.forward(30)
	t.penup()


window.listen()
window.onkey(up, 'Up')
window.onkey(down, 'Down')
window.onkey(left, 'Left')
window.onkey(right, 'Right')

mainloop()
