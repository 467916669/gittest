import turtle
import random
p = turtle.Turtle()
turtle.colormode(255)
p.speed(0)
r = 0
g = 0
b = 0
# 树干长度
length = 120
pen_size = 14
p.pensize(pen_size)
p.penup()
p.left(90)
p.backward(length)
p.pendown()
p.forward(length)
def draw_tree(l, lv):
    l = l * 3 / 4
    size = p.pensize()
    p.pensize(size * 3 / 4)
    global r, g, b
    r += 1
    g += 2
    b += 3
    p.pencolor(r % 200, g % 200, b % 200)
    # 左边枝干
    p.left(45)
    p.forward(l)
    # 左边枝干的递归
    if lv < 14:
        draw_tree(l, lv + 1)
    p.backward(l)
    p.right(90)
    # 右边枝干
    p.forward(l)
    if lv < 14:
        draw_tree(l, lv + 1)
    p.backward(l)
    p.left(45)
    p.pensize(size)
draw_tree(length, 8)
turtle.done()
