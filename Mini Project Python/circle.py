import turtle as tl


tl.Screen()
tl.color('#989077')
tl.bgcolor("pink")
tl.width(5)
x=-150
for i in range(7):
    tl.penup()
    tl.goto(x,0)
    tl.pendown()
    tl.circle(45)
    x+=50
tl.mainloop()
