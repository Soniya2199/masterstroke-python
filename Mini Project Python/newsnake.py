import turtle as tl
import random as r
import time

#!! Main Screen 
screen = tl.Screen()
screen.title("Snake Game")
screen.bgcolor("#388004")
screen.setup(width=600, height=600)
screen.tracer(0)

speed=10

#! Snake head
snake = tl.Turtle() #? created turtle obj
snake.shape("classic")
snake.color("#071e91")
snake.shapesize(1.5)
snake.speed(0)
snake.penup()
snake.direction='stop'

food =tl.Turtle()
shapes=r.choice(['circle','arrow','turtle','triangle','square'])
food.shape(shapes)
colors=r.choice(['#decd10','#c95555','#09e3a5','#b267eb','#450606','#e08a2d','#2de0b9'])
food.color(colors)
food.shapesize(0.7)
food.penup()
food.goto(0,100)

#! snake movements function
def up():
	if snake.direction=='up':
		y=snake.ycor()
		snake.sety(y+10)
	
def down():
	if snake.direction=='down':
		y=snake.ycor()
		snake.sety(y-10)

def left():
	if snake.direction=='left':
		y=snake.ycor()
		snake.sety(y+10)

def right():
	if snake.direction=='right':
		y=snake.ycor()
		snake.sety(y-10)

def key_Move():
	if snake.direction!=up:
		snake.direction=down
	if snake.direction!=down:
		snake.direction=up
	if snake.direction!=right:
		snake.direction=left
	if snake.direction!=left:
		snake.direction=right


#! key press movements	
screen.listen()
screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')

while True:
	
	snake.forward(speed)
	screen.update()

	if snake.distance(food)<20:
		x=r.randint(-600,600)
		y=r.randint(-300,300)
		food.goto(x,y)
	key_Move()
	
	time.sleep(1)




screen.mainloop()