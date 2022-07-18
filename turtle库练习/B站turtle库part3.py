#B站part3
import turtle
p = turtle.Turtle()
turtle.colormode(255)
#更改背景色
turtle.bgcolor(100,200,100)
#弧度 第一个参数表示半径，第二个参数表示弧度
#p.circle(40,90)
#内接多边形 第一个参数表示半径，第三个参数表示边
#关键字参数
#p.circle(60,steps=10)
#对图形进行上色
p.fillcolor("blue")
#开始上色
p.begin_fill()
p.circle(60)
#结束上色
p.end_fill()
turtle.done()
