'''
Author: TERRY
Date: 2022-02-17 21:37:50
LastEditors: TERRY
LastEditTime: 2022-03-01 21:51:00
FilePath: \Python系统课\阶段练习三.py
Description: 
'''
# '''
# Author: TERRY
# Date: 2022-02-17 21:37:50
# LastEditors: TERRY
# LastEditTime: 2022-02-24 21:29:57
# FilePath: \Python系统课\阶段练习三.py
# Description: 
# '''
# # 练习 turtle
import turtle
import math
# # Todo 1
# # 画出一个正方形（边长100）
def jump(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
def rect(x, y,w,h,centre,pen='black',color='white'):
    if centre==0:
        jump(x,y)
        turtle.color(pen,color)
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(w)
            turtle.right(90)
            turtle.forward(h)
            turtle.right(90)
        turtle.end_fill()
        pass
    if centre==1:
        jump(x,y)
        jump(x-0.5*w,y+0.5*h)
        turtle.color(pen,color)
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(w)
            turtle.right(90)
            turtle.forward(h)
            turtle.right(90)
        turtle.end_fill()


# # 画出一个正方形（边长100）
# # 正方形的中心是画布原点(0, 0)
# rect(0,0,100,100,1)

# # Todo 3
# # 画出一个长方形（长50，宽30）
# rect(0,0,50,30,0)

# # Todo 4
# # 画出一个长方形（长50，宽30）
# # 长方形的中心是画布原点(0, 0)
# rect(0,0,50,30,1)

# # Todo 5
# # 画出一个正方形（边长100，红色填充）
# rect(0,0,100,100,1,'red','red')

# # Todo 6
# # 画出一个长方形（长70，宽30，蓝色填充）
# rect(0,0,70,30,0,'blue','blue')

# Todo 7
# 画出一个圆（半径50）
def circle(x, y, r):
    jump(x,y-r)
    turtle.circle(r,steps=100)

    pass
# circle(0,0,50)

# Todo 8
# 画出一个圆（直径50，绿色填充）
# turtle.pencolor('green')
# turtle.color('green')
# turtle.begin_fill()
# circle(0,0,25)
# turtle.end_fill()

# Todo 9
# 画出一个半圆（直径30，蓝色填充）
# turtle.pencolor('blue')
# turtle.color('blue')
# turtle.begin_fill()
# circle(0,0,15)
# turtle.end_fill()
# rect(-14,0,35,40,0,'white','white')


# Todo 10
# 在正方形（边长100）的正中心，画一个圆（半径30）
# 正方形的中心点是原点 (0, 0)
# rect(0,0,100,100,1)
# circle(0,0,30)
# Todo 11
# 画一个点，直径为 30，红色填充
turtle.color('red')
turtle.begin_fill()
circle(0,0,15)
turtle.end_fill()
# Todo 12
# 画一个点，半径为 30，蓝色填充
turtle.color('blue')
turtle.begin_fill()
circle(0,0,30)
turtle.end_fill()


print('hello, world')
print('hello', 'world')
turtle.done()