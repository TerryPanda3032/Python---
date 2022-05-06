# 导入 wonderLang 中的全部内容
from wonderLang import *

# 复制粘贴
# 我找到了其中最重要的东西
# 而忽略了那些重复的东西

# 函数
# 所有的代码全部都是函数
# 函数他就是编程的基石

# 例子 1
# 画两个边长为 99 像素三角形
# 他们之间间隔 30
# 提示, 往右旋转 120 度


# 例子 2
# 画两个边长为 80 像素三角形
# 他们之间间隔 30
# 提示, 往右旋转 120 度


# 例子 3
# 画两个边长为 101 的正方形
# 他们之间间隔 200
# 提示, 往右旋转 90 度

# 例子 4
# 画两个边长为 77 的正方形
# 他们之间间隔 100
# 提示, 往右旋转 90 度


# --------
# 任务
# --------


# 任务 1
# 画两个边长为 120 像素三角形
# 他们之间间隔 44
# 提示, 往右旋转 120 度
def draw(side,angle,width):
    for i in range(side):
        forward(width)
        right(angle)
# draw(3,120,120)
# forward(44)
# draw(3,120,120)

# # 任务 2
# 画两个边长为 80 的正方形
# 他们之间间隔 30
# 提示, 往右旋转 90 度
# for i in range(2):
#     draw(4,90,80)
#     forward(30)


# 任务 3
# 画两个边长为 101 的五角星，
# 如图：
# https://static.wonderland.run/cmw/star.jpg
# 他们之间间隔 30
# 提示, 往右旋转 144 度
# 函数定义 star()
def star(width,angle):
    for i in range(5):
        forward(width)
        right(angle)
        pass
# star(101,144)
# jump(0+30,0)
# star(101,144)


# 任务 4
# 画两个边长为 54 的五角星，
# 如图：
# https://static.wonderland.run/cmw/star.jpg
# 他们之间间隔 15
# 提示, 往右旋转 144 度
# star(54,144)
# forward(15)
# star(54,144)


# 任务 5
# 画两个边长为 88 的五角星，
# 如图：
# https://static.wonderland.run/cmw/star.jpg
# 他们之间间隔 115
# 提示, 往右旋转 144 度
# star(88,144)
# forward(115)
# star(88,144)

# 任务 6
# 画一个房子
# 所有边的长度都是 100
# 如图：
# https://static.wonderland.run/cmw/house.png
# 提示：右转是 right(90) 那 right(-90) 是往哪里转
def house():
    draw(4,90,100)
    draw(3,-120,100)

# 任务 7
# 画两个房子
# 所有边的长度都是 100
# 如图：
# https://static.wonderland.run/cmw/house.png
# 提示：右转是 right(90) 那 right(-90) 是往哪里转
# 函数定义 house()

house()
forward(100)
house()



# ！！！ 不要删除或者注释
# pause 这行代码让窗口不消失
pause()