"""
Author: TERRY
Date: 2022-04-17 21:29:00
LastEditors: TERRY
LastEditTime: 2022-04-29 10:37:59
FilePath: \Python系统课\自制图形库.py
Description: 
"""
# 依旧需要使用 wonderLang 里面的函数，这样更高效
from turtle import color
from cv2 import edgePreservingFilter
from wonderLang import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import cm

# ----------
#  1, 实现 Excel
#  2, 自制可视化数据库

# Todo 1
# 根据本周天气，绘制柱状图
# 柱状图类似如下：
# https://static.wonderland.run/src/chart.png

# 中国本周的每日平均气温, 从周一到周日, 就在下面的 list 中
# 函数参数 temps
# temps 是温度 temperatures 的缩写，是一个温度列表，也就是矩形的高

# 分步提示：
#     1. 遍历数组 temps，每一个温度都画一个矩形。矩形之间的间隔为 0。


# def forecast1(temps):
#     x=np.array([1,2,3,4,5,6,7])
#     y=np.array(temps)

#     plt.bar(x,y,width=1,color='#ffffff',edgecolor="#dc1f0d")
#     plt.show()

# temps = [-22, 19, 22, 21, 25, 27, 30]

# forecast1(temps)


# Todo 2
# 根据本周天气，绘制柱状图
# 柱状图类似如下：
# https://static.wonderland.run/src/chart2.png
# 中国本周的每日平均气温, 从周一到周日
# 函数参数 temps space
# temps 是温度 temperatures 的缩写，是一个温度列表
# space 是温度矩形之间的间距

# 分步提示：
#     1. 在 todo1 的基础上加上一个 space 参数，矩形之间的间距通过 space 参数传递。


# def forecast2(temps, space):
#     x=np.array([1,2,3,4,5,6,7])
#     y=np.array(temps)
#     plt.bar(x,y,width=space,color='#ffffff',edgecolor="#dc1f0d")
#     plt.show()
#     pass


# temps 如下，你也可以写自己的温度列表
# temps = [22, 19, 22, 21, 25, 27, 30]
# forecast2(temps, 0.5)


# Todo 3
# 根据本周天气，绘制柱状图
# 柱状图类似如下：
# https://static.wonderland.run/src/chart2.png一样的就是变高而已)
# 中国本周的每日平均气温, 从周一到周日
# 函数参数 temps space base
# temps 是温度 temperatures 的缩写，是一个温度列表
# space 是温度矩形之间的间距
# base 是温度矩形高加上的值，这样能更好的区分不同的温度。

# 分步提示：
#     1. 在 todo2 的基础上加上一个 base 参数，每个计算出来的温度都增加 base，然后画矩形图


# def forecast(temps, space, base):
#     x=np.array([1,2,3,4,5,6,7])
#     for i in range(7):
#         temps[i]=temps[i]+base
#     y=np.array(temps)
#     plt.bar(x,y,width=space,color='#ffffff',edgecolor="#dc1f0d")
#     plt.show()

# forecast([324,234,22,34,-1234,4,456],space=0.5,base=100)

# temps 如下，你也可以写自己的温度列表
# temps = [22, 19, 22, 21, 25, 27, 30]
# forecast(temps, 20, 4)

# Todo 4
# 根据本周天气，绘制柱状图
# 柱状图类似如下：

# 加入这次的温度中有零下的温度，这该怎么办？你的函数能实现表示零下温度吗？
# temps = [-22, 19, 22, -1, -25, 27, 30]
#
# forecast(temps, 20, 4)
# def forecast(temps, space, base):
#     x=np.array([1,2,3,4,5,6,7])
#     for i in range(7):
#         temps[i]=temps[i]+base
#     y=np.array(temps)
#     plt.bar(x,y,width=space,color='#ffffff',edgecolor="#dc1f0d")
#     plt.show()
#     pass

# Todo 5 绘制坐标轴

# 分步提示：
#     1. 在原点处往左移动到左边边缘，然后前进画布宽度的距离，这样就可以画出 x 轴
#     2. 以同样的方式画出 y 轴，注意向下为 y 轴正方向
#     3. 然后在坐标轴上画出天气预报的柱状图

# def coordinate_axis(temps, space, base):
#     x=np.array([1,2,3,4,5,6,7])
#     for i in range(7):
#         temps[i]=temps[i]+base
#     y=np.array(temps)
#     plt.bar(x,y,width=space,color='#ffffff',edgecolor="#dc1f0d")
#     plt.show()
#     pass
#     pass


# coordinate_axis()
#

# forecast(temps, 20, 4)

# Todo 6 结合坐标系你就做出来自己的 Excel, 可视化数据库
def main():
    temps = [22, -19, 22, 30, -25, 27, 30]
    high = np.array([2, 5])
    x = np.array([1, 2, 3, 4, 5, 6, 7])
    plt.subplot(1, 2, 1)
    plt.bar(x, temps, color="#487e02")
    plt.plot(x, temps, color="#de1f0d")
    plt.title("temperture")
    plt.subplot(1, 2, 2)
    plt.pie(high)
    plt.title("cold&hot")
    plt.show()


main()
