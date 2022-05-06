'''
Author: TERRY
Date: 2022-02-17 21:37:53
LastEditors: TERRY
LastEditTime: 2022-03-14 20:05:58
FilePath: \Python系统课\阶段练习四.py
Description: 
'''
# Todo 1
# 画一个数字 8
# 数字 8 由上下两个圆构成，一个直径为 30，一个直径为 40。
# 两个圆相交的中心是 (0, 0)
import turtle as tt
tt.speed(0)
def jump(x,y):
    tt.penup()
    tt.goto(x,y)
    tt.pendown()
def circle(x, y, r,degree):
    jump(x,y-r)
    tt.circle(r,degree,steps=50)
    pass
# circle(0,15,15)
# circle(0,-20,20)
# Todo 2
# 画一个圆，圆是空心的
# 这个圆每 1/4 的边都是一个不同的颜色：红，黄，蓝，绿
# 圆的直径为 100
# 圆的中心为 (0, 0)
tt.color('red')
tt.begin_fill
tt.circle(50,90)
tt.end_fill()

tt.color('yellow')
tt.begin_fill
tt.circle(50,90)
tt.end_fill()

tt.color('blue')
tt.begin_fill
tt.circle(50,90)
tt.end_fill()

tt.color('green')
tt.begin_fill
tt.circle(50,90)
tt.end_fill()
# Todo 3
# 画出一个奥迪车标
# 只需要实现是个圆圈交叉在一起就好，不需要考虑坐标
# 圆圈的直径为 60
# 圆圈与圆圈之间圆心的距离为 40
# 画笔的粗心为 5
# circle(0,0,30,360)
# circle(40,0,30,360)
# circle(80,0,30,360)
# circle(120,0,30,360)
# Todo 4
# 制作一个阿基米德螺旋线
# 如图所示:
# https://static.wonderland.run/src/todo4.png
# 最里面的半圆的直径为 20
# 后面的每一个半圆的直径都是上一个的一倍
# 画笔的粗心为 4
# tt.pensize(4)
# def draw_spiral(n, w,a=0.05):
#     r = 0
#     b = 0.1
#     c = 0 
#     for i in range(n):
#         r = a*c + b        
#         tt.circle(r, 1)
#         c =c+ w
# draw_spiral(1000, 6)
tt.done()