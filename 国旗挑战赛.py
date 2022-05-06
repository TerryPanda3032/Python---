'''
Author: TERRY
Date: 2022-02-08 16:24:37
LastEditTime: 2022-02-12 21:24:29
FilePath: \Python系统课\国旗挑战赛.py
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







from cmath import rect
from argon2 import PasswordHasher
from wonderLang import *



# Todo 任务 一
# 实现函数, 画一个正多边形, 参数如下
# x y 是起点, 设起点为多边形的顶部边的左顶点
# sides 是多边形的边数
# length 是边长
# 函数定义如下：
# polygon(x, y, sides, length)
'''
description: 
param {*} x
param {*} y
param {*} sides
param {*} length
return {*}
'''
def polygon(x, y, sides, length):
    jump(x, y)
    angle = 180 - ((sides - 2) * 180 / sides)
    for i in range(sides):
        forward(length)
        right(angle)
        pass
    pass


# 提示：
# 这一次的参数中没有右转的角度了，
# 右转的角度可以通过下面的公式计算获得：
#   angle = 180 - ((sides - 2) * 180 / sides)
#   其中 * 代表乘法 / 代表除法

# 1，正方形和正多边形的区别是前者循环 4 次，多边形循环 sides 次


# Todo 任务 二
# 实现一个圆形函数
# x y 是圆形的圆心
# r 是半径
# 函数定义如下：
# circle(x, y, r)

'''
description: 
param {*} x
param {*} y
param {*} r
return {*}
'''
def circle(x, y, r):
    jump(x,y)
    
    polygon(x,y+r,100,2*3.14*r/100)
    pass
# circle(0,0,30)

# 我们画过了 100 边形，发现 100 边形就是圆形，
# 电脑中的圆全部都是通过多边形来模拟的
# 这一次的圆初始点在圆心，所以需要移动到左上角开始画起

# 提示：
# 1，我们用 36 边形来模拟圆形，sides 的取值应该是 36
# 2，下面计算出多边形的边长
#   圆的周长 2 * math.pi * r
#   边长 length = 周长 / sides
# 3，先看这副图，一开始箭头朝向右边，左转一个如下角度：
#   left_angle = (90 + (360 / sides) / 2)
# 4，转完之后就移动 r
# 5，到了左上角了，再转回来，right(left_angle)
# 6，使用 polygon 函数来画一个 36 边形就好啦


# Todo 任务 三
# 实现一个矩形函数
# x y 是矩形中心的坐标
# w h 是宽高
# https://static.wonderland.run/cmw/rect.png
# center_rect(x, y, w, h)

'''
description: 
param [none] x
param [none] y
param [none] w
param [none] h
return [none]
'''
def center_rect(x, y, w, h):
    jump(x,y)
    jump(x-0.5*w,y+0.5*h)
    for i in range(2):
        forward(w)
        right(90)
        forward(h)
        right(90)
        pass
    pass
# center_rect(10,10,50,20)
# 提示:
#     前面已经实现过了 rect 函数，
#     不过 rect 函数中的 x, y 是表示左上角坐标,
#     现在需要实现的 center_rect 函数的 x, y 是矩形中心的坐标,
#     所以应该先从矩形中心移动到矩形左上角, 然后调用 rect 函数

# 1，根据矩形中心坐标 x y 计算出左上角坐标 x1, y1
# 2，调用 rect 函数，传入的参数分别为左上角的坐标，宽和高


# Todo 任务 四
# 注意, 作业中提到的国旗的颜色我们只画黑色线框展示不填色
# 作业 4
# 实现一个函数画日本国旗
# 调用 2 个函数画日本国旗

# 一个画背景的白色矩形，宽高 300 * 200
# 一个画中间的圆，圆的直径必须为国旗高的 3/5
# x, y 是国旗中心点
# japan(x, y)
'''
description: 
param [none] x
param [none] y
return [none]
'''
def japan(x, y):
    jump(x, y)
    turtle.color('green')
    turtle.begin_fill()
    circle(x, y,60)
    turtle.end_fill()
    center_rect(x, y,300,200)
japan(0,0)

# 1, 使用 center_rect 来画矩形
# 2，使用 circle 来画圆


# Todo 任务 五
# 实现一个五角星函数
# x y 是五角星的中心点坐标
# r 是五角星外接圆的半径
# center_star(x, y, r)

# 为了实现这个函数, 你需要使用三角函数计算五角星左上角的坐标
# 注意这个数学过程不需要你理解，只需要按照要求来写代码

# 下面是需要用的函数
'''
description: 
param [none] degree
return [none]
'''
def sin(degree):
    import math
    # 如上课所述, 数学库里面的 sin 函数接受弧度作为参数
    # 我们这个函数接受角度, 下面是弧度转角度的公式
    radians = degree * math.pi / 180
    return math.sin(radians)


def cos(degree):
    import math
    radians = degree * math.pi / 180
    return math.cos(radians)

def star(x,y,width,angle):
    jump(x,y)
    for i in range(5):
        forward(width)
        right(angle)
        pass
    pass
# star(0,0,100,144)
# 提示, 如图
# https://static.wonderland.run/cmw/center_star.jpeg
#     1. 正五角星顶角的一半是 18 度, angle = 18, 外接圆半径为 r
#     2. 五角星顶部横边 BE 的左边点 B 的 x 坐标为 x1 = x - cos(angle) * r   这里 x1 坐标计算已经写好了直接用
#     3. 五角星顶部横边 BE 的左边点 B 的 y 坐标为 y1 = y + sin(angle) * r   这里 y1 坐标计算已经写好了直接用
#     4. 五角星顶部横边的长度为 length = cos(angle) * r * 2
#     5. 调用前面作业写个的 star 函数 (x1, y1, length)


# Todo 任务 六
# 实现一个函数画中国国旗
# 五角星不要求角度朝向（统一用正五角星），国旗宽高 300 * 200
# https://static.wonderland.run/cmw/china.jpg
# x, y 是国旗中心点
# china(x, y)
'''
description: 
param [none] x
param [none] y
param [none] width
param [none] angle
return [none]
'''
def star(x,y,width,angle=144):
    jump(x,y)
    for i in range(5):
        forward(width)
        right(angle)
        pass
def china(x, y):
    jump(x,y)
    center_rect(x,y,300,200)
    star(x-100,y+50,60,144)
    star(x-50,y+10,20,144)
    star(x-50,y+80,20,144)
    star(x-30,y+30,20,144)
    star(x-30,y+60,20,144)
   
# china(0,0)


# 提示:
#     1. 使用 rect 函数画一个矩形
#     2. 计算比例，画 5 个五角星(调用 5 次), 计算好坐标


# Todo 任务 七
# 实现一个函数画法国国旗，长宽 300 * 200
# france(x, y)
# x, y 是国旗中心点坐标
def france(x, y):
    for i in range(3):
        jump(x+i*100,y)
        center_rect(0+i*100,0,100,200)
# france(0,0)       

# 分步提示:
#     1. 计算出三个矩形的宽, 均为 1/3 * w
#     2. 思考一下如何只用 center_rect 函数实现出法国国旗 bingo!!!


# Todo 任务 八
# 实现一个函数画德国国旗，长宽 300 * 200
# germany(x, y)
# x, y 是国旗中心点坐标
def germany(x, y):
    for i in range(3):
        jump(x,y+i*33.3333)
        center_rect(0,0+i*(200/3),300,200/3)
# germany(0,0)
# 分步提示:
#     1. 计算出三个矩形的高, 均为 1/3 * w
#     2. 思考一下如何只用 center_rect 函数实现出德国国旗


# Todo 任务 九
# 实现一个函数冈比亚国旗，长宽 300 * 200
# https://static.wonderland.run/cmw/gambia.png
# gambia(x, y)
def gambia(x, y):
    jump(x,y)
    germany(x,y)
    right(90)
    forward(66.6+8.325)
    right(-90)
    forward(300)
    right(90)
    forward(49.95)
    right(90)
    forward(300)
# gambia(0,0)
# 分步提示:
#     1. 最上面和最下面两个矩形和德国国旗一致
#     2. 中间的矩形分成三个矩形, 高度占比分别为 1:6:1, 分别计算出这三个矩形的中心坐标
#     3. 分别计算中间三个矩形的长度和高度
#     4. 使用 center_rect 画出 5 个矩形, 每次传入的参数不一致


# Todo 任务 十
# 实现一个瑞士国旗，长宽 200 * 200
# switzerland(x, y)
def switzerland(x, y):
    jump(x, y)
    center_rect(x,y,200,200)
    center_rect(x,y,75,25)
    center_rect(x,y,25,75)
# switzerland(0,0)


# 分步提示:
#     1. 瑞士国旗中的两个矩形大小是一样的, 都按照长边 75, 短边 25 来计算
#     2. 思考一下如何只用 center_rect 函数实现出瑞士国旗

def center_star(x,y,r):
    x1=x-cos(18)*r
    y1=y+sin(18)*r
    length=cos(18)*2*r
    star(x1,y1,length,144)
# Todo 任务 十一
# 实现一个函数朝鲜国旗，长宽 300 * 200
# northkorea(x, y)
'''
description: 
param [none] x
param [none] y
return [none]
'''
def northkorea(x, y):
    w=300
    h=200
    center_rect(x,y,w,h)
    w1=300
    h1=h*(17)/(25)
    center_rect(x,y,w1,h1)
    w2=w
    h2=h*15/(25)
    center_rect(x,y,w2,h2)
    r=h2*2/3/2
    circle(x-w/2/5,y,r)
    center_star(x-w/2/5,y,r)

   
#northkorea(0,0)
# 提示:
#     朝鲜国旗从上往下依次为蓝色矩形、白色矩形、红色矩形、白色矩形和蓝色矩形,
#     这些矩形的高度比分别为 4:1:15:1:4, 红色矩形里包含了一个圆形和一个五角星
#     圆形的直径和红色矩形的高度的比为 2:3, 圆形的圆点 x 坐标距离国旗中心点坐标左边 1/5 处
#     使用这些数据计算出各个图形的坐标, 然后画出来



pause()

