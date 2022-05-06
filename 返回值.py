# 函数返回值
#
# 函数不仅可以合并操作重复性的代码
# 还可以通过计算得到一个结果, 结果就是返回值
# 函数可以有「返回值」
# 返回值的意思是函数调用的结果是一个值, 可以被赋值给变量

log = print

# 作用域
# 全局变量
# r = 10

# 定义一个函数 add
# 接受 a b 两个参数
def add(a, b):
    # return 返回
    # 用 return 语句来得到一个返回值
    # 函数执行到 return 语句的时候就结束了
    # result 结果
    r = a + b
    return r

# 1，无法在函数外部获得函数内的东西
# 2，如果想要获得那么需要 return

# 用法
# None 空 啥都没有
log('add 函数的返回值', add(1, 2))
# log('r2:', r)
number = add(2, 3)
# log('r3:', r)
log('add 函数的返回值 number', number)


# 注意看上面的语句, add(2, 3) 被当做一个值赋值给了变量 number
# 也就是说这个函数调用是一个数值, 数值的值就是函数的返回值


# 例如, 使用函数来求绝对值
# -1    1
# 1     1
# -100  100
# 0     0
# -30
# -20
# -10000
def abs(n):
    pass

# print(abs(0))
# print(abs(-8))
# print(abs(3))


# 函数执行遇到 return 就结束
def minus(a, b):
    print('这句话肯定能打印出来')
    return a - b
    print('这一句是不会被执行的, 因为 return 的时候函数就结束了')


print('minus 函数', minus(2, 3))


# 例子
# 使用函数检查一个数字是否是奇数(奇数对 2 取余数不等于 0)
def is_odd(n):
    # 取余数的操作符是 %
    if n % 2 != 0:
        return True
    else:
        return False


#     if True:
#         return True
#     else:
#         return False


def is_odd(n):
    pass


# 返回两个参数中较小的一个
def min(a, b):
    pass



# Todo 1
#
# 实现 max 函数, 接收两个参数, 返回较大的那一个值


# Todo 2
#
# 实现 plus 函数, 接收两个参数, 在函数内部打印出两个参数的和


# Todo 3
#
# 实现 plus 函数, 接收两个参数, 用函数返回的方法，打印出两个参数的和


# Todo 4
#
# 实现 is_even 函数, 偶数返回 True, 奇数返回 False


# Todo 5
#
# 实现 compare 函数, 接受一个参数，如果这个数大于 0，返回 True，反之返回 False


# Todo 6
#
# 实现 compare 函数, 接受两个参数，如果第一个数大于第二个数，返回 True，反之返回 False


