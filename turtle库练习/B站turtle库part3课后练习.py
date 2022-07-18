# 六芒星阵
import turtle
import math
p = turtle.Turtle()
p.pensize(5)
p.color("purple")
p.speed(20)
p.circle(80)
p.circle(80, steps=3)
p.penup()
p.goto(0, 160)
p.pendown()
p.circle(-80, steps=3)
# p.left(60)
# p.forward(80 * math.sqrt(3))
# for i in range(2):
#     p.left(120)
#     p.forward(80 * math.sqrt(3))
turtle.done()
