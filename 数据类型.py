'''
Author: TERRY
Date: 2022-02-17 20:38:46
LastEditors: TERRY
LastEditTime: 2022-02-17 20:57:20
FilePath: \Python系统课\数据类型.py
Description: 
'''
# Todo 1 复习数据类型

# 1, 数字类型
# 整数 integer
a = 20
b = 30
# 浮点数 float
c = 3.0

# 只要有了除号就会变成浮点数
d = a - b / b


# 2, 字符串 string
# 带引号的 ' '  " "

# type 类型的意思

# 3, 布尔值
# 布尔类型

# False True


# Todo 2 选择控制
#
# if 可以根据情况选择性执行某些语句
# 例如下方代码
#
# 定义一个变量 grade 代表年级
grade = 10
# 如果(if) grade 小于 7
if grade < 7:
    # 这句 print 只在 grade 小于 7 这个条件满足的情况下会被执行
    print('小学生')


# 选择控制有多种不同的用法
# 只有 if
if 1 < 2:
    print('条件成立!!!')

# (如果) if 带 else(否则)
# if else 必定会执行一个语句


# 多个 if else


# 例子
# 求绝对值
# x=input()
# x=int(x)
# x=abs(x)
# print(x)
# # 判断奇偶
# % 是求模运算符(取余数)
y=input()
y=int(y)
res=y%2
if res==1:
    print('奇数')
if res==0:
    print('偶数')
else:
    pass

