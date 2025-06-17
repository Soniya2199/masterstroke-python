import turtle
import colorsys

def draw_heart(x, y, size, color):
    """Draws a heart at (x, y) with given size and color."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    
    turtle.left(140)
    turtle.forward(180 * size)
    turtle.circle(-90 * size, 200)
    turtle.left(120)
    turtle.circle(-90 * size, 200)
    turtle.forward(180 * size)
    
    turtle.end_fill()
    turtle.right(40)  # Reset angle

# Setup turtle
turtle.speed(3)
turtle.bgcolor("black")

# Draw big red heart
draw_heart(-100, 0, 1, "red")

# Generate gradient color for the small heart
hue = 0.6  # Adjust hue (0 to 1)
r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)  # Convert HSV to RGB

# Draw small heart with gradient color
turtle.setheading(0)  # Reset angle
draw_heart(100, -50, 0.6, (r, g, b))

# Write name inside the big heart
turtle.penup()
turtle.goto(-50, -20)
turtle.color("white")
turtle.pendown()
turtle.write("Aravindhan", font=("Arial", 20, "bold"))

# Hide turtle and display window
turtle.hideturtle()
turtle.done()