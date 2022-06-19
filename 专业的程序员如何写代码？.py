"""
Author: TERRY
Date: 2022-05-03 21:03:49
LastEditors: TERRY
LastEditTime: 2022-05-28 10:55:15
FilePath: \python---\专业的程序员如何写代码？.py
Description:
"""
# --------
# 1, 自动化测试
# 如何自动测试你的代码？
# --------

log = print

# ======
# 测试
# 本次作业起, 我们开始使用自动测试的方法来验证结果
# 提交作业的时候, 必须实现函数和测试函数
# ======
#
# 定义我们用于测试的函数
# ensure 接受两个参数
# condition 是 bool, 如果为 false, 则输出 message
# 否则, 不做任何处理

# condition  1 == 1  1 != 1  2 > 3
def ensure(condition, message):
    # 在条件不成立的时候, 输出 message
    # condition: true false
    if condition:
        log("*** 测试成功")
    else:
        log("*** 测试失败:", message)

    # not 1 != 1
    # if not xxx
    # if (not condition):
    #     log('*** 测试失败:', message)
    # else:
    #     log('*** 测试成功')


# ensure(1 == 1, '1 和 1 不相等')

# 例子
# 测试的使用
#
# 注意看, 我们使用了上面定义的 ensure 来进行测试
def test_sample():
    # 1, 条件
    # 2, 对你的测试打了一个标签
    ensure(1 == 1, "如果测试失败, 这句话会被打印出来")
    ensure(1 > 2, "测试 1 > 2 失败")


# test_sample()
# 调用上面的 test_sample 可以得到如下输出
# *** 测试失败: 测试 1 > 2 失败

# 例子 1
def sum(number_list):
    # 先设置一个变量用来存列表的和
    s = 0
    for i in range(len(number_list)):
        # 用变量 n 保存元素的值
        n = number_list[i]
        # 累加到变量 s
        s = s + n
    # 循环结束, 现在 s 里面存的是列表中所有元素的和了
    return s


a = [1, 2, 3, 4]
log("sumL:", sum(a))


# 演示测试函数
def test_sum():
    a = [1, 2, 3, 4]
    ensure(sum(a) == 10, "测试列表 a")
    # 1, 检查你的测试答案是否正确
    # 2, log 这个函数，看看这个函数具体的值是多少
    log("!!!", sum(a))
    ensure(sum([10, 100, 1000]) == 1110, "测试列表 2")


test_sum()
# Todo 1
# 参数是一个只包含数字的列表 (number_list/number_list)
# 求列表的乘积
# 函数定义是
# product(number_list)


def product(number_list):
    product = 1
    for x in number_list:
        product = product * x
    return product


print(product([1, 3, 5, 7]))
# 提示：
#     通过遍历列表，然后累乘的方式计算列表的乘积，参考例子 1
#
# 分步提示：
#     1. 先设置一个变量 s 用来存列表的乘积，注意这里 n 的初始值
#     2. 遍历列表，用变量 n 保存元素的值
#     3. 累乘每次的变量 n 到变量 s
#     4. 循环结束后，变量 s 里面存的是列表中所有元素的乘积, 返回变量 s（很重要，一定要 return s）


def test_product():
    numbers = [1, 2, 3, 4]
    result = 24
    ensure(product(numbers) == result, "error product 1")
    ensure(product([0, 7, 9]) == 0, "error product 2")
    ensure(product([]) == 1, "error product 3")
    log("$$$ product 测试完成")


test_product()


# Todo 2
# 返回一个数的绝对值
# 函数定义是
# abs(n)


# 分步提示：
#     1. 如果 n < 0，就把 n 的值赋值成 -n
#     2. 返回 n 的值（很重要，一定要 return n）


def abs(n):
    pass


def test_abs():
    ensure(abs(0) == 0, "abs error, 0")
    ensure(abs(2) == 2, "abs error, 2")
    ensure(abs(-3) == 3, "abs error, -3")
    log("$$$ abs 测试完成")


# Todo 3
# 参数是一个只包含数字的列表
# 求列表中所有数字的平均数
# 函数定义是
# average(number_list)

