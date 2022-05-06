'''
Author: TERRY
Date: 2022-02-17 20:38:49
LastEditors: TERRY
LastEditTime: 2022-02-17 21:12:41
FilePath: \Python系统课\学生判断器.py
Description: 
'''
# put       放
# input     输入
# output    输出



# iphone 锁屏密码
# 1234
# ==
# string 字符串   int 变成一个整数
print('请输入密码')
while True:
    password=input()
    password=int(password)
    if password==1234:
        print('bingo')
        break
    else:
        print('please try again')