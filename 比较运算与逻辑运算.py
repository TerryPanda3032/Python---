'''
Author: TERRY
Date: 2022-02-17 21:37:46
LastEditors: TERRY
LastEditTime: 2022-04-29 10:36:28
FilePath: \Python系统课\比较运算与逻辑运算.py
Description: 
'''
# 算术运算
#  + - *  / ** // %

log = print

# print(2 ** 2)  # 2 * 2
# print(3 ** 3)  # 3 * 3 * 3
# print(4 ** 3)  # 4 * 4 * 4

# log(10 // 3)        # 3
# log(10 % 3)         # 1  10 / 3 = 3 ... 1

# 比较运算和逻辑操作
#
# if 判断的条件(括号里的表达式)其实是一个值, 这种值叫 布尔值(bool) False True
a = 10
log('aa', a < 3)
if a != 3:
    log('a != 3')
else:
    log('不成立')

# 这种值只有两种结果, 一个是真(True), 一个是假(False)
# 在 Python 中, 这两种值分别是 True 和 False
#
# 1 > 2 实际上是一个值, False
# if 是根据这个值来决定执行的语句的
#
# 一共有 6 个常用比较运算
# 分别是
# 相等, 不等, 小于, 大于, 小于等于, 大于等于
# ==
# !=
# <
# >
# <=
# >=

# 例子
# 1 == 1    True
# 1 == 2    False
# 1 != 1    False
# 1 != 2    True
# 1 > 2     False
# 1 < 2     True
# 1 <= 1    True
# 1 >= 1    True


# 除了比较运算, 还有三种逻辑操作
# 三种逻辑操作分别是 与, 或, 非
# 在 Python 中分别如下
# and
# or
# not
#
# 用到的地方很广, 比如登录网站的时候, 服务器做如下判断
# if 用户名存在 and 密码验证成功:
#     登录成功
# else:
#     登录失败

# input

# 密码程序

# 计算器


# 注意
# 比较运算和逻辑操作的结果是 bool(布尔类型), 结果是 True 和 False

# 例子
# 1 == 1 and 2 == 2    # True
# 1 == 1 and 1 == 2    # False
# 1 == 1 or 1 == 2     # True
# 1 == 2 or 2 == 2     # True
# 1 == 2 or 1 == 2     # False
# not (1 == 1)         # 加个括号方便看清楚逻辑

# 1 == 1 and 2 == 2 or 1 == 2
# ((1 == 1) and (2 == 2)) or (1 == 2)


# 可以加括号来让代码更直观一点
# ((1 == 1) and (2 == 2)) or (1 == 2)
# print('1 == 1 and 2 == 2', 1 == 1 and 2 == 2)

#作业：
'a124' == 'a123' and 1 == 1
'a122' == 'a122' and 1 == 3
'a124' == 'a124' or 1 == 2
not ('a' == 'a' and 1 == 1)
2 != 1 and 1 == 1
not(3 == 2) or 3 == 9