# 提示：
#     求列表的平均数就是先求出列表中元素的总和，然后除以列表的长度（即元素的个数）

# 分步提示：
#     1. 使用例子 1 中的 sum 函数来计算列表中所有元素的总和
#     2. 使用 len 函数计算出列表中元素的个数
#     3. 使用列表中元素的总和除以列表中元素的个数，得到平均数
#     4. 返回平均数


# Todo 3.1 自己尝试写一个 test_average 函数


# Todo 4
# 参数是一个数字 n
# 返回以下序列的结果
# 1 - 2 + 3 - 4 + 5 ... n

# sum1(n)


# 提示：
#     观察序列可以发现一个规律：奇数的时候是加，偶数的时候是减
#     一看到 1 2 3 4 5 每次都加 1，就想到了循环

# 分步提示：
#     1. 先设置一个变量 s 用来存序列的和，初始值为 0
#     2. 循环 n 次，从 1 开始，到 n + 1 结束，即包括 n 但是不包括 n + 1
#     3. 判断每次循环的值。如果是奇数，累加这个数到 s 上，如果是偶数，累减这个数到 s 上
#     4. 循环结束后，变量 s 里面存的是序列的和
#     5. 返回变量 s（很重要，一定要 return s）


def sum1(n):
    pass


def test_sum1():
    ensure(sum1(1) == 1, "sum1 error 1")
    ensure(sum1(5) == 3, "sum1 error 2")
    ensure(sum1(3) == 1 - 2 + 3, "sum1 error 3")
    log("$$$ sum1 测试完成")


# Todo 5
# 参数是一个数字 n
# 返回以下序列的结果
# 1 + 2 - 3 + 4 - ... n

# sum2(n)


# 分步提示：
#     1. 先设置一个变量 s 用来存序列的和，初始值为 1，这样就可以从 2 开始计算循环了
#     2. 循环 n - 1 次，从 2 开始，到 n 结束（包括 n）
#     3. 判断每次循环的值。
#        如果是第一个数字（这里是从 2 开始的），观察式子的规律，
#        从 2 开始之后，当一个数字是奇数时，就是减去这个数（比如说 3 5 7 9...）。
#        当一个数字是偶数时，就是加上这个数（比如 2 4 6 8...）。
#     4. 循环结束后，变量 s 里面存的是序列的和
#     5. 返回变量 s（很重要，一定要 return s）


def sum2(n):
    pass


def test_sum5():
    ensure(sum2(1) == 1, "sum2 error 1")
    ensure(sum2(2) == 3, "sum2 error 2")
    ensure(sum2(4) == 4, "sum2 error 3")
    ensure(sum2(5) == 1 + 2 - 3 + 4 - 5, "sum2 error 4")
    log("$$$ sum2 测试完成")


# Todo 6
# 一起来实现一个数学概念
# 1！== 1
# 2！== 1 * 2
# 5！== 1 * 2 * 3 * 4 * 5
# 注意如果是 0 的话，得数就是 1，规定！
# 0！== 1
# Todo 6.1 如果是：
# 7！== ？？
# 4！== ？？

# 我们一起来实现 fac 函数，用来在计算机中模拟上面的阶乘
# 接受一个参数 n

# 返回 n 的阶乘, 1 * 2 * 3 * ... * n 的乘积结果
# fac(1) == 1
# fac(5) == 120
# fac(n)


# 提示：
#     计算从 1 到 n 的阶乘，重复了 n 次，所以可以用循环来处理

# 分步提示：
#     1. 先设置一个变量 s 用来存阶乘，初始值为 1
#     2. 用循环把 1 到 n 的数字相乘保存到 s 中
#     3. 循环结束后，变量 s 里面存的是从 1 到 n 的阶乘, 返回变量 s（很重要，一定要 return s）


def fac(n):
    pass


def test_fac():
    ensure(fac(1) == 1, "fac error 1")
    ensure(fac(5) == 120, "fac error 2")
    ensure(fac(0) == 1, "fac error 3")
