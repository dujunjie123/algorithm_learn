# -*- coding: utf-8 -*-
# @Time : 2023/3/19 11:03
# @Author : 杜俊杰
# @File : p12.py
# @Project : algorithm_learn
# @File Description :

from timeit import Timer

def t1():
    l = list()
    for i in range(1000):
        l.append(i)


def t2():
    l = list()
    for i in range(1000):
        l = l + list(i)


time1 = Timer("t2()","from __main__ import t2")
print(time1.timeit(10000))


# if __name__ == '__main__':