#B站part2课后练习
import turtle
import random
p = turtle.Turtle()

turtle.colormode(255)
p.pensize(2)
p.speed(100)
for i in range(100):
    p.color(random.randint(100,255),random.randint(100,255),random.randint(100,255))
    p.left(10)
    p.circle(5*i*0.5)
turtle.done()