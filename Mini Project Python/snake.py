import turtle
from turtle import *
import random

#!! Main Screen 
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("#388004")
screen.setup(width=600, height=600)

#! Snake head
snake = turtle.Turtle() #? created turtle obj
snake.shape("triangle")
snake.color("red")
snake.penup()

#! Food 
class Food(turtle.Turtle):
    def _init_(self):
        super()._init_()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.refresh()
    
    def refresh(self):
        """Move the food to a new random location."""
        x = random.randint(-280, 280)  # Within screen bounds
        y = random.randint(-280, 280)
        self.goto(x, y)

food = Food()

# Move the snake (dummy movement for testing food generation)
def move():
    snake.forward(20)
    screen.ontimer(move, 200)

# Collision detection with food
def check_collision():
    if snake.distance(food) < 15:
        food.refresh()  # Generate food at a new position

    screen.ontimer(check_collision, 100)

# Start movement and collision check
move()
check_collision()

# Keep window open
screen.mainloop()