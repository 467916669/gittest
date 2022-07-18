import turtle
import random

p = turtle.Turtle()
p.speed(0)
turtle.colormode(255)


# 画矩形
def retang(len):
    if len > 300:
        return
    p.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 画一个矩形
    p.forward(len)
    p.left(90+1)
    retang(len + 1)


retang(60)
turtle.done()
