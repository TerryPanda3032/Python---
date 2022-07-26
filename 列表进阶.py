log = print

# --------
# 1 列表添加
# --------


# def append_list():
#     l = [77, 98, 32, 10]
#     log('append 之前', l)
#     l.append('新元素')
#     log('append 之后', l)
#     # Todo 1 往 l 这个列表中加入 1000, 44 和 你的名字
#     l.append('1000')
#     l.append('44')
#     l.append('彭辰涵')
#     print(l)
#     pass
# append_list()


# append_list()


# def practice1():
#     # Todo 2 如何生成一个列表，这个列表中有 1 ~ 10
#     # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\
#     list2=[]
#     for i in range(1,10+1):
#         list2.append(i)
#         pass
#     print(list2)
#     pass
# practice1()


# def practice2():
#     # Todo 3 如何生成一个列表，这个列表中有 1 ~ 100
#     # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ...]
#     list3=[]
#     for i in range(1,100+1):
#         list3.append(i)
#         pass
#     print(list3)
#     pass
# practice2()


# def practice3():
#     # Todo 4 如何生成一个列表，这个列表中有 1 ~ 100 的偶数
#     # [2, 4, 6, 8, 10 ...]
#     list4=[]
#     list4=[i for i in range(1,101) if i%2!=1]
#     print(list4)
# practice3()

# --------
# 2 列表修改
# --------


def change_list():
    l = [1, 2, 100, 'nihao']
    log('改之前', l)
    l[3] = 'hello'
    log('改之后', l)


def practice4():
    # 把列表中的每一个元素都 + 1
    numbers = [100, 200, 300, 400]


def practice5():
    # 把列表中的每一个偶数元素都 + 1
    numbers = [100, 201, 300, 433]


# --------
# 3 列表删除
# --------

def delete_list():
    l = [1, 2, 100, 33]
    log('删除之前', l)
    # del delete 删除
    del l[0]
    log('删除之后', l[1])


def practice6():
    # 把列表中的每一个偶数元素都删除掉
    numbers = [100, 201, 300, 433, 444, 550]


def practice7():
    # 把列表中的每一个奇数元素都删除掉
    numbers = [1, 201, 420, 521, 77, 87]

