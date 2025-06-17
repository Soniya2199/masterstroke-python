import turtle
import time
import random

# Setup screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turns off screen updates for smooth movement

# Snake initial setup
snake = []
for i in range(3):
    segment = turtle.Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(-20 * i, 0)
    snake.append(segment)
    

# Food setup
food = turtle.Turtle("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Score setup
score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

# Snake movement
direction = "stop"

def move():
    if direction != "stop":
        for i in range(len(snake) - 1, 0, -1):
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

# Change direction functions
def go_up():
    global direction
    if direction != "down":
        direction = "up"

def go_down():
    global direction
    if direction != "up":
        direction = "down"

def go_left():
    global direction
    if direction != "right":
        direction = "left"

def go_right():
    global direction
    if direction != "left":
        direction = "right"

# Keyboard bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Game loop
game_running = True

while game_running:
    screen.update()
    move()
    
    # Check collision with food
    if snake[0].distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))  # Move food
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        snake.append(new_segment)
        score += 10
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

    # Check collision with walls
    if (snake[0].xcor() > 290 or snake[0].xcor() < -290 or
        snake[0].ycor() > 290 or snake[0].ycor() < -290):

        game_running = False
        score_display.goto(0, 0)
        score_display.write("Game Over!", align="center", font=("Arial", 20, "bold"))

    # Check collision with itself
    for segment in snake[1:]:
        if snake[0].distance(segment) < 10:
            game_running = False
            score_display.goto(0, 0)
            score_display.write("Game Over!", align="center", font=("Arial", 20, "bold"))

    time.sleep(0.1)

screen.mainloop()



# # import packages 
# import turtle 
# import random 

# # global colors 
# col = ['red', 'yellow', 'green', 'blue', 
# 	'white', 'black', 'orange', 'pink'] 

# # method to call on screen click 


# def fxn(x, y): 
# 	global col 
# 	ind = random.randint(0, 7) 
	
# 	# set screen color randomly 
# 	sc.bgcolor(col[ind]) 

# # set screen 
# sc = turtle.Screen() 
# sc.setup(400, 300) 

# # call method on screen click 
# turtle.onscreenclick(fxn)
# sc.mainloop()
#*******************************************************************************************

# screen = turtle.Screen()
# screen.title("Snake Game")
# screen.bgcolor("#388004")
# screen.setup(width=600, height=600)
# snake = turtle.Turtle() #? created turtle obj
# snake.shape("triangle")
# snake.color("red")
# snake.penup()

# snake.sety(120)
# snake.setx(50)

# turtle.done()