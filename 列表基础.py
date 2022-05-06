'''
Author: TERRY
Date: 2022-03-08 20:57:34
LastEditors: TERRY
LastEditTime: 2022-04-04 21:57:28
FilePath: \Python系统课\列表基础.py
Description: 
'''
# '''
# Author: TERRY
# Date: 2022-03-08 20:57:34
# LastEditors: TERRY
# LastEditTime: 2022-03-22 21:38:15
# FilePath: \Python系统课\列表基础.py
# Description: 
# '''
# # 复习
# # --------
# # 0, log print
# # 推荐使用 log 来进行数据的打印
# # log 三个字母
# # print 五个字母
# # --------

# log = print

# def learn_print1():

#     log('Name:', 'Li Yao')

#     # Todo 1 试着打印一下你自己的名字
#     log('name','TERRY')
#     # 变量 a 和 b 有什么不同呢？
#     a = 123
#     b = "123"

#     # 我们在使用 log 的时候，通常前面会加入一个字符串
#     # 尤其是有很多 log 的时候，这样会方便我们确定到底是哪个 log 的输出
#     # 内建函数 type 类型
#     log('a:', a, type(a))       # int
#     log('b', b, type(b))        # str

# learn_print1()

# def learn_print2():
#     # 循环 loop
#     i = 0
#     while i < 3:
#         log('loop i:', i)
#         i = i + 1


# learn_print2()


# # --------
# # 1.1, 复习数据类型 data type
# # 1.2, 复习 return
# # --------


# def data_type():
#     a = 10      # 整型 int
#     d = 0.12  # 浮点数 float

#     # 字符串 string  ''  ""
#     b = 'hi'
#     c = "hello 10"
#     c_1 = '''
#     fjkdafkalsj
#     jfakldjfakj
#     fdlkajf
#     '''
#     log('c', c_1)

#     # 1 0 布尔值(boolean)
#     f = True
#     g = False
#     # log('d:', type(d), type(a), type(b), type(c), type(f), type(g))


#     return b + c

# a = data_type()
# log('!!!', a)

# Todo 2
# 定义一个函数，函数名为：
# plus(a, b)
# 函数会将 a 和 b 加在一起并返回



from cv2 import log


def plus(a, b):
    list_plus=[a, b]
    c=sum(list_plus)
    return c
# plus(1,2)
# # --------
# # 2, list
# # --------

# # 数据是如何储存在计算机中的？
# # 第一个数据结构：列表 list

# # 1, 如何创建一个列表 list
# # 和创建变量是类似的
# #   列表名
# #   []
# #   列表中的元素用 , 分隔

# # 数据的操作最重要的就是：增删改查

# # 1，如何创建一个列表
# def create_list():
#     list_1 = [1, 3, 4, 5]
#     list_2 = [1, 3, 'Lucas', 'Susan']
#     list_3 = [1, 3, 'Lucas', 'Susan', list_1]

#     log('list_1: ', list_1)
#     log('list_2: ', list_2)

#     # Todo 3 Try to log list_3
#     log('list_3: ', list_3)


# # create_list()

# # 2，如何访问列表中的元素
# def visit_list1():
#     list_1 = [1, 3, 4, 5]
#     list_2 = [1, 3, 'Lucas', 'Susan']
#     list_3 = [1, 3, 'Lucas', 'Susan', list_1]
#     log('用下标访问 list 中的元素:')
#     log('list_2[0]', list_2[0])
#     log('list_2[1]', list_2[1])
#     log('list_2[1]', list_2[2])

#     # Todo 4 如何打印出列表中的第三个，第四个元素
#     log(list_3[3],list_3[4])

#     # 假如我们访问一个不存在的元素
#     # log('list_1[4]', list_1[4])

# visit_list1()

# # 3, 假如一个列表中有 1000 个元素，那该怎么办？
# # 手动访问元素当然是低效的
# # 可以用循环来访问元素，这个过程叫 遍历 (traversal)
# def visit_list2():
#     # 需要复制列表，否则拿不到 (作用域)
#     list_1 = [1, 3, 4, 5]
#     list_3 = [1, 3, 'Lucas', 'Susan', list_1]
#     i = 0
#     while i < 5:
#         log('list3', list_3[i])
#         i = i + 1

# visit_list2()

# # Todo advance
def practice():
    import random
   
    l = [random.randint(1, 999) for i in range(100)]

# practice()

# # 4，自动获得列表中的元素个数
# def length_of_list():
#     list_1 = [1, 3, 4, 5]
#     list_2 = [1, 3, 'Lucas', 'Susan']
#     list_3 = [1, 3, 'Lucas', 'Susan', list_1]
#     # 内建函数 len()
#     log('求 list 长度', len(list_1))

#     length = len(list_3)
#     log(length)

#     # Todo 4 log list_2 的长度
#     print(len(list_2))
#     # Todo 5 改进循环
#     for i in list_3:
#         log('list3', i)

# length_of_list()

# # Todo 6 练习 1
# # 建一个函数名字为 log_list
# # log_list(list)
# # 输入一个 list 自动打印出 list 中的所有元素
def log_list(list):
    list=input('list')
    return list
    pass
# print(log_list(list))

log=print

# Todo 7 练习 2
# 创建一个函数，这个函数接受一个只含有数字的列表
# 打印出这个列表中的所有偶数
def list2(list):
    list=[1,2,3,4,5,6,7,8,9,10]
    for i in list:
        temp1=i
        if temp1%2==0:
            log(temp1)
        else:
            pass
        pass
    pass
# list2(list)
# 步骤拆分：
# 1，遍历列表中的所有元素
# 2，检查每一个元素是否是偶数 (通过求余数(%)来判断是否是偶数)
# 3，如何是偶数，就 log 这个偶数


# Todo 8 练习 3
# 创建一个函数，这个函数接受一个只含有数字的列表
# 返回列表中的所有数字的和``
# def list3(list):
#     list=[12321,1231,4545,6767]
#     res=sum(list)
#     return res
# log(list3(list))
# 步骤拆分：
# 1，创建一个新的变量用于保存这个和
# 2，遍历列表中的所有元素
# 3，将列表中的每一个元素加到刚刚创建的变量中


# Todo 9 练习 4
# 创建一个函数，这个函数接受一个只含有数字的列表
# 返回列表中的所有数字的平均数
def list5(list):
    list=[12321,1231,4545,6767]
    res=sum(list)
    a=0
    for i in list:
        a=a+1
        pass
    res=res/a
    return res
log(list5(list))
# 步骤拆分：
# 1，调用练习 3 的求和函数
# 2，用练习 3 的函数值 / 列表元素的个数


# Todo 10 练习 5
# 创建一个函数，这个函数接受一个只含有数字的列表
# 返回列表中的所有数字中的最小值
def list7(list):
    list=[12321,1231,4545,6767]
    res=min(list)
    return res



# 步骤拆分：
# 1，先假设一个最小值，比如就是列表中的第一个值
# 2，用假设的这个最小值和列表中的每一个元素做比较
#   如果比这个假设的最小值小，那么把最小值设为当前值
# 3，循环结束后返回这个最小值

