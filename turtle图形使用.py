'''
Author: TERRY
Date: 2022-02-12 21:29:13
LastEditors: TERRY
LastEditTime: 2022-02-15 21:18:16
FilePath: \Python系统课\turtle图形使用.py
Description: 
'''
'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  - /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           佛祖保佑       永不宕机     永无BUG
'''



'''
Author: TERRY
Date: 2022-02-12 21:29:13
LastEditors: TERRY
LastEditTime: 2022-02-13 18:28:34
FilePath: \Python系统课\turtle图形使用.py
Description: 
'''

# 请导入 turtle 这个库
import turtle

"""
多行字符串

库 turtle
函数的集合

在使用任何库之前一定要去导入

turtle (0, 0)
圆的直径和半径
"""

# dot 点
# 第一个参数：直径
# 第二个参数，可有可无，颜色
# turtle.dot(30, 'red')

# circle 圆
# 第一个参数：半径
# 第二个参数：可有可无，角度
# 可指定参数 steps
# 注意：circle 是从圆的底部画起的



# 任务零
# x y 是圆形的中心点坐标
# r 是圆的半径
'''
description: 
param [none] x
param [none] y
return [none]
'''
def jump(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
'''
description: 
param [none] x
param [none] y
param [none] r
return [none]
'''
def circle(x, y, r):
    jump(x,y)
    turtle.circle(r,steps=100)

    pass
#circle(0,0,100)


"""
这是一个多行字符串

任务一：

绘制一个如下图形，一个正方形，内部有三个红点，中间红点在正方形中心。

图形如下：
https://static.wonderland.run/src/todo1.png

1，正方形边长为 200，线条为黑色
2，圆点的直径均为 20， 填充颜色为红色，画完后请隐藏画笔
3，中间圆点的圆心位置为画布的正中心，三个圆心之间的距离相隔为 40

提示圆点使用 turtle.dot(直径，颜色)
"""
'''
description: 
param [none]
return [none]
'''
def rect():
    for i in range(4):
        turtle.forward(200)
        turtle.right(90)
        pass
    pass
# rect()
# jump(100,-100)
# turtle.dot(20,'red')
# jump(140,-100)
# turtle.dot(20,'red')
# jump(60,-100)
# turtle.dot(20,'red')
# turtle.hideturtle()


"""
任务二：
注释使用

写一个计算长方形面积的程序，并对每行代码进行相应的注释，要求如下:

1, 使用多行注释，说明程序的功能：
计算长方形的面积
并输出结果

2, 设置第1个变量：
用“a”表示长方形的长，并赋值为6；使用单行注释说明程序的功能；
   
3, 设置第2个变量：
用“b”表示长方形的宽，并赋值为3；使用单行注释说明程序的功能；
  
4, 设置第3个变量：
用“s”表示长方形的面积，并体现运算公式，使用单行注释说明程序功能；
  
5, 输出长方形的面积，运行结果格式为：“长方形的面积为：”并使用单行注释说明程序功能。  
(提示使用 print/log 输出结果)

"""

def main():
    a=6#长方形长
    b=3#长方形宽
    s=6*3#长方形面积
    s=str(s)
    print('长方形的面积为'+s)#输出长方形的面积
main()


"""
任务三：

画出下面示意图形，要求如下：

https://static.wonderland.run/src/todo2.png

1， 画出如下的图形，注：直线部分是由两个步长为200的线段垂直相交组成，

2，圆的直径为200；
    图形的中心位置为画布中心；
    画笔宽度为2，颜色为红色。

# """
# turtle.pensize(2)
# jump(0,0)
# turtle.color('red')
# circle(0,-100,100)
# jump(0,0)
# turtle.left(90)
# turtle.forward(100)
# turtle.right(180)
# turtle.forward(200)
# jump(0,0)
# turtle.left(90)
# turtle.forward(100)
# turtle.right(180)
# turtle.forward(200)
# turtle.hideturtle()







"""
任务四：

画出下面示意图形，要求如下：
https://static.wonderland.run/src/todo3.png

美国队长盾牌

1，中间的五角星使用我们的 center_star 

2，三个圆形的直径分别为 240, 280, 340, 400 

记得填上颜色
"""
def sin(degree):
    import math
    radians = degree * math.pi / 180
    return math.sin(radians)

def star(x,y,width,angle=144):
    jump(x,y)
    for i in range(5):
        turtle.forward(width)
        turtle.right(angle)
        pass
def cos(degree):
    import math
    radians = degree * math.pi / 180
    return math.cos(radians)
def center_star(x,y,r):
    x1=x-cos(18)*r
    y1=y+sin(18)*r
    length=cos(18)*2*r
    star(x1,y1,length,144)





turtle.color('red')
turtle.begin_fill()
circle(0,-200,200)
turtle.end_fill()

turtle.color('white')
turtle.begin_fill()
circle(0,-170,170)
turtle.end_fill()

turtle.color('red')
turtle.begin_fill()
circle(0,-140,140)
turtle.end_fill()

turtle.color('blue')
turtle.begin_fill()
circle(0,-120,120)
turtle.end_fill()

turtle.color('white')
turtle.begin_fill()
center_star(0,0,120)
turtle.end_fill()
turtle.hideturtle()


turtle.done()













