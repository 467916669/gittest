import turtle
import random
p = turtle.Turtle()
p.speed(20)
turtle.colormode(255)
turtle.setup(1000, 700)
turtle.bgpic("2.png")
# 画单个星星
def star():
    a = [3, 5, 7, 9, 11]
    # 随机选择几角星
    s = random.choice(a)
    s_len = random.randint(20, 40)
    r_cl = random.randint(0, 255)
    g_cl = random.randint(0, 255)
    b_cl = random.randint(0, 255)
    p.fillcolor(r_cl, g_cl, b_cl)
    # 填充颜色
    p.begin_fill()
    for i in range(s):
        p.forward(s_len)
        p.left(180 - 180 / s)
    p.end_fill()
# 更新画笔位置
def penlocation():
    x_loc = random.randint(-500, 500)
    y_loc = random.randint(-350, 350)
    p.penup()
    p.goto(x_loc, y_loc)
    p.pendown()
for i in range(20):
    star()
    penlocation()
turtle.done()
