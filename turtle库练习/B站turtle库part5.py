import turtle
import random

p = turtle.Turtle()
turtle.colormode(255)
p.speed(0)
def circle(radious):
    if radious > 100:
        return
    p.circle(radious)
    p.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    p.left(5)
    circle(radious + 1)
circle(50)
turtle.done()
