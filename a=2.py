"""
Author: TERRY
Date: 2022-03-18 20:39:13
LastEditors: TERRY
LastEditTime: 2022-05-28 10:47:17
FilePath: \python---\a=2.py
Description: 
"""
import turtle

import turtle

turtle.color("purple")
length = 30
i = 1
while i <= 10:
    turtle.forward(length)
    turtle.left(120)
    length = length + 20
    i = i + 1
    if i % 3 == 0:
        turtle.color("blue")
    elif i % 5 == 0:
        turtle.color("green")
    elif i % 7 == 0:
        turtle.color("black")
    else:
        turtle.color("purple")

turtle.done()
