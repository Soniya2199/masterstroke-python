import turtle

def draw_heart(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    
    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-90, 200)
    turtle.left(120)
    turtle.circle(-90, 200)
    turtle.forward(180)
    
    turtle.end_fill()
    turtle.right(40)  # Reset angle

# Setup turtle
turtle.speed(3)
turtle.bgcolor("white")

# Draw first heart
draw_heart(-100, 0, "red")

# Draw second heart slightly overlapping the first
turtle.setheading(0)  # Reset heading
draw_heart(100, 0, "red")

# Write name in the middle
turtle.penup()
turtle.goto(-50, -20)
turtle.color("black")
turtle.pendown()
turtle.write("Aravindhan", font=("Arial", 20, "bold"))

# Hide turtle and display window
turtle.hideturtle()
turtle.done()
