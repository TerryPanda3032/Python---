'''
Author: TERRY
Date: 2022-03-08 20:57:37
LastEditors: TERRY
LastEditTime: 2022-04-21 20:54:27
FilePath: \Python系统课\列表进阶与for循环.py
Description: 
'''
log = print


# Todo 6 练习 1
# 建一个函数名字为 log_list
# log_list(list)
# 输入一个 list 自动打印出 list 中的所有元素
def log_list(list):
    c=list
    return c
    pass


print(log_list([100, 300, 'nihao']))

# Todo 7 练习 2
# 创建一个函数，这个函数接受一个只含有数字的列表
# 打印出这个列表中的所有偶数

# 步骤拆分：
# 1，遍历列表中的所有元素
# 2，检查每一个元素是否是偶数 (通过求余数(%)来判断是否是偶数)
# 3，如何是偶数，就 log 这个偶数
def log_even(list):
    for i in list:
        temp1=i
        if temp1%2==0:
            log(temp1)
        else:
            pass
        pass
    pass
log(log_even([100, 300, 700, 4, 3]))


# Todo 8 练习 3
# 创建一个函数，这个函数接受一个只含有数字的列表
# 返回列表中的所有数字的和

# 步骤拆分：
# 1，创建一个新的变量用于保存这个和
# 2，遍历列表中的所有元素
# 3，将列表中的每一个元素加到刚刚创建的变量中
def summ(list):
    res=sum(list)
    return res  # odd 奇数  even 偶数
    pass


summ([100, 300, 700, 4, 3])

# product   求积  [100, 300, 700, 4, 3]


def product(list):
    res=product(list)
    return res  # odd 奇数  even 偶数
    pass


# product([100, 300, 700, 4, 3])

# Todo 9 练习 4
# 创建一个函数，这个函数接受一个只含有数字的列表
# 返回列表中的所有数字的平均数

# 步骤拆分：
# 1，调用练习 3 的求和函数
# 2，用练习 3 的函数值 / 列表元素的个数
def average(list):
    a=0
    b=sum(list)
    for i in list:
        a=a+1
    pass
    res=b/a
    return res
    pass

    


# average([100, 300, 700, 4, 3])

# Todo 10 练习 5
# 创建一个函数，这个函数接受一个只含有数字的列表
# 返回列表中的所有数字中的最小值.

# 步骤拆分：
# 1，先假设一个最小值，比如就是列表中的第一个值
# 2，用假设的这个最小值和列表中的每一个元素做比较
#   如果比这个假设的最小值小，那么把最小值设为当前值
# 3，循环结束后返回这个最小值
def minn(list):
    res=min(list)
    return res
log(minn([100, 0, 700, 4, 3]))


# max
def maxx(list):
    res=max(list)
    return res

    pass
log(maxx([0,23232,24,4454,67678678]))
# for 循环
# --------
# for 循环和 while 循环的区别
# 1，while 无限循环
# 2，while 条件

# 1, 指定次数
# 2， for + list
# --------

def intro_new_loop():
    # nums = [200, 300, 10]
    # # Todo 1 while loop
    # i = 0
    # while i < 3:
    #     log('while', i)
    #     i = i + 1
    for i in range(3):
        log("for",i)

    # Todo 2 for loop
    # range 1 3   -->   1  2
    # range 1 4   -->   1  2  3


intro_new_loop()


def intro_list_loop():
    nums = [100, 300, 'Yao', 'hello', ['1', '2']]
    for e in nums:
        log('a:', e)


intro_list_loop()


def learn_print2():
    # 循环 loop
    # i = 0
    # while i < 3:
    #     log('loop i:', i)
    #     i = i + 1
    for i in range(3):
        log('loop i:',i)

learn_print2()
