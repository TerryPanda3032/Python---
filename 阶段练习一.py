
from operator import length_hint

from wonderLang import *

"""
注意
1. 你的时间非常宝贵，所以遇到不清楚的地方就马上来问。
    按照提问规则提问
    
2. 作业有提示，如果几分钟都想不出来就看提示
    提示其实是作业的拆分。
    不要觉得看提示不好，先做出来最重要。
"""


# ----------------------
# 这个函数的作用是把三角箭头光标移动到 x y 坐标处（只移动光标不画线）


# 例子 1
# 实现函数, 用于画一个边长 100 的正方形
# 参数 x, y 是正方形左上角坐标
# 在任意位置可以画出函数


# Todo 1  OK
# 实现函数, 用于画一个正方形, 边长由参数提供
# 参数 x, y 是正方形左上角坐标
# 参数 l(注意，这里是字母 l，不是数字 1) 是正方行边长
# 函数声明如下
# square(x, y, l)
# def square(x, y, length):
#     jump(x, y)
#     for i in range(4):
#         forward(length)
#         right(90)
# square(0,0,30)
# 提示:
# 复制 Example 1 中的例子进行修改

# 分步提示:
# 1. 在例子 1 的基础上再增加一个参数 l （这个是字母 l，不是数字 1）
# 2. forward 的参数换成 l


# Todo 2
# 实现函数, 用于画一个矩形, 长宽由参数提供
# 参数 x, y 是左上角坐标
# 参数 w, h 是长宽
# 函数声明如下
# rect(x, y, w, h)
# def  rect( x,y,w, h):
#     jump(x,y)
#     for i in range(2):
#         forward(w)
#         right(90)
#         forward(h)
#         right(90)
#         pass
# rect(0,0,30,20)

# 提示:
# 根据例子 1 的程序修改

# 分步提示:
# 1. 考虑矩形只重复两次(一次会画出长和宽), 所以只需要循环 2 次


# Todo 3
# 画一排正方形, 一共 5 个
# 从 0 0 点开始, 边长为 30, 正方形之间间隔为 0
# 函数声明如下
# square5()
# square(0+30,0,30)
# square(60,0,30) 
# square(90,0,30)
# square(120,0,30)
# square(150,0,30)
# 提示:
# 根据资料中的循环例子, 计算每个正方形的坐标
#
# 分步提示:
# 1. 要画出 5 个正方形, 表明循环 5 次
# 2. 计算每次循环的正方形左上角坐标 x, y
# 3. 在每次循环中画正方形, 调用作业 1 中实现的函数


# Todo 4
# 画一排正方形, 一共 5 个
# 从 0 0 点开始, 边长为 30, 正方形之间间隔为 10 像素
# 函数声明如下
# square5_10()
# def square5_10():
#     an=0
#     for i in range(5):
#         x1=-40+40*an
#         square(x1,0,30)
#         an+=1
#         pass
# square5_10()
# 提示:
# 作业 4 和作业 3 的不同之处在于每个正方形的左上角坐标不同, 计算出每个左上角的坐标之后,
# 参考作业 3 的提示



# Todo 5
# 实现函数, 画一排正方形, 有如下参数
# x, y 是第一个正方形左上角坐标
# n 是正方形的个数
# space 是两个正方形之间的间距
# len 是正方形的边长
# square_line(x, y, n, space, len)

# 提示:
# 作业 4 中画 5 个正方形, 循环 5 次
# 作业 5 中画 n 个正方形, 循环 n 次, 同时两个正方形的间距从 10 换成了 space
# def square_line(x, y, n, space, len):
#     jump(x,y)
#     for i in range(n):
#         for i in range(4):
#             forward(len)
#             right(90)
#         forward(space)
#     pass
# square_line(0,0,10,60,40)
# Todo 6
# 实现函数, 用上题的函数来画一个正方形方阵, 参数如下
# x, y 是第一个正方形左上角坐标
# space 是两个正方形之间的间距
# len 是正方形的边长
# n 是横向正方形的个数
# m 是纵向正方形的个数
# square_square(x, y, space, len, n, m)
# def  rect( w, h):
#     #jump(x,y)
#     for i in range(2):
#         forward(w)
#         right(90)
#         forward(h)
#         right(90)
#         pass
# def rect_pro(x, y, space, len,n,m):
#     jump(x,y)
#     for i in range(n):
#         rect(len,len)
#         forward(space)
#         pass
#     jump(x,y)
#     for i in range(m):
#         rect(len,len)
#         right(-270)
#         forward(space)
#         right(-90)
# rect_pro(0,0,20,10,5,20)

# 提示:
# m 是纵向正方形的个数, 所以需要循环 m 次,
# 每次循环画一排正方形, 即作业 5 的要求, 所以每次循环调用作业 5 的 square_line 函数就行


pause()

